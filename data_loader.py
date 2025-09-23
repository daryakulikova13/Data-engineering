import pandas as pd
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

try:
    print("Загрузка данных...")
    raw_data = pd.read_csv(file_url)
    
    print("ДАННЫЕ УСПЕШНО ЗАГРУЖЕНЫ!")
    print("=" * 50)
    
    print(f"Размер данных: {raw_data.shape}")
    print(f"Колонки: {list(raw_data.columns)}")
    print("\n Первые 10 строк:")
    print(raw_data.head(10))
    print("\n Переменная 'raw_data' доступна в Variable Explorer")
    
except Exception as e:
    print(f"ОШИБКА: {e}")
    print("\n Возможные решения:")
    print("1. Проверьте доступ к файлу в Google Drive")
    print("2. Убедитесь, что файл в формате CSV")
    print("3. Проверьте интернет-соединение")

print("=" * 50)
print("СКРИПТ ЗАВЕРШЁН")
print("=" * 50)