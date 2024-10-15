#either we can pandas or csv module to read csv file
import pandas as pd
import csv

class Test_CRUD():
    def test_update_1(self):
        df=pd.read_csv(r"/src/userdata.csv")
        print(df)

    def test_update_2(self):
        with open (r"/src/userdata.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])
