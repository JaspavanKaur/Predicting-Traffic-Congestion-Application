import pandas as pd
import numpy as np
import re
import io
import copy

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

import pickle

#import data
initial_traffic_volume = pd.read_csv('Train.csv')

#data preprocessing
# Splitting of date time into Year, Month, Day, Hour
initial_traffic_volume['date_time'] = pd.to_datetime(initial_traffic_volume.date_time)
initial_traffic_volume['year'] = initial_traffic_volume.date_time.dt.year
initial_traffic_volume['month'] = initial_traffic_volume.date_time.dt.month
initial_traffic_volume['day'] = initial_traffic_volume.date_time.dt.day
initial_traffic_volume['hour'] = initial_traffic_volume.date_time.dt.hour
# making a copy of the dataframe
init_traffic_volume = copy.deepcopy(initial_traffic_volume)
# Dropping of unnecessary columns to reduce dimensionality. These columns are based on our EDA,
# what can be applied to an SG context (eg. no snow) as well as trial and error to get optimized models
traffic_volume = initial_traffic_volume.drop(['date_time', "air_pollution_index", 'visibility_in_miles', 'rain_p_h', 'dew_point', 'snow_p_h', 'weather_description', 'is_holiday', 'year'], axis=1)
# Mapping of weather type to numbers
traffic_volume['weather_type'] = traffic_volume['weather_type'].map({
    'Clouds':1,
    'Clear':2, 
    'Mist':3, 
    'Rain':4, 
    'Snow':5, 
    'Drizzle':6, 
    'Haze':7,
    'Fog':8,
    'Thunderstorm':9,
    'Smoke':10,
    'Squall':11
})
#Reorganisation of columns for target (traffic volume) to be set at the last column
traffic_volume = traffic_volume[['month','day','hour','humidity', 'wind_speed', 'wind_direction', 'temperature', 'clouds_all', 'weather_type', 'traffic_volume']]
#Binning of traffic volume data into 3 levels
labels_traffic = [0, 1, 2]
traffic_volume['traffic_vol'] = pd.qcut(traffic_volume['traffic_volume'], q=3 , labels = labels_traffic)
# Dropping the numbered traffic volume column
traffic_volume = traffic_volume.drop(['traffic_volume'], axis=1)

#Normalisation of data
standardScaler = StandardScaler()
traffic_volume.iloc[:, :-1] = standardScaler.fit_transform(traffic_volume.iloc[:, :-1])

#Splitting of data into training (0.7) and testing (0.3)
X = traffic_volume.iloc[:, :-1]
y = traffic_volume.iloc[:, -1]

#Train Random Forest Model
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=110)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X,y)

#Saving the model
pickle.dump(clf, open('model.pkl','wb'))

#Loading model to compare the results
# model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[10,2,9,89,2,329,288.28,40,1]]))
