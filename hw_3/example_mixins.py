from matrix_calc.mixins import Matrix

import numpy as np
np.random.seed(0)

A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
path = "hw_3/artifacts/2"

C = A + B
C.save_to_file("matrix+.txt", path)

C = A * B
C.save_to_file("matrix*.txt", path)

C = A @ B
C.save_to_file("matrix@.txt", path)
