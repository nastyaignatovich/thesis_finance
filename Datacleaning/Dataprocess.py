import numpy as np
import pandas as pd
import openpyxl as xl
import pickle

data= pd.read_csv('survey_answers.csv')


drops = ['Отметка времени','Баллы','Адрес электронной почты']

data = data.drop(drops, axis=1)

data = data.drop(31, axis=0)

gender_map = {'Male' : 0, 'Female' : 1}
print(data.columns)
data['2. What is your gender? '] = data['2. What is your gender? '].replace(gender_map)

data

marital_status_map = {'Have a patner' : 0, 'Single' : 1, 'Have a partner' : 0}

data['3. What is your marital status?'] = data['3. What is your marital status?'].replace(marital_status_map)

data

level_of_education_map={'High school diploma': 0,'Bachelor’s degree': 1, 'Master’s degree and higher' : 2}
data ['4. What is your highest level of education?'] = data['4. What is your highest level of education?'].replace(level_of_education_map)

data

ocupation_map = {'Yes' : 0, 'No' : 1}

data['5. Is your current occupation related to STEM fields?'] = data['5. Is your current occupation related to STEM fields?'].replace(ocupation_map)

data

finance_map = {'Yes' : 0, 'No' : 1}

data['6. Is your current occupation related to economics and/or finance?'] = data['6. Is your current occupation related to economics and/or finance?'].replace(finance_map)

data

income_map={'Below 15 000': 0,'Between 15 000 and 40 000': 1,'Between 25 000 and 40 000': 1, 'Between 40 000 and 60 000' : 2, 'More than 60 000' : 3}
data ['8. What is your annual income in EUR after taxes? '] = data['8. What is your annual income in EUR after taxes? '].replace(income_map)


horizon_map={'Less than 1 year': 0,'1–5 years': 1, '5–10 years' : 2, 'More than 10 years' : 3}
data ['13. What is your typical investment horizon?'] = data['13. What is your typical investment horizon?'].replace(horizon_map)
data = data.drop([88,89], axis=0)

with open("../Regression/data.pkl", "wb") as f:
    pickle.dump(data, f)

data.to_excel('survey_answers.xlsx')