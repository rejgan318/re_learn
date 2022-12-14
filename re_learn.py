"""
Базовые операции с регулярными выражениями

Для отладки https://regex101.com/
"""

import re

text = """
Текст для анализа

Это шапка, ее нужно удалить. Фрагмент текста для парсинга ниже. 
Встречаются и цифры не в основном блоке: 1. Первая    42. Сорок вторая
Критерий начала блока данных для парсинга - цифра в первой позиции строки и дл конца. Данные могут идти в несколько
колонок.
TODO Удалить пробелы с помощью регулярного выражения

1. Один
2. Два
11. Одиннадцать
21. Двадцать один (после re остаются хвостовые пробелы :()       22. Двадцать два (во второй колонке)
30. Тридцать 
"""

first_pos_data = re.search(r"^\d+\. +", text, flags=re.MULTILINE).regs[0][0]
text = text[first_pos_data:]    # delete header without data
result = re.findall(r"\d+\. +(\D*)", text, flags=re.MULTILINE)
result = [r.strip() for r in result]
print(result)
