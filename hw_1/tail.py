import click


LINES_WITHOUT_A_FILE = 17
LINES_WITH_FILE = 10


@click.command()
@click.argument('files', type=click.File('r'), nargs=-1)
def tail(files):
    """
    CLI-приложение, выводящее в 'stdout' последние 10 строк каждого из переданных файлов.
    Упрощенный вариант утилиты 'tail'. 
    При передаче более 1 файла выводит название каждого файла.
    Если файл не передан, то выводит последние 17 строк из 'tail'.
    """

    if not files:
        print_from_stdin()
    else:
        print_from_file(files)


def print_from_lines(lines):
    """
    Функция для вывода в 'stdout' строк из массива строк
    """
    for line in lines:
        click.echo(line, nl=False)


def print_from_stdin():
    """
    Функция получает из 'stdin' последние LINES_WITHOUT_A_FILE и выводит их в 'stdout'
    """
    text_stream = click.get_text_stream('stdin')
    lines = text_stream.readlines()[-LINES_WITHOUT_A_FILE:]
    print_from_lines(lines)


def print_from_file(files):
    """
    Функция выводит в 'stdout' из одного или нескольких файлов последние LINES_WITH_FILE строк 
    """

    for i, file in enumerate(files):
        lines = file.readlines()[-LINES_WITH_FILE:]
        # выводить название файла, если передано более 1 файла
        if len(files) > 1:
            click.echo(f'==> {file.name} <==')
        print_from_lines(lines)
        # пропускать строку, если передано более одного файла. после последнего файла пустая строка не нужна.
        if len(files) > 1 and (i != len(files)-1):
            click.echo()


if __name__ == '__main__':
    tail()