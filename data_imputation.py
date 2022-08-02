import numpy as np
import pandas as pd
from data_description import Data_description

class Data_imputation:

    tasks = [
        "\n1. Show number of Null Values",
        "2. Remove Columns",
        "3. Fill Null Values (with mean)",
        "4. Fill Null Values (with median)",
        "5. Fill Null Values (with mode)",
        "6. Show the Dataset\n"
    ]

    def __init__(self,data):
        self.data=data

    #function that prints all the columns
    def show_columns(self):
        
        print("\nColumns: ")
        for column in self.data.columns.values:
            print(column,end=" ")

    def printNULLvalues(self):
        
        print("\nNULL values in the dataset are :-\n")
        print(self.data.isnull().sum())
        print(" ")

        return 

    def remove_column(self):
        self.show_columns()
        while(1):

            columns=input("\nEnter the columns you want to delete (press -1 to go back ) ")

            if(columns=="-1"):
                break

            choice=input("Are you sure(y/n)?  ")

            if choice.lower() =='y':

                try:
                    self.data.drop(columns.split(" "),axis=1,inplace=True)
                except KeyError:
                    print("!! One or more columns are not present..please try again")
                    continue
                print(".........Done.........")
                print("columns are deleted.\n")


    def impute_mean(self):
        
        self.show_columns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ")
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("\nColumn is not present. Try again.....\n")
                    continue
                except TypeError:
                    # Imputation is only possible on some specific datatypes like int, float etc.
                    print("The Imputation is not possible here. Try on another column.")
                    continue
                print("Done......\n")
                break
        return

    def impute_median(self):

        self.show_columns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ")
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("\nColumn is not present. Try again.....\n")
                    continue
                except TypeError:
                    # Imputation is only possible on some specific datatypes like int, float etc.
                    print("\nThe Imputation is not possible here. Try on another column.\n")
                    continue
                print("Done......\n")
                break
        return

    def impute_mode(self):

        self.show_columns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ")
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mode()[0])
                except KeyError:
                    print("\nColumn is not present. Try again.....\n")
                    continue
                except TypeError:
                    # Imputation is only possible on some specific datatypes like int, float etc.
                    print("The Imputation is not possible here. Try on another column.")
                    continue
                print("Done......\n")
                break
        return

    def data_imputer(self):

        while(1):
            print("\nImputation Tasks:")

            for task in self.tasks:
                print(task)

            while(1):
                
                try:
                    choice = int(input("\nEnter your choice(-1 to go back)"))
                except ValueError:
                    print("\na valid integer must be entered please try again....\n")
                    continue
                break
            if choice == -1:
                break

            elif choice==1:
                self.printNULLvalues()

            elif choice==2:
                self.remove_column()

            elif choice==3:
                self.impute_mean()
            elif choice==4:
                self.impute_median()
            elif choice == 5:
                self.impute_mode()
            elif choice==6:
                Data_description.show_dataset(self)

            else:
                print("\nplease enter a valid choice and try again......\n")

        return self.data
            
            
