import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request ")

#ipaddress = input("What is the SCI IP Address? ")
#username = input("What is the username? ")
#password = input("What is the password? ")
#reportId = str(input("What is the Report ID? "))
#sectionId = str(input("What is the Section ID? "))
#startDate = input("What is the start date (YYYY-MM-DD)? ")
#endDate = input("What is the end date (YYYY-MM-DD)? ")

ipaddress = "your ip address"
url1 = "https://" + ipaddress + "/api/users/login"
params1 = {'username':'admin','password':'your password'} 
r = requests.post(url1, json= params1,verify=False)
token = r.json()['id']
print ("token: ", token)

reportId = "4"
sectionId = "41"
url2 = "https://" + ipaddress + "/api/reports/" + reportId + "/sections/" + sectionId + "/data" + "?access_token=" + token
#params2 = {'start':startDate, 'end':endDate}
params2 = {'limit': 100, 'start':'2020-10-18T15:36:06-07:00', 'end':'2020-10-19T15:36:06-07:00'}

s = requests.post(url2, json=params2, verify=False)
print ("Unique clients : SSID") 
for i in s.json()['data']:
	print (str(int(i['clientCount'])) + " : " + i['ssid'])
