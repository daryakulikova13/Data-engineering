#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:52:20 2025

@author: dasha
"""

from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import Session
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DB_USER') 
db_password = os.getenv('DB_PASSWORD')
db_url = os.getenv('DB_URL')
db_port = os.getenv('DB_PORT')
db_root_base = os.getenv('DB_NAME', 'homeworks')

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
    pool_recycle=3600
)

session_homeworks = Session(bind=engine)

df = pd.read_parquet(r"/home/dasha/Desktop/Data-engineering_project/pseudomonas_aeruginosa.parquet")

new_column_names = {col: col.lower() for col in df.columns}
df.rename(columns=new_column_names, inplace=True)
print(df.info())

def split_name(full_name):
    if pd.isna(full_name):
        return None, None
    if ' [' in full_name and full_name.endswith(']'):
        parts = full_name.rsplit(' [', 1)
        protein_name = parts[0].strip()
        organism = parts[1].rstrip(']').strip()
        return protein_name, organism
    return full_name, "Unknown"

df[['protein_name', 'organism']] = df['name'].apply(lambda x: pd.Series(split_name(x)))

numeric_cols = [
    "id", "name", "sequence", "molecular_weight", "isoelectric_point",
    "protein_length", "amino_acid_composition", "hydrophobicity"
]

df = df.head(100)
df.to_sql(
    name="kulikova",
    con=engine,
    schema="public",
    if_exists="replace",
    index=False,
 )