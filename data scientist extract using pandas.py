# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WliCO9VElzfj3e0u909YJYPt-s8-EaHW

IMPORTING THE CSV FILE FROM GOOGLE DRIVE
"""

from google.colab import drive
drive.mount('/content/drive')

"""SETTING THE PATH TO ACCESS THE CSV FILE"""

import pandas
data = pandas.read_csv("/content/drive/MyDrive/Colab Notebooks/ds/ds_salaries.csv")

"""EXTRACTING NUMBER OF DATA SCIENTIST IN CALIFFORNIA, AND IN OTHER COUNTRIES"""

california = data[(data["job_title"]=="Data Scientist") & (data["company_location"]=="CA")].count()
print("california:"+ str(california["job_title"]))

US = data[(data["job_title"]=="Data Scientist") & (data["company_location"]=="US")].count()
print("United States:"+ str(US["job_title"]))

Spain = data[(data["job_title"]=="Data Scientist") & (data["company_location"]=="ES")].count()
print("Spain:"+ str(Spain["job_title"]))

India = data[(data["job_title"]=="Data Scientist") & (data["company_location"]=="IN")].count()
print("India:"+ str(India["job_title"]))

Nigeria = data[(data["job_title"]=="Data Scientist") & (data["company_location"]=="NG")].count()
print("Nigeria:"+ str(Nigeria["job_title"]))

"""MAXIMUM SALARY OF COUNTRIES FOR ALL ROLE"""

CA_max = data[data["company_location"]=="CA"]
print("california's max salary:"+str(CA_max["salary"].max())+ " USD")

US_max = data[data["company_location"]=="US"]
print("Unites states max salary:"+str(US_max["salary"].max())+" USD")

IN_max = data[data["company_location"]=="IN"]
print("india's max salary:"+str(IN_max["salary"].max())+" INR")

"""MINIMUM SALARY OF COUNTRIES FOR ALL ROLE"""

CA_min = data[data["company_location"]=="CA"]
print("california's min salary:"+str(CA_min["salary"].min())+ " USD")

US_min = data[data["company_location"]=="US"]
print("Unites states min salary:"+str(US_min["salary"].min())+" USD")

IN_min = data[data["company_location"]=="IN"]
print("india's min salary:"+str(IN_min["salary"].min())+" INR")

"""COUNT OF EACH LEVEL FOR A COUNTRIES"""

ca_entry_level = data[(data["experience_level"]=="EN") & (data["company_location"]=="CA")]
print("california's entry level cantitates count: "+str(ca_entry_level['experience_level'].count()))

ca_middle_level = data[(data["experience_level"]=="MI") & (data["company_location"]=="CA")]
print("california's middle level cantitates count: "+str(ca_middle_level['experience_level'].count()))

ca_senior_level = data[(data["experience_level"]=="SE") & (data["company_location"]=="CA")]
print("california's senior level cantitates count: "+str(ca_senior_level['experience_level'].count()))

ca_Executive_level = data[(data["experience_level"]=="EX") & (data["company_location"]=="CA")]
print("california's Executive level cantitates count: "+str(ca_Executive_level['experience_level'].count()))

"""MAXIMUM SALARY OF EACH LEVEL CANTITADES"""

entry_max=data[(data["experience_level"]=="EN") & (data["job_title"]=="Data Engineer") & (data["company_location"]=="US") & (data["company_size"]=="M")]
print("Maximun salary of data engineer(Entry level) in United States Mid company:"+str(entry_max["salary"].max()))

middle_max=data[(data["experience_level"]=="MI") & (data["job_title"]=="Data Engineer") & (data["company_location"]=="US") & (data["company_size"]=="M")]
print("Maximun salary of data engineer(Middle level) in United States Mid company:"+str(middle_max["salary"].max()))

senior_max=data[(data["experience_level"]=="SE") & (data["job_title"]=="Data Engineer") & (data["company_location"]=="US") & (data["company_size"]=="M")]
print("Maximun salary of data engineer(Senior level) in United States Mid company:"+str(senior_max["salary"].max()))

executive_max=data[(data["experience_level"]=="EX") & (data["job_title"]=="Data Engineer") & (data["company_location"]=="US") & (data["company_size"]=="M")]
print("Maximun salary of data engineer(Executive level) in United States Mid company:"+str(executive_max["salary"].max()))

"""MACHINE LEARNING ENGINEERING COUNT IN EACH YEAR"""

year_2020 = data[(data["work_year"]==2020) & (data["job_title"]=="Machine Learning Engineer")]
print("Machine Learning Engineer count in 2020:"+str(year_2020["work_year"].count()))

year_2021 = data[(data["work_year"]==2021) & (data["job_title"]=="Machine Learning Engineer")]
print("Machine Learning Engineer count in 2021:"+str(year_2021["work_year"].count()))

year_2022 = data[(data["work_year"]==2022) & (data["job_title"]=="Machine Learning Engineer")]
print("Machine Learning Engineer count in 2022:"+str(year_2022["work_year"].count()))

year_2023 = data[(data["work_year"]==2023) & (data["job_title"]=="Machine Learning Engineer")]
print("Machine Learning Engineer count in 2023:"+str(year_2023["work_year"].count()))

"""EACH YEAR'S TOTAL SALARY OF EVERY FIELD"""

YEAR_2020_total  = data[data["work_year"]==2020]
YEAR_2020_total = YEAR_2020_total["salary"]
print("Every field's total salary in 2020: "+str(YEAR_2020_total.sum()))

YEAR_2021_total  = data[data["work_year"]==2021]
YEAR_2021_total = YEAR_2021_total["salary"]
print("Every field's total salary in 2021: "+str(YEAR_2021_total.sum()))

YEAR_2022_total  = data[data["work_year"]==2022]
YEAR_2022_total = YEAR_2022_total["salary"]
print("Every field's total salary in 2022: "+str(YEAR_2022_total.sum()))

YEAR_2023_total  = data[data["work_year"]==2023]
YEAR_2023_total = YEAR_2023_total["salary"]
print("Every field's total salary in 2023: "+str(YEAR_2023_total.sum()))