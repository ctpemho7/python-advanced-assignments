from matrix import Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[2, 0], [1, 2]])

C = A @ B
C.save_to_file("matrix@.txt")

C = A + B
C.save_to_file("matrix+.txt")

C = A * B
C.save_to_file("matrix*.txt")
