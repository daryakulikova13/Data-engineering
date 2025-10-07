#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:17:03 2025

@author: dasha
"""
import pandas as pd
import requests
import json

def fetch_food_products():
    api_url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        'action': 'process',
        'json': 1,
        'page_size': 20,  
        'search_terms': 'biscuits',  
        'fields': 'product_name,brands,countries,quantity,nutrition_grades,ecoscore_grade'  
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        print("Данные успешно получены из Open Food Facts API!")
        print(f"Получено {len(data['products'])} продуктов")
        
        return data['products']
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

def create_food_dataframe(products):
    if not products:
        print("Нет данных для создания DataFrame")
        return None

    df = pd.DataFrame(products)
    
    print("DataFrame успешно создан!")
    print(f"Размер DataFrame: {df.shape}")
    
    return df


def clean_and_analyze_data(df):
    print("\nПроводим базовый анализ данных...")
    print(f"Всего строк: {df.shape[0]}, столбцов: {df.shape[1]}")
    print("\nСтолбцы в данных:")
    for i, column in enumerate(df.columns, 1):
        print(f"{i}. {column}")
    
    main_columns = ['product_name', 'brands', 'countries', 'quantity', 'nutrition_grades', 'ecoscore_grade']
    available_columns = [col for col in main_columns if col in df.columns]
    
    if available_columns:
        display_df = df[available_columns].head(10)
        print(f"\nПервые 10 продуктов (только основные поля):")
        print(display_df)
    else:
        print("\nПервые 5 строк всех данных:")
        print(df.head())
    
    print(f"\nСтатистика по отсутствующим данным:")
    missing_data = df.isnull().sum()
    for column, missing_count in missing_data.items():
        if missing_count > 0:
            print(f"   - {column}: {missing_count} пропущенных значений")

def main():
    print("Начинаем загрузку данных из Open Food Facts API...")
    print("Ищем информацию о печенье...")

    food_products = fetch_food_products()
    
    if food_products:
        df = create_food_dataframe(food_products)
        
        if df is not None:
            clean_and_analyze_data(df)

            df.to_csv('/home/dasha/Desktop/api_example/food_products_main.csv', index=False, encoding='utf-8')
            print(f"\nПолные данные сохранены в '/home/dasha/Desktop/api_example/food_products_main.csv'")

            main_columns = ['product_name', 'brands', 'countries', 'quantity', 'nutrition_grades', 'ecoscore_grade']
            available_columns = [col for col in main_columns if col in df.columns]
            
            if available_columns:
                df[available_columns].to_csv('/home/dasha/Desktop/api_example/food_products_main.csv', index=False, encoding='utf-8')
                print(f"Основные данные сохранены в '/home/dasha/Desktop/api_example/food_products_main.csv'")

if __name__ == "__main__":
    main()
    
    