import pandas as pd
import csv


class Test_Read():
    def test_read_csv(selfself):
        with open('userdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])


    def test_read_pandas(self):
       df=pd.read_csv('userdata.csv')
       print(df)


