import numpy as np 
import config
import os 
import json
import pickle

class DiabetesPrediction():
    def __init__(self,user_data):
        self.user_data = user_data
        self.model_path= config.MODEL_PATH
        self.project_path= config.PROJECT_PATH


    def load_data(self):
        
        with open(self.model_path,'rb') as f:
            self.model = pickle.load(f)


        with open(self.project_path,'r') as f:
            self.project_data = json.load(f)

    def prediction_model(self):

        self.load_data()

        Glucose = eval(self.user_data['Glucose'])
        BloodPressure = eval(self.user_data['BloodPressure'])
        SkinThickness = eval(self.user_data['SkinThickness'])
        Insulin = eval(self.user_data['Insulin'])
        BMI = eval(self.user_data['BMI'])
        DiabetesPedigreeFunction = eval(self.user_data['DiabetesPedigreeFunction'])
        Age = eval(self.user_data['Age'])

        test_array = np.zeros(len(self.project_data["columns"]))

        test_array[0]=Glucose
        test_array[1]=BloodPressure
        test_array[2]=SkinThickness
        test_array[3]=Insulin
        test_array[4]=BMI
        test_array[5]=DiabetesPedigreeFunction 
        test_array[6]=Age
        result = self.model.predict_proba([test_array])[0]
        threshold = 0.5
        prob = result[1]
        if prob >= threshold:
                pred_class= "Person with Diabetes! Take Care Your Self "
        else:
                pred_class= "Person with No Diabetes "
        print("Predicted Class is :",pred_class)
        return pred_class

if __name__ == "__main__":
    obj = DiabetesPrediction()
    obj






    

    