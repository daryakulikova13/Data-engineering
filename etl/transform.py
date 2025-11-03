#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:10:01 2025

@author: dasha
"""

import pandas as pd
import ast
import os

def transform_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    data = raw_df.copy()
    
    print("Типы данных ДО изменений:")
    print(data.dtypes)
    numeric_columns = {
        'Molecular_Weight': 'float64',
        'Isoelectric_Point': 'float64', 
        'Protein_Length': 'Int64',
        'Hydrophobicity': 'float64'
    }
    
    for col, dtype in numeric_columns.items():
        if col in data.columns:
            if dtype == 'Int64':
                data[col] = pd.to_numeric(data[col], errors='coerce')
                try:
                    data[col] = data[col].astype('Int64')
                    print(f"{col} - теперь целые числа")
                except Exception:
                    print(f"{col} - оставили как числа с точкой")
            else:
                data[col] = pd.to_numeric(data[col], errors='coerce')
                print(f"{col} - теперь числа с точкой")

    string_columns = ['ID', 'Name', 'Sequence']
    for col in string_columns:
        if col in data.columns:
            data[col] = data[col].astype(str).str.strip()
            print(f"{col} - теперь строковый тип")

    if 'Amino_Acid_Composition' in data.columns:
        data = process_amino_acid_composition(data)

    print(data.dtypes)
    
    return data

def process_amino_acid_composition(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    try:
        data['Amino_Acid_Composition'] = data['Amino_Acid_Composition'].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('{') else x
        )
        print("Amino_Acid_Composition - преобразован в словарь Python")
    except Exception as e:
        print(f"Amino_Acid_Composition - не удалось преобразовать в словарь: {e}")
        print("Оставили как есть")
    
    return data

def split_protein_name(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    
    def split_name(full_name):
        if pd.isna(full_name):
            return None, None
        if ' [' in full_name and full_name.endswith(']'):
            parts = full_name.rsplit(' [', 1)
            protein_name = parts[0].strip()
            organism = parts[1].rstrip(']').strip()
            return protein_name, organism
        return full_name, "Unknown"
    
    data[['Protein_Name', 'Organism']] = data['Name'].apply(
        lambda x: pd.Series(split_name(x))
    )
    
    print("Колонка Name разделена на protein_name и organism")
    return data

def test_with_real_data():
    try:
        raw_file_path = "/raw/raw_proteins.csv"
        
        if os.path.exists(raw_file_path):
            print("\n1. Загрузка сырых данных из CSV")
            raw_df = pd.read_csv(raw_file_path)
            print(f"Загружено {len(raw_df)} строк")
            
            print("\n2. Трансформация данных")
            transformed_df = transform_data(raw_df)
            
            print("\n3. Разделение имен")
            final_df = split_protein_name(transformed_df)
            
            print("\nТрансформация завершена успешно!")
            print(f"Итоговый размер: {final_df.shape}")
            print(f"Новые колонки: {[col for col in final_df.columns if col not in raw_df.columns]}")
            
        else:
            print(f"Файл {raw_file_path} не найден")
            
    except Exception as e:
        print(f" Ошибка: {e}")

if __name__ == "__main__":
     test_with_real_data()
    
