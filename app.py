import streamlit as st
import requests

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
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
IDEA: use geo_location api to convert input=freestyle_address --> lon lat
SAME: for dropoff
'''
date_raw = st.date_input("Select date:")
date = str(date_raw).replace("/", "-")
time_raw = st.time_input("Select time:")
time = str(date)[:4] + ":" + str(time_raw)
time=time[:-3]
pick_lon = st.text_input("Select pickup longitude:")
pick_lat = st.text_input("Select pickup latitude:")
drop_lon = st.text_input("Select dropoff longitude:")
drop_lat = st.text_input("Select dropoff latitude:")
passengers = st.text_input("Select amount of passengers:")

url = 'https://taxifare.lewagon.ai/predict'

result = requests.get(f"{url}?pickup_datetime={date}%{time}&pickup_longitude={pick_lon}&pickup_latitude={pick_lat}\
    &dropoff_longitude={drop_lon}&dropoff_latitude={drop_lat}&passenger_count={passengers}").json()
print(date)
# st.write(f"{url}?pickup_datetime={date}%{time}&pickup_longitude={pick_lon}&pickup_latitude={pick_lat}\
#     &dropoff_longitude={drop_lon}&dropoff_latitude={drop_lat}&passenger_count={passengers}")

if st.button("Ready to know how many $$$ you will need to spend? :O"):
    st.write(f"You will (likely) spend: {round(result['fare'], 2)}$")

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''



#Here goes: condition for this to wait!
#while not result["fare"]:


# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
