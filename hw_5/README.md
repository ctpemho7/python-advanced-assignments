# Коментарии к ДЗ 5

Весь код представлен в папке `hw_5`.

## Задание 1

Код для скачивания картинок: `img_parser.py`. Позволяет указать количество картинок, папку для загрузки и URL. По умолчанию скачивает shitposting skeletons.

Варианты запуска:

```sh
python img_parser.py 10 --output very_cool_pictures
```

```sh
python img_parser.py 15 --output my_people --url https://thispersondoesnotexist.com/
```

Пример вывода программы:

```
[01:09:08.891411] Downloaded very_cool_pictures/image_3.jpg
[01:09:08.896245] Downloaded very_cool_pictures/image_9.jpg
[01:09:08.950402] Downloaded very_cool_pictures/image_0.jpg
[01:09:08.990414] Downloaded very_cool_pictures/image_7.jpg
[01:09:09.021902] Downloaded very_cool_pictures/image_4.jpg
[01:09:09.043337] Downloaded very_cool_pictures/image_5.jpg
[01:09:09.087589] Downloaded very_cool_pictures/image_2.jpg
[01:09:09.104336] Downloaded very_cool_pictures/image_1.jpg
[01:09:09.122799] Downloaded very_cool_pictures/image_8.jpg
[01:09:09.289510] Downloaded very_cool_pictures/image_6.jpg
```