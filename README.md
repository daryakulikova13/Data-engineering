# Data-engineering
Проект для загрузки датасетов из Google Drive с использованием Python и pandas.

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

## Результаты преобразования типов данных
### Типы данных ДО обработки:
ID                         object
Name                       object
Sequence                   object
Molecular_Weight          float64
Isoelectric_Point         float64
Protein_Length              int64
Amino_Acid_Composition     object
Hydrophobicity            float64
dtype: object

### Типы данных ПОСЛЕ обработки:
ID                         object
Name                       object
Sequence                   object
Molecular_Weight          float64
Isoelectric_Point         float64
Protein_Length              Int64
Amino_Acid_Composition     object
Hydrophobicity            float64
dtype: object

### Вывод скрипта:
==================================================
ЗАПУСК СКРИПТА В SPYDER
==================================================
Загружаем данные по ссылке:
   https://drive.google.com/uc?id=1dQ3FPIm5Iy-nac0sCEB84bCuATwP08We
Типы данных ДО изменений:
Загрузка данных...
ДАННЫЕ УСПЕШНО ЗАГРУЖЕНЫ!
==================================================
Размер данных: (1000, 8)
Колонки: ['ID', 'Name', 'Sequence', 'Molecular_Weight', 'Isoelectric_Point', 'Protein_Length', 'Amino_Acid_Composition', 'Hydrophobicity']

Первые 10 строк:
               ID                 Name             Sequence  Molecular_Weight  Isoelectric_Point  Protein_Length Amino_Acid_Composition  Hydrophobicity
0  WP_369686368.1  ATP-binding cass...  MLELNFTQTLGSHTLT...         5756.5430           8.517644              56  {'M': 1, 'L': 8,...          0.339286
1  WP_369686367.1  aldehyde dehydro...  MQSRDNGKPLAEARGL...         6617.5065           6.106918              62  {'M': 2, 'Q': 2,...         -0.146774
2  WP_369686366.1  hypothetical pro...  GGEYLEIIEAARDIRV...         9303.2892           4.533444              81  {'G': 4, 'E': 8,...         -0.406173
3  WP_369686365.1  hypothetical pro...  NAVVNQKRVPLAPNGD...         6304.0708           9.989715              58  {'N': 5, 'A': 5,...         -0.591379
4  WP_369686364.1  homocysteine S-m...  MAGYLPQWLDAGAKLI...         3619.1997           7.810425              34  {'M': 1, 'A': 5,...          0.141176
5  WP_369686363.1  hypothetical pro...  NRLILSPMGVRDVFRA...         9303.6417           8.358213              83  {'N': 4, 'R': 6,...         -0.059036
6  WP_369686362.1  DUF1043 family p...  MTWEYALIGLVVGIII...         5601.4576           6.140907              48  {'M': 2, 'T': 1,...         -0.164583
7  WP_369686361.1  hypothetical pro...  EIIKELVLRRKLFFKD...         9935.1238           5.608610              83  {'E': 10, 'I': 4...         -0.630120
8  WP_369686360.1  WYL domain-conta...  MQALLPCESPAALSIP...         8771.2230           8.802336              81  {'M': 4, 'Q': 1,...          0.319753
9  WP_369686359.1  fimbrial protein...  IIPFTCQTPDVIVPMG...         9075.0983           6.224745              85  {'I': 7, 'P': 8,...         -0.192941

✓ Molecular_Weight - теперь числа с точкой
✓ Isoelectric_Point - теперь числа с точкой
✓ Protein_Length - теперь целые числа
✓ Hydrophobicity - теперь числа с точкой
✓ ID - теперь строковый тип (убрали лишние пробелы)
✓ Name - теперь строковый тип (убрали лишние пробелы)
✓ Sequence - теперь строковый тип (убрали лишние пробелы)
✓ Amino_Acid_Composition - преобразован в словарь Python

✓ Сохранили в CSV: белки_pseudomonas.csv
  (можно открыть в Excel)
==================================================
СКРИПТ ЗАВЕРШЁН
==================================================
