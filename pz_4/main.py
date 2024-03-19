import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('train.csv')

class DataPipeline:
    def __init__(self, data):
        self.data = data

    def data_analysis(self):
        print("---------------------Analysis---------------------")
        print(self.data.head(27), "\n")
        print("------------------------------------------------")
        print(self.data.info(), "\n")
        print("------------------------------------------------")
        print(self.data.describe(), "\n")
        print("------------------------------------------------")
        print(self.data.isnull().sum(), "\n")
        print("------------------------------------------------")



    def data_visualize(self):
        # data_sort = self.data.sort_values(by=['Social_2', 'Rooms'])
        print("---------------------Visualize---------------------")
        # ---------------------------------------------------------
        # plt.hist(data_sort['Social_2'])
        # plt.title("gistogram Social_2")
        # plt.xlabel("Social_2")
        # plt.show()
        #
        # plt.scatter(data_sort['Rooms'], data_sort['Price'])
        # plt.title("Rooms and Price")
        # plt.show()
        #
        # plt.boxplot(data_sort['HouseFloor'])
        # plt.title("HouseFloor")
        # plt.show()
        # ---------------------------------------------------------
        plt.hist(self.data['Social_2'])
        plt.title("gistogram Social_2")
        plt.xlabel("Social_2")
        plt.show()

        plt.scatter(self.data['Rooms'], self.data['Price'])
        plt.title("Rooms and Price")
        plt.show()


        plt.boxplot(self.data['HouseFloor'])
        plt.title("HouseFloor")
        plt.show()

    def processing_passes(self):
        median = self.data['LifeSquare'].median()
        self.data['LifeSquare'] = self.data['LifeSquare'].fillna(median)
        median = self.data['Healthcare_1'].median()
        self.data['Healthcare_1'] = self.data['Healthcare_1'].fillna(median)
        return self.data

    def processing_emission(self):
        self.data.loc[data['HouseFloor'] == 0, 'HouseFloor'] = self.data.loc[data['HouseFloor'] == 0, 'Floor']
        return self.data



dt_1 = DataPipeline(data)
dt_1.data_analysis()
dt_1.processing_passes()
dt_1.processing_emission()
dt_1.data_analysis()
dt_1.data_visualize()




#-----------------------------------------------------------------------------------------------
# data['LifeSquare'] = data['LifeSquare'].fillna(data['Square'] * 0.6)
# data['Healthcare_1'] = data['Healthcare_1'].fillna((data['Ecology_1'] * data['Social_2']) * 2)
#-----------------------------------------------------------------------------------------------



