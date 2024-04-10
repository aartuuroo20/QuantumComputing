import csv
import time
import numpy as np

from functions import get_theoric_probability, load_probability, get_qlm_probability
from matplotlib import pyplot as plt
from qat.qpus import get_default_qpu
from qlmaas.qpus import LinAlg
from scipy.stats import entropy, chisquare
from pre_benchmark import PreBenchmark

class Benchmark:
    def __init__(self):
        self.number_qubits = 0
        self.load_method = ""
        self.qpu = ""
        self.mean = 0
        self.sigma = 0
        self.step = 0
        self.shots = 0
        self.ks = 0
        self.kl = 0
        self.chi2 = 0
        self.pvalue = 0
        self.elapsed_time = 0
        self.quantum_time = 0
    
    def run_benchmark(self, n_qubits: int, samples: int, output_csv: str):
        # Open CSV file in 'append' mode
        with open(output_csv, 'a', newline='') as csvfile:
            fieldnames = [
                'n_qubits', 'load_method', 'qpu', 'mean', 'sigma', 
                'KS', 'KL', 'chi2', 'pvalue', 'elapsed_time', 'quantum_time'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
                
            for i in range(samples):
                tick = time.time()
                x, pn, mu, sigma, deltax, shots, norm = get_theoric_probability(n_qubits)
                plt.plot(x, pn, '-o')

                Up_KPtree = load_probability(pn, "KPTree")
                job = Up_KPtree.to_job()

                qpu = LinAlg()
                result, quantum_time = get_qlm_probability(Up_KPtree, shots, qpu)

                ks = np.abs(pn.cumsum() - result.cumsum()).max()
                epsilon = pn.min() * 1.0e-5
                kl = entropy(pn, np.maximum(epsilon, result))

                plt.plot(x, pn, '-')
                plt.plot(x, result, 'o')
                plt.legend(["theoretical pdf", "quantum pdf"])

                # Chi square
                observed_frequencies = np.round(result * shots, decimals=0)
                expected_frequencies = np.round(pn * shots, decimals=0)
                
                chi2, pvalue = chisquare(
                    f_obs=observed_frequencies,
                    f_exp=expected_frequencies
                )

                tack = time.time()
                elapsed_time = tack - tick

                self.number_qubits = n_qubits
                self.load_method = "KPTree"
                self.qpu = "default_qpu"
                self.mean = mu
                self.sigma = sigma
                self.step = deltax
                self.shots = shots
                self.ks = ks
                self.kl = kl
                self.chi2 = chi2
                self.pvalue = pvalue
                self.elapsed_time = elapsed_time
                self.quantum_time = quantum_time

                data = {
                    'n_qubits': self.number_qubits,
                    'load_method': self.load_method,
                    'qpu': self.qpu,
                    'mean': self.mean,
                    'sigma': self.sigma,
                    'KS': self.ks,
                    'KL': self.kl,
                    'chi2': self.chi2,
                    'pvalue': self.pvalue,
                    'elapsed_time': self.elapsed_time,
                    'quantum_time': self.quantum_time,
                }
                
                writer.writerow(data)

pre_benchmark = PreBenchmark()
pre_benchmark.run_benchmark()
pre_benchmark.get_results()

benchmark = Benchmark()
benchmark.run_benchmark(n_qubits=4, samples=int(pre_benchmark.ideal_samples), output_csv='benchmark_results.csv')


    


'''
list_of_elapsed_times = []
list_of_quantum_times = []
list_of_ks = []
list_of_kl = []
list_of_chi2 = []
list_of_pvalue = []

for i in range(10):
    tick = time.time()
    x, pn, mu, sigma, deltax, shots, norm = get_theoric_probability(5)
    plt.plot(x, pn, '-o')

    Up_KPtree = load_probability(pn, "KPTree")
    job = Up_KPtree.to_job()

    qpu = get_default_qpu()
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

    list_of_elapsed_times.append(elapsed_time)
    list_of_ks.append(ks)
    list_of_kl.append(kl)
    list_of_chi2.append(chi2)
    list_of_pvalue.append(pvalue)
    list_of_quantum_times.append(quantum_time)

#Calculating the mean time and standard deviation
mean_time = np.mean(list_of_elapsed_times)
std_time = np.std(list_of_elapsed_times)

#Calculating the mean and standard deviation of the quantum time
mean_quantum_time = np.mean(list_of_quantum_times)
std_quantum_time = np.std(list_of_quantum_times)

#Calculating the mean and standard deviation of the Kolmogorov-Smirnov
mean_ks = np.mean(list_of_ks)
std_ks = np.std(list_of_ks)

#Calculating the mean and standard deviation of the Kullback-Leibler
mean_kl = np.mean(list_of_kl)
std_kl = np.std(list_of_kl)

#Calculating the mean and standard deviation of the chi2
mean_chi2 = np.mean(list_of_chi2)
std_chi2 = np.std(list_of_chi2)

#Calculating the mean and standard deviation of the pvalue
mean_pvalue = np.mean(list_of_pvalue)
std_pvalue = np.std(list_of_pvalue)

r = 0.05
em = 1.0e-4

#Check if 1.96 is the correct value for the confidence interval
number_repetitions_t = ((1.96 * std_time) / (r * mean_time)) ** 2
number_repetitions_m_ks = (( std_ks * 1.96) / em) ** 2
number_repetitions_m_kl = (( std_kl * 1.96) / em) ** 2

ideal_samples = max(number_repetitions_t, number_repetitions_m_ks, number_repetitions_m_kl)

#Save the data in a csv file
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

with open('data.csv', 'w') as f:
    for key in data.keys():
        f.write("%s,%s\n"%(key,data[key]))
    f.close()
'''
