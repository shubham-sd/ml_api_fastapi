from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import pandas as pd
from mangum import Mangum

# loading the model
load_gnb = pickle.load(open('./gnb_model', 'rb'))
# load_lr = pickle.load(open('./original_lr_model.pkl', 'rb'))


# initializing app
app = FastAPI()
# handler = Mangum(app)

# defining user inputs and their datatypes
class RFMInput(BaseModel):
    Frequency: float
    Recency: float
    Monetary: float
    

# creating api endpoints
@app.post('/rfm_prediction')
def rfm_predict(input_param: RFMInput):
    # print(input_param)
    data = input_param.json()
    # print(data)
    input_dict = json.loads(data)

    frequency = input_dict['Frequency']
    recency = input_dict['Recency']
    monetary_value = input_dict['Monetary']

    input_list = [frequency, recency, monetary_value]

    prediction = load_gnb.predict([input_list])

    if prediction == 2:
        return "Your Customer is of level Gold (High)"
    elif prediction == 1:
        return "Your Customer is of level Silver (Medium)"
    else:
        return "Your Customer is of level Bronze (Low)"

# class for car price prediction inputs
class CarPricePrediction(BaseModel):
    Make: str
    Model: str
    Year: int
    Mileage: int




# # input for car price prediction
# class CostPredInput(BaseModel):
#     Institute_brand_value : str
#     Course_Offered: str
#     Course_level: str
#     No_of_Instructors: int
#     Total_Course_Hours: int
#     Mode_of_Course: str
#     Certification_Exam: str
#     Placement_Offered: str
#     Licencing_and_Registration: int
#     Infrastructure_Cost: int
#     Technical_Requirements: int
#     Monthly_Rent: int
#     Monthly_Bills: int
#     Advertising_Marketing: int
#     Maintenance: int
#     Non_teaching_staff_salary: int
#     teaching_staff_salary: int

# # creating api endpoint for car price prediction
# @app.post('/cost_prediction')
# def cost_predict(input_param: CostPredInput):
#     print(input_param)
#     data = input_param.json()
#     print(data)
#     input_dict = json.loads(data)

#     df = pd.DataFrame([input_param.dict ().values()], columns=input_param.dict ().keys())

#     inst = input_dict['Institute_brand_value']
#     courses = input_dict['Course_Offered']
#     level = input_dict['Course_level']
#     no_of_intstr = input_dict['No_of_Instructors']
#     hours = input_dict['Total_Course_Hours']
#     mode = input_dict['Mode_of_Course']
#     cert_exam = input_dict['Certification_Exam']
#     place = input_dict['Placement_Offered']
#     licence = input_dict['Licencing_and_Registration']
#     infra = input_dict['Infrastructure_Cost']
#     tech_req = input_dict['Technical_Requirements']
#     rent = input_dict['Monthly_Rent']
#     bill = input_dict['Monthly_Bills']
#     adv_market = input_dict['Advertising_Marketing']
#     maintenance = input_dict['Maintenance']
#     nts_salary = input_dict['Non_teaching_staff_salary']
#     ts_salary = input_dict['teaching_staff_salary']
    

#     input_list = [inst, courses, level, no_of_intstr, hours, mode, cert_exam, place, licence, 
#                  infra, tech_req, rent, bill, adv_market, maintenance, nts_salary, ts_salary]

#     prediction = load_lr.predict(df)

#     return prediction[0]
