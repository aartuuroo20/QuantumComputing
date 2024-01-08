import numpy as np
from qat.plugins import ScipyMinimizePlugin
from qat.linalg import LinAlg

plugin = ScipyMinimizePlugin(x0=np.random.random(10),
                             method="COBYLA",
                             tol=1e-3,
                             options={"maxiter": 300})

stack = plugin | LinAlg()
# Any job will run, as long as it contains 10 variables!
result = stack.submit(my_job)