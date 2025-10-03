#!/usr/bin/python3
"""Module that defines text_indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Символы, после которых нужно ставить два переноса строки
    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            # Берём часть текста от start до текущего символа и убираем лишние пробелы
            line = text[start:i+1].strip()
            print(line)
            print()
            start = i + 1

    # Печатаем остаток текста, если есть
    remainder = text[start:].strip()
    if remainder:
        print(remainder)
