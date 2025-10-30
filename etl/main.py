#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:49:19 2025

@author: dasha
"""

import argparse
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname('/home/dasha/my_data_project/etl/')
sys.path.append(parent_dir)

from extract import extract_from_google_drive, validate_raw_data, save_raw_data
from transform import transform_data, split_protein_name
from load import load_to_database, load_to_parquet, validate_output_data

def main():
    parser = argparse.ArgumentParser(description='ETL Pipeline для данных о белках Pseudomonas aeruginosa')
    parser.add_argument('--file-id', '-id', required=True, 
                       help='ID файла в Google Drive')
    parser.add_argument('--table-name', '-t', default='kulikova', 
                       help='Имя таблицы в БД')
    parser.add_argument('--max-rows', '-m', type=int, default=100, 
                       help='Максимальное количество строк для загрузки в БД')
    
    args = parser.parse_args()
    
    try:
        print("\n1. EXTRACT - извлечение данных")
        raw_df = extract_from_google_drive(args.file_id)
        validate_raw_data(raw_df)
        save_raw_data(raw_df)
 
        print("\n2. TRANSFORM - преобразование данных")
        transformed_df = transform_data(raw_df)
        final_df = split_protein_name(transformed_df)

        print("\n3. LOAD - загрузка данных")
        validate_output_data(final_df)
        load_to_database(final_df, args.table_name, args.max_rows)
        load_to_parquet(final_df)
        
    except Exception as e:
        print(f"\nОшибка: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())