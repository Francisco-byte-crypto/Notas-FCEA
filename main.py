from create_graphs import *
from create_pandas_dataframe import create_pandas_dataframe as cpd

def main(url):
    data = cpd(url)
    students_present_per_test(data)
    total_notes_boxplot(data)
    plus_50_histogram(data)
    O_to_100_histogram(data)
    passed_per_test(data, url)

url = input('Ingrese la url al pdf con las notas: ')
main(url)