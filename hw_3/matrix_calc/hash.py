from .mclass import Matrix
from typing import Iterable, Dict, Tuple


class HashMixin():
    """
    Примесь для вычисления хэша матрицы.
    Вычисляется так: sum(A * A) * A.cols * A.rows.
    Сумма произведения квадрата матрицы (поэлементное умножение) на её размерность
    """
    def __hash__(self: Iterable):
        second_power = self * self
        element_sum = sum(sum(row) for row in second_power.data)
        return int(element_sum * self.rows * self.cols)  


class HashMatrix(Matrix, HashMixin):
    # здесь храним кэш, в нем ключ - это кортеж из хэша двух матриц
    _matmul_cache: Dict[Tuple[int, int], 'Matrix'] = {}

    def __matmul__(self, other):
        """Матричное умножение с кэшированием """
        if self.cols != other.rows:
            raise ValueError(
                "Операция невозможна, проверьте размерность матрицы: "
                f"число столбцов первой матрицы ({self.cols}) "
                f"должно совпадать с числом строк второй матрицы ({other.rows})"
            )
        
        cache_key = (hash(self), hash(other))
        if cache_key in self._matmul_cache:
            return self._matmul_cache[cache_key]

        result = HashMatrix([
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ])

        self._matmul_cache[cache_key] = result
        return result
