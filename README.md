# Student Habits vs Academic Performance

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=for-the-badge)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

Исследовательский проект, посвящённый анализу влияния образа жизни, привычек и психологического состояния студентов на их академическую успеваемость. В рамках работы проведён полный цикл анализа данных: от разведочного анализа (EDA) и проверки статистических гипотез до поиска аномалий (парадоксальных студентов) и построения прогностической ML-модели.

**Главная цель:** выяснить, какая комбинация привычек гарантирует высокую оценку (80+ баллов) и при этом позволяет сохранить нормальный сон и ментальное здоровье.

## Структура проекта

```text
student-habits-vs-performance/
├── data/
│   └── student_habits_performance.csv
├── src/
│   ├── __init__.py
│   ├── constants.py  
│   └── utils.py  
├── 01_preparation.ipynb    
├── 02_analysis/            
│   ├── 02_01_threshold_analysis.ipynb
│   ├── 02_02_hidden_factors.ipynb
│   ├── 02_03_conditional_probabilities.ipynb
│   ├── 02_04_diet_and_exercise_profiles.ipynb
│   ├── 02_05_study_hours_saturation.ipynb
│   ├── 02_06_paradoxical_students.ipynb
│   ├── 02_07_missing_values_analysis.ipynb
│   └── 02_08_predictive_model.ipynb
├── .gitignore
├── README.md
└── requirements.txt
```

## Стек технологий

| Инструмент | Назначение |
|---|---|
| Pandas | Обработка данных, группировка, агрегация, оконные функции |
| Matplotlib / Seaborn | Визуализация данных, графики |
| Scikit-learn | ML-модель (Decision Tree Classifier), анализ Feature Importance |

## Запуск проекта

1. Клонирование репозитория:

```bash
git clone git@github.com:progen1tor/student-habits-vs-performance.git
cd student-habits-vs-performance
```

2. Создание виртуального окружения и установка зависимостей:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Запуск Jupyter Notebook:

```bash
jupyter notebook
```

Откройте `01_preparation.ipynb` для начала работы, затем переходите к ноутбукам в папке `02_analysis`.

> **NB!** Для корректного отображения графиков убедитесь, что установлен шрифт Arial. В проекте используется кастомная стилизация графиков (цвета, размеры шрифтов), которая хранится в src/constants.py.

## Контакты

- Telegram: [@ob1101](https://t.me/ob1101)
