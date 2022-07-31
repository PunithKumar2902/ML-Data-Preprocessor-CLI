from data_description import Data_description
from input_data import Data_input
from data_imputation import Data_imputation
from download_data import Download
from encoding import Categorical
from feature_scaling import FeatureScaling

class Preprocessor:

    # The Task associated with this class. This is also the main class of the project.
    tasks = [
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]

    data = 0
    
    def __init__(self):
        self.data = Data_input().inputfunction()
        print("\n\n WELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\n\n")

    # function to remove the target column of the DataFrame.
    def removeTargetColumn(self):
        print("Columns\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        
        while(1):
            column = input("\nWhich is the target variable:(Press -1 to exit)  ")
            if column == "-1":
                exit()
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    print(column)
                    self.data.drop(column, axis = 1, inplace = True)
                except KeyError:
                    print("No column present with this name. Try again......")
                    continue
                print("Done.......")
                break
            else:
                print("Try again with the correct column name...")
        return
    
    def printData(self):
        print(self.data)

    # main function of the Preprocessor class.
    def preprocessorMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nTasks (Preprocessing)\n")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? (Press -1 to exit):  "))
                except ValueError:
                    print("Integer Value required. Try again.....")
                    continue
                break

            if choice == -1:
                exit()

            # moves the control into the DataDescription class.
            elif choice==1:
                Data_description(self.data).describe()


            # moves the control into the Imputation class.
            elif choice==2:
                self.data = Data_imputation(self.data).imputer()
                

            # moves the control into the Categorical class.
            elif choice==3:
                self.data = Categorical(self.data).categoricalMain()


            # moves the control into the FeatureScaling class.
            elif choice==4:
                self.data = FeatureScaling(self.data).scaling()


            # moves the control into the Download class.
            elif choice==5:
                Download(self.data).download()
            
            else:
                print("\nWrong Integer value!! Try again..")

# obj is the object of our Preprocessor class(main class).
obj = Preprocessor()
# the object 'obj' calls the main function of our Preprocessor class.
obj.preprocessorMain()
