from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn

# loading the model
load_gnb = pickle.load(open('./gnb_model', 'rb'))



# initializing app
app = FastAPI()


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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=30000)
