# Проект реализуется в рамках дисциплины "Инжиниринг управления данными (базовый уровень)"
Проект посвящён анализу белков, входяющих в геном микроорганизма *Pseudomonas aeruginosa*
<img width="4107" height="1928" alt="image" src="https://github.com/user-attachments/assets/cbbe11c0-4ac5-4032-8706-57dbed6e2592" />
*Pseudomonas aeruginosa* -условно-патогенная бактерия, обладающая значительным клиническим и научным потенциалом. Это грамотрицательная палочка, широко распространенная в окружающей среде, которая отличается исключительной способностью к выживанию в различных, в том числе малоблагоприятных, условиях. Её природная устойчивость к многим антибиотикам и дезинфицирующим средствам обусловлена низкой проницаемостью её внешней мембраны и наличием эффективных систем активного вывода токсинов. В клинической практике P. aeruginosa представляет серьезнейшую угрозу, особенно для пациентов с ослабленным иммунитетом. Она является частым возбудителем нозокомиальных (внутрибольничных) инфекций, вызывая такие заболевания, как пневмония (у пациентов на ИВЛ), инфекции кровотока, ожоговых ран, а также хронические инфекции дыхательных путей у больных муковисцидозом, где образование биопленок делает ее практически неуязвимой для терапии.

Именно сложность лечения инфекций, вызванных этой бактерией, и определяет огромную значимость изучения её протеома — полного набора белков. Протеомные данные позволяют расшифровать молекулярные механизмы патогенности и устойчивости. Анализируя белки, мы можем идентифицировать конкретные факторы вирулентности (например, экзотоксин А, протеазы, система секреции III типа), понять механизмы формирования биопленки и изучить работу насосов, выводящих антибиотики. Кроме того, протеомика является ключом к разработке новых методов диагностики и лечения: она позволяет обнаруживать белки-маркеры для быстрой идентификации штаммов, определять мишени для новых лекарств и вакцин, а также понимать, как бактерия адаптирует свой белковый профиль в ответ на действие антимикробных препаратов, что открывает пути к преодолению резистентности. Таким образом, глубокое изучение протеома Pseudomonas aeruginosa является не просто академическим интересом, а насущной необходимостью для разработки эффективных стратегий борьбы с этим опасным патогеном.


# Ссылка на датасет
Ссылка на датасет на Google Диске:[Открыть датасет](https://drive.google.com/drive/folders/17_n1YnmEWkbr0EwFk1wTnYzYauQCbaod?hl=ru)

# Структура проекта
1. Датасет, содержащий 8 столбцов и 1000 строк (формат .csv);
- Размер данных: (1000, 8)
- Колонки:`['ID', 'Name', 'Sequence', 'Molecular_Weight', 'Isoelectric_Point', 'Protein_Length', 'Amino_Acid_Composition', 'Hydrophobicity']`

2. Скрипт, позволяющий выгружать датасет из Google Drive и выводить первые десять строк данных (`data_loader.py`) [Результат выполнения скрипта](screenshot.jpg);
Первые 10 строк:
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>Sequence</th>
      <th>Molecular_Weight</th>
      <th>Isoelectric_Point</th>
      <th>Protein_Length</th>
      <th>Hydrophobicity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WP_369686368.1</td>
      <td>ATP-binding cass...</td>
      <td>MLELNFTQTLGSHTLT...</td>
      <td>5756.5430</td>
      <td>8.517644</td>
      <td>56</td>
      <td>0.339286</td>
    </tr>
    <tr>
      <td>WP_369686367.1</td>
      <td>aldehyde dehydro...</td>
      <td>MQSRDNGKPLAEARGL...</td>
      <td>6617.5065</td>
      <td>6.106918</td>
      <td>62</td>
      <td>-0.146774</td>
    </tr>
    <tr>
      <td>WP_369686366.1</td>
      <td>hypothetical pro...</td>
      <td>GGEYLEIIEAARDIRV...</td>
      <td>9303.2892</td>
      <td>4.533444</td>
      <td>81</td>
      <td>-0.406173</td>
    </tr>
    <tr>
      <td>WP_369686365.1</td>
      <td>hypothetical pro...</td>
      <td>NAVVNQKRVPLAPNGD...</td>
      <td>6304.0708</td>
      <td>9.989715</td>
      <td>58</td>
      <td>-0.591379</td>
    </tr>
    <tr>
      <td>WP_369686364.1</td>
      <td>homocysteine S-m...</td>
      <td>MAGYLPQWLDAGAKLI...</td>
      <td>3619.1997</td>
      <td>7.810425</td>
      <td>34</td>
      <td>0.141176</td>
    </tr>
    <tr>
      <td>WP_369686363.1</td>
      <td>hypothetical pro...</td>
      <td>NRLILSPMGVRDVFRA...</td>
      <td>9303.6417</td>
      <td>8.358213</td>
      <td>83</td>
      <td>-0.059036</td>
    </tr>
    <tr>
      <td>WP_369686362.1</td>
      <td>DUF1043 family p...</td>
      <td>MTWEYALIGLVVGIII...</td>
      <td>5601.4576</td>
      <td>6.140907</td>
      <td>48</td>
      <td>-0.164583</td>
    </tr>
    <tr>
      <td>WP_369686361.1</td>
      <td>hypothetical pro...</td>
      <td>EIIKELVLRRKLFFKD...</td>
      <td>9935.1238</td>
      <td>5.608610</td>
      <td>83</td>
      <td>-0.630120</td>
    </tr>
    <tr>
      <td>WP_369686360.1</td>
      <td>WYL domain-conta...</td>
      <td>MQALLPCESPAALSIP...</td>
      <td>8771.2230</td>
      <td>8.802336</td>
      <td>81</td>
      <td>0.319753</td>
    </tr>
    <tr>
      <td>WP_369686359.1</td>
      <td>fimbrial protein...</td>
      <td>IIPFTCQTPDVIVPMG...</td>
      <td>9075.0983</td>
      <td>6.224745</td>
      <td>85</td>
      <td>-0.192941</td>
    </tr>
  </tbody>
</table>

3. Выполнено приведение типов переменных;
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

4. EDA-отчёт в виде Jypiter Notebook, где проведена базовая статистическая обработка данных, а также частота распределения признаков и корреляционный анализ;
Рендер на Jypiter Notebook - [![View on nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.org/github/daryakulikova13/Data-engineering/blob/main/notebooks/Seaborn_EDA.ipynb)



