from matrix_calc.hash import HashMatrix
from matrix_calc.mclass import Matrix
import numpy as np

import os

np.random.seed(0)


def find_hash_collision():
    """
    Функция для поиска коллизии. 
    Возвращает две разные матрицы с одинаковым хэшем или None, если не найдены.
    """

    np.random.seed(52)
    hashes = {}
    max_attempts = 10000

    for _ in range(max_attempts):
        m = HashMatrix(np.random.randint(0, 10, (2, 2)).tolist())
        h = hash(m)

        if h in hashes and hashes[h].data != m.data:
            return hashes[h], m
        hashes[h] = m

    return None, None



if __name__ == "__main__":
    A, C = find_hash_collision()

    if not A:
        print("Коллизия не найдена!") 

    path = "hw_3/artifacts/3"

    print(f"Хэш матрицы А: {hash(A)}")
    print(A)
    A.save_to_file("A.txt", path)

    print(f"Хэш матрицы C: {hash(C)}")
    print(C)
    C.save_to_file("C.txt", path)

    # два одинаковых с хэшем
    B = D = HashMatrix(np.random.randint(0, 10, (2, 2)).tolist())

    print("Матрица В:")
    print(B)
    B.save_to_file("B.txt", path)

    print("Матрица D:")
    print(D)
    D.save_to_file("D.txt", path)

    print("Результат произведения A @ B с кешем")    
    hash_ab = A @ B
    print(hash_ab)
    hash_ab.save_to_file("AB.txt", path)

    print("Результат произведения C @ D с кешем")    
    hash_cd = C @ D
    print(hash_cd)


    print("Настоящий результат произведения C @ D без кеша")    
    true_cd = Matrix(C.data) @ Matrix(D.data)
    print(true_cd)
    true_cd.save_to_file("CD.txt", path)


    filepath = os.path.join(path, "hash.txt")
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Хеш матрицы AB: {hash(hash_ab)}\n"
                f"Хеш матрицы CD: {hash(hash_cd)}\n")
