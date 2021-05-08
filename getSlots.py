import requests
from playsound import playsound
import time
import random
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

def main():
   while True:
       alert()
       time.sleep(120)



def alert():
    #states = getStates() used this to get state id for assam
    #districts = getDistricts() #used this to get district id for kamrup metro
   # print(districts)
    slots = getSlots()
    #playsound('alert.mp3')
    if slots is None :
        print("NONE")
    n_s = 0
    for x in slots:
        venues = slots[x] 
        for v in venues :
            sessions = v.get('sessions')
            print(v.get('name'))
            for s in sessions :
       
                cap = s.get('available_capacity')
               
                age = s.get('min_age_limit')
              
                print(cap)
                print(age)
                
                if age<45 and cap>0:
                     n_s =  n_s + cap
                     print(s)
                    
 
        
    if n_s>0:
        playsound('salert.mp3')


def getStates():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states')
    json_data = response.json()
    return json_data


def getDistricts():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/4')
    json_data = response.json()
    #print(json_data)
    return json_data

def getSlots():
    
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
   # response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=47&date=07-05-2021')
    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=49&date=08-05-2021',headers=headers)
    #print(response)
    json_data = response.json()
    return json_data


if __name__ == "__main__":
    main()
