import os
import numbers
import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class SaveMixin:
    """
    Миксин для сохранения матрицы в файл
    """
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
        

class DisplayMixin:
    """
    Миксин для получения представления матрицы
    """
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.value])
    
    def __repr__(self):
        return str(self)


class GetterSetterMixin:
    """
    Миксин для getter и setter
    """
    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        self.data = np.asarray(value)


class Matrix(NDArrayOperatorsMixin, SaveMixin, DisplayMixin, GetterSetterMixin):
    """
    Класс Matrix на примесях и NDArrayOperatorsMixin
    """
    def __init__(self, value):
        self.value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of
            # _HANDLED_TYPES. Use ArrayLike instead of type(self)
            # for isinstance to allow subclasses that don't
            # override __array_ufunc__ to handle ArrayLike objects.
            if not isinstance(
                x, self._HANDLED_TYPES + (Matrix,)
            ):
                return NotImplemented

        # Defer to the implementation of the ufunc
        # on unwrapped values.
        inputs = tuple(x.value if isinstance(x, Matrix) else x
                    for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)
