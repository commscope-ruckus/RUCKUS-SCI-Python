import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request ")

ipaddress = input("What is the SCI IP Address? ")
username = input("What is the username? ")
password = input("What is the password? ")
ipaddress = "your SCI ip address"
username = "admin"
password = "password"

url1 = "https://" + ipaddress + "/api/users/login"
params1 = {'username':username,'password':password} 

r = requests.post(url1, json= params1,verify=False)
token = r.json()['id']
print ("token: ", token)

reportId = input("What is the Report ID? ")
sectionId = input("What is the Section ID? ")
startDate = input("What is the start date (YYYY-MM-DD)? ")
endDate = input("What is the end date (YYYY-MM-DD)? ")
dimension = input("What is the dimension? ")
value = input("What is the value? ")
#reportId = "1"
#sectionId = "14"
#startDate = "2019-09-21"
#endDate = "2019-09-21"
#dimension = "manufacturer"
#value = "Apple, Inc."

url2 = "https://" + ipaddress + "/api/reports/" + reportId + "/sections/" + sectionId + "/data" + "?access_token=" + token
params2 = {'start':startDate, 'end':endDate, 'filter':{"type":"selector", "dimension":dimension, "value":value}}

s = requests.post(url2, json=params2, verify=False) 
print (s.json())

#This section prints tabulated data 
#for i in s.json():
#	for j in s.json()[i]:
#		for k, v in j.items():
#  			print(k,'\t', v)

