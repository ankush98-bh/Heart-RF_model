import numpy as np
import json
import pickle
import config
class heart_prediction():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slop,ca,thal):
        self.age= age
        self.sex= sex
        self.cp=cp
        self.trestbps= trestbps
        self.chol= chol
        self.fbs=fbs
        self.restecg= restecg
        self.thalach=thalach
        self.exang= exang
        self.oldpeak= oldpeak
        self.slop= slop
        self.ca= ca
        self.thal= thal

    def load_model(self):
        with open (config.file_path,'rb') as f:
            self.model=pickle.load(f)
        
        with open (config.project_data,'r') as f:
            self.data=json.load(f)
        
    def heart_result(self):
        self.load_model()

        test_array= np.zeros(len(self.data['columns']))
        print(test_array)

        test_array[0]=self.age
        test_array[1]= self.sex
        test_array[2]=self.ca
        test_array[3]= self.trestbps
        test_array[1]=self.chol
        test_array[5]=self.fbs
        test_array[6]= self.restecg
        test_array[7]=self.thalach
        test_array[8]= self.exang
        test_array[9]=self.oldpeak
        test_array[10]=self.slop
        test_array[11]=self.ca
        test_array[12]=self.thal
        print(test_array)
        
        result= self.model.predict([test_array])[0]
        return result
        