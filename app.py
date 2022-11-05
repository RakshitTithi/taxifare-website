import streamlit as st
import datetime
import requests
import urllib.parse

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
date_and_time
pickup_longitude
pickup_latitude
dropoff_longitude
dropoff_latitude
passenger_count
'''



date_and_time=st.date_input('Insert a date and time')
pickup_longitude=st.number_input('Insert a pickup long',value=23.5)
pickup_latitude=st.number_input('Insert a pickup lat')
dropoff_longitude=st.number_input('Insert a dropoff long')
dropoff_latitude=st.number_input('Insert a dropoff lat',)
passenger_count=st.number_input('Insert passenger count',value=0)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''
params={
    'date_and_time':date_and_time,
    "pickup_longitude":pickup_longitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':passenger_count

}
'''
3. Let's call our API using the `requests` package...
'''
new_url=f'https://taxifare.lewagon.ai/predict?{urllib.parse.urlencode(params)}'
request=requests.get(new_url)

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
prediction=request.json()
print(new_url)
st.write(prediction)
