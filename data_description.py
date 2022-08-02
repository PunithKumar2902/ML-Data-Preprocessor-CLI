import pandas as pd

class Data_description:

    tasks=['\n1.Describe a specific column','2.Show properties of each column','3.Show the dataset']

    def __init__(self,data):
        self.data=data

    # The function that prints the database on the command line.
    def show_dataset(self):

        while(1):
            
            try:
                rows=int(input('\nEnter the number of rows(>0) (enter -1 to go back)'))

                if rows==-1:
                    break
                if rows<=0:
                    print("\nno of rows must be > 0 ...please try again")
                    continue
                print(self.data.head(rows))

            except ValueError:
                print("\na valid integer must be entered.....please try again")
                continue
            
            break
        return

    #function that prints all the columns
    def show_columns(self):
        
        print("\nColumns :-\n")
        for column in self.data.columns.values:
            print(column,end=" ")

    #function to describe any column
    def describe(self):
        while(1):

            
            print("\nTasks (Data Description) :")

            for task in self.tasks:
                print(task)

            while(1):
                
                try:
                    choice = int(input("\nSelect a Task (-1 to go back)."))
                except ValueError:
                    print("\na valid integer must be entered...please try again")
                    continue
                break

            if choice==-1:
                break
            elif choice==1:
                self.show_columns()

                while(1):
                    column=input('\n\nPlease select a column : ')

                    try:
                        print("\n***DESCRIPTION FOR SELECTED COLUMN***\n")
                        print(self.data[column].describe())
                    except KeyError:
                        print("\nThere is no column with the name....please try again")
                        continue
                    break
            elif choice == 2:
                print("\n")
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice==3:

                self.show_dataset()
            else:
                print("\nenter a value less than 4!!...please try again")

                
