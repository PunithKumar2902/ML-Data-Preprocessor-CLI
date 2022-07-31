from os import path
import sys
import pandas as pd

class Data_input:

    # all extensions supported by this project.
    accepted_extensions=['.csv']
    
    # function to convert all the column names of any specific dataset into lowercase.
    def to_lower_case(self,data):

        for column in data.columns.values:

            data.replace({column : column.lower()},inplace = True)

        return data

    # function that takes any dataset from the input file and convert it into DataFrame.
    def inputfunction(self):
        
        try:
            
            filename,extension= path.splitext(sys.argv[1])

            if filename=="":
                raise SystemExit("provide the DATASET name (with extension).")
            
            if extension not in self.accepted_extensions:
                raise SystemExit("This file extension is not supported.")

        except IndexError:
            raise SystemExit("provide the DATASET name (with extension).")

        try:
            data = pd.read_csv(filename+extension)

        except FileNotFoundError:
            raise SystemExit("File doesn't exist")

        data = self.to_lower_case(data)

        return data
