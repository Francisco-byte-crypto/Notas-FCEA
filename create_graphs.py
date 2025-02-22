import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from create_pandas_dataframe import create_pandas_dataframe as cpd
from url_to_headers import url_to_headers as uth

class Plot:
    def __init__(self, title, xlabel, ylabel):
        self.fig, self.ax = plt.subplots(figsize=(12.8, 7.2), layout='constrained')
        self.ax.set_title(title)
        self.ax.set_ylabel(ylabel)    
        self.ax.set_xlabel(xlabel)
        self.ax.grid(visible=True)

def students_present_per_test(data):

    summary = data.describe()
    column_names = []
    column_values = []

    for column in data.columns:
        if(column == "CÉDULA" or column == "NOMBRE" or column == "TOTAL" or column == "NOTA"): pass
        else: column_names.append(column)

    for colum_name in column_names:
        column_values.append(summary[colum_name]['count'])

    if(len(column_names)==0): raise Exception("No se encontraron revisiones para este parcial o el esquema de revisiones no sigue el formato tradicional.")
    if(len(column_values)==0): raise Exception("La lista de valores está vacía.")

    plot = Plot('Estudiantes presentes en cada prueba.', 'Pruebas', 'Personas presentes')
    plot.ax.bar(column_names, column_values)
    plot.fig.savefig("charts/Barchart - Estudiantes presentes en cada prueba.png")

def total_notes_boxplot(data):
    plot = Plot('Diagrama de caja de notas totales.png', '', 'Notas')
    plot.ax = data['TOTAL'].plot.box()
    yticks = [i for i in range(0, int(data['TOTAL'].max()) + 5, 5)]
    plot.ax.set_yticks(yticks, labels=yticks)
    plot.fig.savefig("charts/Boxplot - Diagrama de caja de notas totales.png")

def plus_50_histogram(data):
    data = data[data['TOTAL'] >= 50]

    plot = Plot('Alumnos por nota total superiores a 50', 'Notas', 'Alumnos')
    plot.ax.hist(x = data['TOTAL'], histtype='bar', bins=[50,60,70,80,90,100])
    plot.ax.set_xticks([50,60,70,80,90,100])
    plot.fig.savefig("charts/Histograma - Alumnos por nota total superiores a 50")

def O_to_100_histogram(data):
    plot = Plot('Alumnos por nota total', 'Notas', 'Alumnos')
    plot.ax.hist(x = data['TOTAL'], histtype='bar', bins=[0,10,20,30,40,50,60,70,80,90,100])
    plot.ax.set_xticks([10,20,30,40,50,60,70,80,90,100])
    plot.fig.savefig("charts/Histograma - Alumnos por nota total.")

def passed_per_test(data, url):
    summary =  data.describe()
    headers = uth(url)
    column_names = []
    students_passed = []
    students_passed_totals = []
    total_students = summary['TOTAL']['count']

    for column in data.columns:
        if(column == "CÉDULA" or column == "NOMBRE" or column == "NOTA"): pass
        else: column_names.append(column)

    # We are going to add 3 to the index as the headers lists have this schema: [MAX, NONE, NONE, NUM, NUM, NUM, ...]
    for i in range(0, len(column_names)):
        def set_students_passed(x, i):
            minimum = headers['MINIMO'][i+3]
            if(x >= minimum): return x
            else: return np.nan
        test_column = column_names[i]
        data[test_column] = data[test_column].apply(set_students_passed, i=i)
        students_passed.append(data[test_column].count())
    
    for i in range(len(students_passed)):
        passed_totals = students_passed[i] / total_students
        students_passed_totals.append(passed_totals)

    plot = Plot('Alumnos aprobados sobre el total de presentados por prueba', '', '')
    plot.ax.bar(column_names, students_passed_totals)
    plot.ax.set_yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plot.fig.savefig("charts/Barchart - Alumnos aprobados sobre el total de presentados por prueba.")
