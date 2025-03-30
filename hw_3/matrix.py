import os
from typing import Iterable


class Matrix:
    def __init__(self, data: Iterable):
        if not data or not all(isinstance(row, Iterable) for row in data):
            raise ValueError("Входной параметр - двумерный итератор")
        
        # Проверяем, что все строки имеют одинаковую длину
        row_lengths = [len(row) for row in data]
        if len(set(row_lengths)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину!")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        """ Покомпонентное сложение двух матриц """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения!")
        
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)


    def __mul__(self, other):
        """Покомпонентное умножение двух матриц """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для умножения!")
        
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)


    def __matmul__(self, other):
        """Матричное умножение """
        if self.cols != other.rows:
            raise ValueError(
                "Операция невозможна, проверьте размерность матрицы: "
                f"число столбцов первой матрицы ({self.cols}) "
                f"должно совпадать с числом строк второй матрицы ({other.rows})"
            )
        
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def save_to_file(self, filename, path="artifacts"):
        """
        Сохраняет матрицу в файл.
        
        Параметры:
            filename (str): Имя файла (например, "matrix.txt").
            path (str): Путь к директории. По умолчанию - "artifacts".
        """
        os.makedirs(path, exist_ok=True)
        
        filepath = os.path.join(path, filename)
        
        with open(filepath, "w") as f:
            f.write(str(self))
        
