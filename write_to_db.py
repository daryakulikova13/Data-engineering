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

db_user = user
db_password = password
db_url = host
db_port = port
db_root_base = "homeworks"

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
    pool_recycle=3600
)

session_homeworks = Session(bind=engine)

df = pd.read_parquet(r"/home/dasha/Desktop/Data-engineering_project/pseudomonas_aeruginosa.parquet")

new_column_names = {col: col.lower() for col in df.columns}
df.rename(columns=new_column_names, inplace=True)
print(df.info())

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