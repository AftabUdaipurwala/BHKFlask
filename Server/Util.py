import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,bath,bhk,TotalSqftAct):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    z = np.zeros(len(__data_columns))
    z[0] = bath
    z[1] = bhk
    z[2] = TotalSqftAct
    if loc_index >= 0:
        z[loc_index] = 1
    return round(__model.predict([z])[0], 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('./artifacts/bangalore_home_prices_model.pickle','rb') as f:
        __model=pickle.load(f)
    print('loading of artifacts is done')

if __name__ == "__main__":
  load_saved_artifacts()
  print(get_location_names())
  print(get_estimated_price('1st phase jp nagar', 3 , 3,1000))
  print(get_estimated_price('location_Hebbal', 3, 3, 1000))
