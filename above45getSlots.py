import requests
from playsound import playsound
import time
import random
from datetime import date

user_agent_list = [
    'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/4.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/4.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

def main():
    district_id, date = getUserRequirements()
    while True:

       alert(district_id, date,1)
       time.sleep(5)



def alert(district_id, date,flag):
    slots = getSlots(district_id, date) if(flag == 1 ) else getSlotsByPin(district_id,date)
    if slots is None :
        print("NONE")
    n_s = 0
    for x in slots:
        venues = slots[x] 
        for v in venues :
            sessions = v.get('sessions')
            print("Center Name: %s" %(v.get('name')))
            for s in sessions :
       
                cap = s.get('available_capacity')
               
                age = s.get('min_age_limit')
                print('Date: %s Available capacity %d Age %d' %(s.get('date'), cap, age))
                #print('Available capacity:',cap)
                #print('Age',age)
                
                if age==45 and cap>0:
                     n_s =  n_s + cap
                     print(s)
                    
 
        
    if n_s>0:
        playsound('salert.mp3')


def getStates():
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states', headers = headers)
    json_data = response.json()
    return json_data


def getDistricts(state_id):
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
    request_url = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/' + str(state_id)
    print(request_url)
    response = requests.get(request_url, headers = headers)
    json_data = response.json()
    #print(json_data)
    return json_data

def getSlots(district_id, date):
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
    request_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + str(district_id) + '&date=' + date
    response = requests.get(request_url,headers=headers)
    #print(response)
    json_data = response.json()
    return json_data

def getSlotsByPin(district_id, date):
	print("SLOT BY PIN")
	print(district_id)
	user_agent = random.choice(user_agent_list)
	headers = {'User-Agent': user_agent}
	request_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=' + str(district_id) + '&date=' + date
	response = requests.get(request_url,headers=headers)
	json_data = response.json()
	return json_data

def getUserRequirements():
    
    states = getStates().get('states')
    for x in states:
        print("State: %s Id: %d" % (x.get('state_name'), x.get('state_id')))
    print('Select state - Please input Id value of your state')    
    state_id = input()
    
    districts = getDistricts(state_id).get('districts')
    for d in districts:
        print("District: %s Id: %d" % (d.get('district_name'), d.get('district_id')))
    print('Select district - Please input Id value of your district')
    district_id = input()
    
    today = date.today().strftime("%d-%m-%Y")

    return district_id, today   

if __name__ == "__main__":
    main()