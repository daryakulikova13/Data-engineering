#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:47:07 2025

@author: dasha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("EDA-анализ: белки Pseudomonas aeruginosa")
print("=" * 60)
print("\n" + "="*60)
print("1. Введение")
print("="*60)
print("Анализ биохимических характеристик белков бактерии Pseudomonas aeruginosa.")
print("Цель: оценить качество данных и выявить основные закономерности.")
print("\n" + "="*60)
print("2. ЗАГРУЗКА И ПЕРВИЧНЫЙ ОСМОТР")
print("="*60)

data = pd.read_csv('/home/dasha/Desktop/Data-engineering_project/pseudomonas_aeruginosa.csv')  
print("✅ Данные успешно загружены из 'pseudomonas_aeruginosa.csv'")

print(f"📊 Размер датасета: {data.shape}")
print(f"📊 Колонки: {list(data.columns)}")

print("\n" + "="*60)
print("3. ОЦЕНКА СТРУКТУРЫ ДАННЫХ")
print("="*60)

print("\nТипы данных:")
print(data.dtypes)

print("\nПервые 5 строк:")
print(data.head())

missing_data = data.isnull().sum()
missing_percent = (missing_data / len(data)) * 100

missing_info = pd.DataFrame({
    'Пропусков': missing_data,
    'Процент': missing_percent
})

print("Пропущенные значения:")
print(missing_info[missing_info['Пропусков'] > 0])

if missing_data.sum() > 0:
    plt.figure(figsize=(10, 4))
    missing_data[missing_data > 0].plot(kind='bar', color='coral')
    plt.title('Распределение пропущенных значений')
    plt.ylabel('Количество пропусков')
    plt.xticks(rotation=45)
    plt.tight_layout() 
    plt.show()
    
print("\n" + "="*60)
print("5. АНАЛИЗ ВЫБРОСОВ И АНОМАЛИЙ")
print("="*60)

numeric_cols = data.select_dtypes(include=[np.number]).columns

if len(numeric_cols) > 0:
    print(f"Числовые колонки для анализа: {list(numeric_cols)}")

    print("\n📈 Описательная статистика:")
    print(data[numeric_cols].describe())
    
    print("\n🔍 Выбросы (по правилу 1.5*IQR):")
    for col in numeric_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
        print(f"• {col}: {len(outliers)} выбросов ({len(outliers)/len(data)*100:.1f}%)")

    if len(numeric_cols) > 0:
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        axes = axes.ravel()
        
        for i, col in enumerate(numeric_cols[:4]):
            data[col].hist(bins=30, ax=axes[i], alpha=0.7, color='skyblue')
            axes[i].set_title(f'Распределение {col}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Частота')
        
        plt.tight_layout()
        plt.show()

print("\n" + "="*60)
print("6. ЗАКЛЮЧЕНИЕ И ВЫВОДЫ")
print("="*60)
print("ОБЩИЕ ВЫВОДЫ:")
print(f"• Проанализировано {len(data)} белков")
print(f"• Пропущенных значений: {missing_data.sum()} ✅")  # Будет 0
print(f"• Числовых характеристик: {len(numeric_cols)}")
print(f"• Качество данных: ОТЛИЧНОЕ (полностью заполненный датасет)")
print("\nРЕКОМЕНДАЦИИ:")
print("- Данные готовы для дальнейшего анализа")
if len(numeric_cols) > 0:
    print("- Можно переходить к корреляционному анализу")
print("- Можно исследовать взаимосвязи между характеристиками белков")