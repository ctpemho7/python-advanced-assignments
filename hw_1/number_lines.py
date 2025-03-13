import click

@click.command()
@click.argument('filename', type=click.File('r'), required=False)
def number_lines(filename):
    """
    CLI-приложение для нумерации строк из файла или stdin.
    Повторяет поведение утилиты 'nl -b a'
    Если файл не передан, то скрипт читает строки из stdin.
    """
    stream = filename if filename else click.get_text_stream('stdin')

    line_number = 1 
    for line in stream:
        if line.strip():
            click.echo(f"{line_number:>6}  {line}", nl=False)
            line_number += 1
        else:
            click.echo(line, nl=False)
    click.echo()

if __name__ == "__main__":
    number_lines()
