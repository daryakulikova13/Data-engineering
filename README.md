# Проект реализуется в рамках дисциплины "Инжиниринг управления данными (базовый уровень)"
Проект посвящён анализу белков, входяющих в геном микроорганизма *Pseudomonas aeruginosa*

# Структура проекта
my_data_project/
├── data_loader.py          
├── requirements.txt        
├── pyproject.toml       
├── README.md             
└── notebooks/             

# Результат работы скрипта
Скрипт загружает данные из Google Drive и выводит первую десятку строк:
[Результат выполнения скрипта](screenshot.jpg)

# Описание скрипта
Скрипт `data_loader.py`:
- Загружает CSV файлы из Google Drive по ID
- Выводит информацию о данных (размер, колонки)
- Показывает первые 10 строк для проверки

# Ссылка на датасет
Ссылка на датасет на Google Диске:[Открыть датасет](https://drive.google.com/drive/folders/17_n1YnmEWkbr0EwFk1wTnYzYauQCbaod?hl=ru)

# Результаты преобразования типов данных
## Типы данных ДО обработки:
```
ID                         object
Name                       object
Sequence                   object
Molecular_Weight          float64
Isoelectric_Point         float64
Protein_Length              int64
Amino_Acid_Composition     object
Hydrophobicity            float64
dtype: object
```

## Типы данных ПОСЛЕ обработки:
```
ID                         object
Name                       object
Sequence                   object
Molecular_Weight          float64
Isoelectric_Point         float64
Protein_Length              Int64
Amino_Acid_Composition     object
Hydrophobicity            float64
dtype: object
```

## Вывод скрипта:

Загружаем данные по ссылке:
https://drive.google.com/uc?id=1dQ3FPIm5Iy-nac0sCEB84bCuATwP08We
Загрузка данных...
ДАННЫЕ УСПЕШНО ЗАГРУЖЕНЫ!

- Размер данных: (1000, 8)
- Колонки:`['ID', 'Name', 'Sequence', 'Molecular_Weight', 'Isoelectric_Point', 'Protein_Length', 'Amino_Acid_Composition', 'Hydrophobicity']`

Первые 10 строк:
| ID | Name | Sequence | Molecular_Weight | Isoelectric_Point | Protein_Length | Hydrophobicity |
|----|------|----------|------------------|-------------------|----------------|----------------|
| WP_369686368.1 | ATP-binding cass... | MLELNFTQTLGSHTLT... | 5756.5430 | 8.517644 | 56 | 0.339286 |
| WP_369686367.1 | aldehyde dehydro... | MQSRDNGKPLAEARGL... | 6617.5065 | 6.106918 | 62 | -0.146774 |
| WP_369686366.1 | hypothetical pro... | GGEYLEIIEAARDIRV... | 9303.2892 | 4.533444 | 81 | -0.406173 |
| WP_369686365.1 | hypothetical pro... | NAVVNQKRVPLAPNGD... | 6304.0708 | 9.989715 | 58 | -0.591379 |
| WP_369686364.1 | homocysteine S-m... | MAGYLPQWLDAGAKLI... | 3619.1997 | 7.810425 | 34 | 0.141176 |
| WP_369686363.1 | hypothetical pro... | NRLILSPMGVRDVFRA... | 9303.6417 | 8.358213 | 83 | -0.059036 |
| WP_369686362.1 | DUF1043 family p... | MTWEYALIGLVVGIII... | 5601.4576 | 6.140907 | 48 | -0.164583 |
| WP_369686361.1 | hypothetical pro... | EIIKELVLRRKLFFKD... | 9935.1238 | 5.608610 | 83 | -0.630120 |
| WP_369686360.1 | WYL domain-conta... | MQALLPCESPAALSIP... | 8771.2230 | 8.802336 | 81 | 0.319753 |
| WP_369686359.1 | fimbrial protein... | IIPFTCQTPDVIVPMG... | 9075.0983 | 6.224745 | 85 | -0.192941 |

```
✓ Molecular_Weight - теперь числа с точкой
✓ Isoelectric_Point - теперь числа с точкой
✓ Protein_Length - теперь целые числа
✓ Hydrophobicity - теперь числа с точкой
✓ ID - теперь строковый тип (убрали лишние пробелы)
✓ Name - теперь строковый тип (убрали лишние пробелы)
✓ Sequence - теперь строковый тип (убрали лишние пробелы)
✓ Amino_Acid_Composition - преобразован в словарь Python
```

Сохранили в CSV: белки_pseudomonas.csv
(можно открыть в Excel)

СКРИПТ ЗАВЕРШЁН

