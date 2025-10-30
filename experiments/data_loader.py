import pandas as pd
import ast

pd.set_option('display.max_columns', None)  
pd.set_option('display.width', 1000)        
pd.set_option('display.max_colwidth', 20)  
print("=" * 50)
print("ЗАПУСК СКРИПТА В SPYDER")
print("=" * 50)
FILE_ID = "1dQ3FPIm5Iy-nac0sCEB84bCuATwP08We"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"
print(f"Загружаем данные по ссылке:")
print(f"   {file_url}")
print("Типы данных ДО изменений:")

try:
    print("Загрузка данных...")
    raw_data = pd.read_csv(file_url)
    
    print("ДАННЫЕ УСПЕШНО ЗАГРУЖЕНЫ!")
    print("=" * 50)
    
    print(f"Размер данных: {raw_data.shape}")
    print(f"Колонки: {list(raw_data.columns)}")
    print("\nПервые 10 строк:")
    print(raw_data.head(10))
    print("\nПеременная 'raw_data' доступна в Variable Explorer")

    # Переименовываем для удобства
    data = raw_data.copy()
    
    print("Типы данных ДО изменений:")
    print(data.dtypes)
    
    # Меняем типы на правильные
    # 1. Числовые столбцы
    if 'Molecular_Weight' in data.columns:
        data['Molecular_Weight'] = pd.to_numeric(
            data['Molecular_Weight'], errors='coerce'
        )
        print("✓ Molecular_Weight - теперь числа с точкой")
    
    if 'Isoelectric_Point' in data.columns:
        data['Isoelectric_Point'] = pd.to_numeric(
            data['Isoelectric_Point'], errors='coerce'
        )
        print("✓ Isoelectric_Point - теперь числа с точкой")
    
    if 'Protein_Length' in data.columns:
        data['Protein_Length'] = pd.to_numeric(
            data['Protein_Length'], errors='coerce'
        )
        # Пробуем сделать целыми числами, если получается
        try:
            data['Protein_Length'] = data['Protein_Length'].astype('Int64')
            print("✓ Protein_Length - теперь целые числа")
        except Exception:
            print("✓ Protein_Length - оставили как числа с точкой")
    
    if 'Hydrophobicity' in data.columns:
        data['Hydrophobicity'] = pd.to_numeric(
            data['Hydrophobicity'], errors='coerce'
        )
        print("✓ Hydrophobicity - теперь числа с точкой")
    # 2. Текстовые и специальные столбцы
    
    if 'ID' in data.columns:
        data['ID'] = data['ID'].astype(str).str.strip()
        print("✓ ID - теперь строковый тип (убрали лишние пробелы)")
    
    if 'Name' in data.columns:
        data['Name'] = data['Name'].astype(str).str.strip()
        print("✓ Name - теперь строковый тип (убрали лишние пробелы)")
    
    if 'Sequence' in data.columns:
        data['Sequence'] = data['Sequence'].astype(str).str.strip()
        print("✓ Sequence - теперь строковый тип (убрали лишние пробелы)")
    
    # 3. Сложный столбец - Amino_Acid_Composition (словарь)
    if 'Amino_Acid_Composition' in data.columns:
        try:
            # Пробуем преобразовать строку в словарь
            data['Amino_Acid_Composition'] = data['Amino_Acid_Composition'].apply(
                lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('{') else x
            )
            print("✓ Amino_Acid_Composition - преобразован в словарь Python")
        except Exception as e:
            print(f"⚠ Amino_Acid_Composition - не удалось преобразовать в словарь: {e}")
            print("  Оставили как есть")
    
    print("\nТипы данных ПОСЛЕ изменений:")
    print(data.dtypes)
    
    data.to_csv("белки_pseudomonas.csv", index=False)
    print("✓ Сохранили в CSV: белки_pseudomonas.csv")
    print("  (можно открыть в Excel)")
    
except Exception as e:
    print(f"ОШИБКА: {e}")
    print("\nВозможные решения:")
    print("1. Проверьте доступ к файлу в Google Drive")
    print("2. Убедитесь, что файл в формате CSV")
    print("3. Проверьте интернет-соединение")

print("=" * 50)
print("СКРИПТ ЗАВЕРШЁН")
print("=" * 50)
