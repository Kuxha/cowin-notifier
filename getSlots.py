import requests
from playsound import playsound
import time

def main():
   while True:
       alert()
       time.sleep(120)



def alert():
    #states = getStates() used this to get state id for assam
    #districts = getDistricts()used this to get district id for kamrup metro
    slots = getSlots()
    #playsound('alert.mp3')
    for x in slots:
        sessions = slots[x] 
        print(sessions)
        no = len(sessions)
        print(len(sessions))
        if no>0:
            playsound('salert.mp3')


def getStates():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states')
    json_data = response.json()
    return json_data


def getDistricts():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/4')
    json_data = response.json()
    return json_data

def getSlots():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=49&date=03-05-2021 ')
    json_data = response.json()
    return json_data


if __name__ == "__main__":
    main()
