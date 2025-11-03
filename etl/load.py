#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:27:24 2025

@author: dasha
"""

from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import Session
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

def create_db_engine():
    db_user = os.getenv('DB_USER') 
    db_password = os.getenv('DB_PASSWORD')
    db_url = os.getenv('DB_URL')
    db_port = os.getenv('DB_PORT')
    db_root_base = os.getenv('DB_NAME', 'homeworks')
    
    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
        pool_recycle=3600
    )
    
    return engine

def load_to_database(df: pd.DataFrame, table_name: str = "kulikova", max_rows: int = 100):
    try:
        new_column_names = {col: col.lower() for col in df.columns}
        df.rename(columns=new_column_names, inplace=True)
        engine = create_db_engine()
        
        df = df.head(100)
        df.to_sql(
            name=table_name,
            con=engine,
            schema="public", 
            if_exists="replace",
            index=False,
        )
        
        print(f"Успешно загружено {len(df)} строк в таблицу {table_name}")
        
    except Exception as e:
        print(f"Ошибка загрузки в БД: {e}")
        raise

def load_to_parquet(df: pd.DataFrame, filename: str = "processed_proteins.parquet"):
    os.makedirs('/processed/', exist_ok=True)
    file_path = f'/processed/{filename}'
    df.to_parquet(file_path, index=False)
    print(f"Данные сохранены в Parquet: {file_path}")

def validate_output_data(df: pd.DataFrame) -> bool:
    if df.empty:
        print("Ошибка: Выходной DataFrame пустой")
        return False
    
    print("Валидация выходных данных пройдена")
    return True
