#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:53:31 2025

@author: dasha
"""

import pandas as pd
import os

def extract_from_google_drive(file_id: str = "1dQ3FPIm5Iy-nac0sCEB84bCuATwP08We") -> pd.DataFrame:
    file_url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Загружаем данные по ссылке: {file_url}")
    
    try:
        raw_data = pd.read_csv(file_url)
        print(f"Размер данных: {raw_data.shape}")
        print(f"Колонки: {list(raw_data.columns)}")
        
        return raw_data
        
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        raise

def validate_raw_data(df: pd.DataFrame) -> bool:
    if df.empty:
        print("Ошибка: DataFrame пустой")
        return False
    
    required_columns = ['ID', 'Name', 'Sequence', 'Molecular_Weight', 'Isoelectric_Point', 
                        'Protein_Length', 'Amino_Acid_Composition', 'Hydrophobicity']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Ошибка: Отсутствуют обязательные колонки: {missing_columns}")
        return False
    
    print("Валидация сырых данных пройдена")
    return True

def save_raw_data(df: pd.DataFrame, filename: str = "raw_proteins.csv"):
    os.makedirs('/raw/', exist_ok=True)
    file_path = f'/raw/{filename}'
    df.to_csv(file_path, index=False)
    print(f"Сырые данные сохранены в {file_path}")
    
if __name__ == "__main__":
    try:
        print("\n1. Загрузка данных")
        df = extract_from_google_drive()  
        print("\n2. Валидация данных")
        is_valid = validate_raw_data(df)
        
        if is_valid:
            print("\n3. Сохранение данных")
            save_raw_data(df)
            print("\n Все операции выполнены успешно")
        else:
            print("\n Валидация не пройдена")
            
    except Exception as e:
        print(f"\n Критическая ошибка: {e}")
