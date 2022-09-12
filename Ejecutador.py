import csv
from Graphics import CreateGraph, PrintGraph
import numpy as np
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'es_CO')


class Plot:
    pass


class ExpenseData:
    def __init__(self, category):
        self.Category = category
        self.ExpensesInformation = []

    def AddExpenseInformation(self, data):
        self.ExpensesInformation.append(data)

    def GetExpenseSum(self):
        sum = 0
        for expense in self.ExpensesInformation:
            sum += expense.Value
        return sum


class SpecificData:
    def __init__(self, tag, createdOn, value):
        self.Tag = tag
        self.CreatedOn = createdOn
        self.Value = value


###################################################

Data = []
AllValues = []

with open('BD.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            AllValues.append(int(row[3]))
            if(any(element.Category == row[0] for element in Data)):
                for element in Data:
                    if element.Category == row[0]:
                        element.AddExpenseInformation(
                            SpecificData(row[1], row[2], int(row[3])))
                        break
            else:
                newData = ExpenseData(row[0])
                newData.AddExpenseInformation(
                    SpecificData(row[1], row[2], int(row[3])))
                Data.append(newData)
            line_count += 1
    print(f'Processed {line_count} lines.')


graphs = []
for element in Data:
    print("****************")
    print(element.Category)
    tags = []
    creationDates = []
    values = []
    for sube in element.ExpensesInformation:
        tags.append(sube.Tag)
        creationDates.append(sube.CreatedOn)
        values.append(sube.Value)

    plot = Plot()
    plot.x = tags
    plot.y = values
    plot.label = element.Category
    graphs.append(plot)

    print("****************")
    print("Conteo" + "\t" + str((pd.Series(values).count())))
    print("Media" + "\t" + locale.currency(pd.Series(values).mean(), grouping=True))
    print("Varianza" + "\t" + locale.currency(pd.Series(values).var(), grouping=True))
    print("DesvEsta" + "\t" + locale.currency(pd.Series(values).std(), grouping=True))

    print("Minimo" + "\t" + locale.currency(pd.Series(values).min(), grouping=True))
    print("25%" + "\t" + locale.currency(pd.Series(values).quantile(0.25), grouping=True))
    print("50%" + "\t" + locale.currency(pd.Series(values).quantile(0.5), grouping=True))
    print("75%" + "\t" + locale.currency(pd.Series(values).quantile(0.75), grouping=True))
    print("Maximo" + "\t" + locale.currency(pd.Series(values).max(), grouping=True))
    print("****************")

labels = [o.Category for o in Data]
values = [o.GetExpenseSum() for o in Data]
PrintGraph("", labels, values)
CreateGraph(graphs)
