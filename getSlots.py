import requests


def main():
    getStates()
   





def getStates():
    response = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states')
    json_data = response.json()
    print(json_data)
    

getStates()

if __name__ == "__main__":
    main()
