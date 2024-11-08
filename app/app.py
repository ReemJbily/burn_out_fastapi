from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np
import pickle

app = FastAPI()

# Define the file path
filename = r'C:/Users/Windows.10/Employee-Burn-Out/burn-out-model-catboost.pk1'

class InputDataModel(BaseModel):
    Gender: int = Field(default=0)
    Company_Type: int = Field(default=0)
    Remote: int = Field(default=0)
    Designation: int = Field(default=0)
    Resource: int = Field(default=0)

class OutputDataModel(BaseModel):
    Mental_Fatigue_Score: float = Field(default=0.0)

# Load the model
try:
    with open(filename, 'rb') as f:
        app.model = pickle.load(f)
except FileNotFoundError:
    raise HTTPException(status_code=404, detail="Model file not found")

@app.post("/predict/")
async def predict(input_data: InputDataModel):
    try:
        # Convert InputDataModel to a list
        data_list = [
            input_data.Gender,
            input_data.Company_Type,
            input_data.Remote,
            input_data.Designation,
            input_data.Resource,
            
        ]
        
        # Add work period
        work_period = 12.0
        data_list.append(work_period)
        
        # Perform prediction
        prediction_result = round(app.model.predict(data_list) * 100, 2)
        if prediction_result < 0:
            prediction_result = -prediction_result
        
        return {"burn_out": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
