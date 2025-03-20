# Комментарии к ДЗ 2 

Все артефакты представлены в `hw_2/artifacts/`.

Пример сгенерированного файла в `hw_2/artifacts/final_output.tex`.

## Задание 1

Функция: `generate_table`, модуль `generate`.

Артефакт: `output_step1.tex`.

## Задание 2

Функция: `generate_image`, модуль `generate` генерирует. 

Ссылка на пакет в pypi: [ссылка](https://pypi.org/project/pa-latex/)

## Задание 3

В качестве базового докер-образа используется готовый образ с Python 3.10 и TexLive.

Поскольку изображение берется из папки artifacts, монтируем её:

```bash
docker build -t docs . 
docker run -v ./artifacts:/workspace/artifacts docs
```

