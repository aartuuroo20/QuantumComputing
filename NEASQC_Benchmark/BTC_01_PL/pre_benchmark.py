from functions import get_theoric_probability, load_probability, get_qlm_probability
from matplotlib import pyplot as plt
from qat.qpus import get_default_qpu
from qlmaas.qpus import LinAlg
from scipy.stats import entropy, chisquare

import numpy as np
import time

class PreBenchmark:
    def __init__(self):
        self.list_of_elapsed_times = []
        self.list_of_quantum_times = []
        self.list_of_ks = []
        self.list_of_kl = []
        self.list_of_chi2 = []
        self.list_of_pvalue = []
        self.ideal_samples = 0
    
    def run_benchmark(self):
        for i in range(10):
            tick = time.time()
            x, pn, mu, sigma, deltax, shots, norm = get_theoric_probability(5)
            plt.plot(x, pn, '-o')

            Up_KPtree = load_probability(pn, "KPTree")
            job = Up_KPtree.to_job()

            qpu = LinAlg()
            result, quantum_time = get_qlm_probability(Up_KPtree , shots, qpu)

            ks = np.abs(pn.cumsum() - result.cumsum()).max()
            epsilon = pn.min() * 1.0e-5
            kl = entropy(pn, np.maximum(epsilon, result))

            plt.plot(x, pn, '-')
            plt.plot(x, result, 'o')
            plt.legend(["theoretical pdf", "quantum pdf"])

            #Chi square
            observed_frecuency = np.round(
                result * shots, decimals=0)

            expected_frecuency = np.round(
                pn * shots, decimals=0)
                
            chi2, pvalue = chisquare(
                f_obs=observed_frecuency,
                f_exp=expected_frecuency)

            tack = time.time()
            elapsed_time = tack - tick

            self.list_of_elapsed_times.append(elapsed_time)
            self.list_of_ks.append(ks)
            self.list_of_kl.append(kl)
            self.list_of_chi2.append(chi2)
            self.list_of_pvalue.append(pvalue)
            self.list_of_quantum_times.append(quantum_time)
    
    def get_results(self):
        mean_time = np.mean(self.list_of_elapsed_times)
        std_time = np.std(self.list_of_elapsed_times)

        mean_quantum_time = np.mean(self.list_of_quantum_times)
        std_quantum_time = np.std(self.list_of_quantum_times)

        mean_ks = np.mean(self.list_of_ks)
        std_ks = np.std(self.list_of_ks)

        mean_kl = np.mean(self.list_of_kl)
        std_kl = np.std(self.list_of_kl)

        mean_chi2 = np.mean(self.list_of_chi2)
        std_chi2 = np.std(self.list_of_chi2)

        mean_pvalue = np.mean(self.list_of_pvalue)
        std_pvalue = np.std(self.list_of_pvalue)

        r = 0.05
        em = 1.0e-4

        number_repetitions_t = ((1.96 * std_time) / (r * mean_time)) ** 2
        number_repetitions_m_ks = (( std_ks * 1.96) / em) ** 2
        number_repetitions_m_kl = (( std_kl * 1.96) / em) ** 2

        ideal_samples = max(number_repetitions_t, number_repetitions_m_ks, number_repetitions_m_kl)
        self.ideal_samples = ideal_samples

        data = {
            'n_qubits': 8,
            'load_method': 'KPTree',
            'KS_mean': mean_ks,
            'KS_std': std_ks,
            'KL_mean': mean_kl,
            'KL_std': std_kl,
            'chi2_mean': mean_chi2,
            'chi2_std': std_chi2,
            'pvalue_mean': mean_pvalue,
            'pvalue_std': std_pvalue,
            'elapsed_time_mean': mean_time,
            'elapsed_time_std': std_time,
            'quantum_time_mean': mean_quantum_time,
            'quantum_time_std': std_quantum_time,
            'number_repetitions': int(ideal_samples),
        }

        with open('summary.csv', 'w') as f:
            for key in data.keys():
                f.write("%s,%s\n"%(key,data[key]))
            f.close()
        