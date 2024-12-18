import numpy as np
import pandas as pd
import openpyxl as xl
import pickle

# Load the dataset
data= pd.read_csv('survey_answers.csv')

# Drop unnecessary columns from the dataset
drops = ['Отметка времени','Баллы','Адрес электронной почты']

# Drop a specific row
data = data.drop(drops, axis=1)
data = data.drop(31, axis=0)

# Mapping gender responses to numerical values
gender_map = {'Male' : 0, 'Female' : 1}
print(data.columns)
data['2. What is your gender? '] = data['2. What is your gender? '].replace(gender_map)

# Display updated dataset
data

# Mapping marital status
marital_status_map = {'Have a patner' : 0, 'Single' : 1, 'Have a partner' : 0}
data['3. What is your marital status?'] = data['3. What is your marital status?'].replace(marital_status_map)

# Display updated dataset
data

# Mapping education levels to numerical values for simplicity
level_of_education_map={'High school diploma': 0,'Bachelor’s degree': 1, 'Master’s degree and higher' : 2}
data ['4. What is your highest level of education?'] = data['4. What is your highest level of education?'].replace(level_of_education_map)

# Display updated dataset
data

# Mapping occupation responses related to STEM fields
ocupation_map = {'Yes' : 0, 'No' : 1}
data['5. Is your current occupation related to STEM fields?'] = data['5. Is your current occupation related to STEM fields?'].replace(ocupation_map)

# Display updated dataset
data

# Mapping occupation responses related to economics/finance
finance_map = {'Yes' : 0, 'No' : 1}
data['6. Is your current occupation related to economics and/or finance?'] = data['6. Is your current occupation related to economics and/or finance?'].replace(finance_map)

# Display updated dataset
data

# Mapping income ranges to numerical categories for simplification
income_map={'Below 15 000': 0,'Between 15 000 and 40 000': 1,'Between 25 000 and 40 000': 1, 'Between 40 000 and 60 000' : 2, 'More than 60 000' : 3}
data ['8. What is your annual income in EUR after taxes? '] = data['8. What is your annual income in EUR after taxes? '].replace(income_map)

# Mapping investment horizons to numerical categories
horizon_map={'Less than 1 year': 0,'1–5 years': 1, '5–10 years' : 2, 'More than 10 years' : 3}
data ['13. What is your typical investment horizon?'] = data['13. What is your typical investment horizon?'].replace(horizon_map)

# Drop rows with indices 88 and 89 (assumed invalid or unnecessary)
data = data.drop([88,89], axis=0)

#Save the cleaned and transformed dataset into a binary file
with open("../Regression/data.pkl", "wb") as f:
    pickle.dump(data, f)

# Export the cleaned data to an Excel file
data.to_excel('survey_answers.xlsx')