import pandas as pd
import numpy as np

def predict(num_prediction, model, cls_data, pst_days):
    prediction_list = cls_data[-pst_days:]
    
    for _ in range(num_prediction):
        x = prediction_list[-pst_days:]
        x = x.reshape((1, pst_days, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[pst_days-1:]
        
    return prediction_list
    
def predict_dates(num_prediction, df_date):
    last_date = df_date.values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    
    return prediction_dates
