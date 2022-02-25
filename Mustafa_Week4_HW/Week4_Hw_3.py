#Requests General Information: 
#I want to choose random information with the requests module. Acceptance Criteria
#Get the name, surname, city and country information of a random person by using the requests module. (Example=> name:Amber, surname: Murray, city: Salisbury, country: United Kingdom)
#Make lowercase and adjacent by removing the spaces. (Example=> ambermurraysalisburyunitedkingdom)
#Then randomly shuffle the location of all the characters. (Example=> mberarrumasyarubsiluniydetmdoingk)
#Apply this process for 100 different people and write in a list.
#Find that has the most characters and print it.

import requests
import random



lst = []

counter = 0

while counter < 100 :


    r = requests.get("https://randomuser.me/api/")
    #when we request random values from this web adress it gives data as dictionary
    # {"results":[{"gender":"male","name":{"title":"Mr","first":"Ray","last":"Sanders"},
    # "location":{"street":{"number":5556,"name":"Parker Rd"},
    # "city":"Gladstone","state":"Western Australia",
    # "country":"Australia","postcode":1994,
    # "coordinates":{"latitude":"-86.5077","longitude":"-7.0741"},
    # "timezone":{"offset":"-11:00","description":"Midway Island, Samoa"}},
    # "email":"ray.sanders@example.com",
    # "login":{"uuid":"cd0896e8-fc05-445b-a943-bf0c907190fd",
    # "username":"crazydog741","password":"magicman",
    # "salt":"8XcutvR3","md5":"b9a07a6e6eb7acac2b17962449f3305d",
    # "sha1":"d2e688747bd44467d7de9d1f8370ccf005e149d6",
    # "sha256":"1dcec5785abeb7dc33a51515cc8a9e01cc5b786dc10ce972b896ed6369cac2a9"},
    # "dob":{"date":"1996-09-11T13:36:47.197Z","age":26},
    # "registered":{"date":"2003-03-31T10:11:33.153Z","age":19},
    # "phone":"05-0416-0980","cell":"0418-533-759",
    # "id":{"name":"TFN","value":"595528324"},
    # "picture":{"large":"https://randomuser.me/api/portraits/men/78.jpg",
    # "medium":"https://randomuser.me/api/portraits/med/men/78.jpg",
    # "thumbnail":"https://randomuser.me/api/portraits/thumb/men/78.jpg"},
    # "nat":"AU"}],"info":{"seed":"b7c969366c94c360","results":1,"page":1,"version":"1.3"}}

    name = (str(r.json()["results"][0]["name"]["first"]).replace(" ", "")).lower()
    surname = (str(r.json()["results"][0]["name"]["last"]).replace(" ", "")).lower()
    city = (str(r.json()["results"][0]["location"]["city"]).replace(" ", "")).lower()
    country = (str(r.json()["results"][0]["location"]["country"]).replace(" ", "")).lower()

    rnd_str = name + surname + city + country
    
    lst_str = list(rnd_str)
    
    random.shuffle(lst_str)
    
    lst.append("".join(lst_str))
    
    counter += 1


result = max(lst, key=len)
print(f"The longest element of the list: {result}")
