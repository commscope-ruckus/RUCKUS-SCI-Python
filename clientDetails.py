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

ipaddress = "your IP address"
url1 = "https://" + ipaddress + "/api/users/login"
params1 = {'username':'admin','password':'your password'} 
r = requests.post(url1, json= params1,verify=False)
token = r.json()['id']
print ("token: ", token)

reportId = "1"
sectionId = "13"
url2 = "https://" + ipaddress + "/api/reports/" + reportId + "/sections/" + sectionId + "/data" + "?access_token=" + token
params2 = {
    "granularity": "all",
    "metric": "traffic",
    "start": "2020-10-18T15:36:06-07:00",
    "end": "2020-10-19T15:36:06-07:00",
    "limit": 100
}
s = requests.post(url2, json=params2, verify=False)

reportId = "1"
sectionId = "14"
for i in range(0, len(s.json()['data']) - 1):
	clientMac = s.json()['data'][i]['key']
	clientTraffic = s.json()['data'][i]['value']
	url3 = "https://" + ipaddress + "/api/reports/" + reportId + "/sections/" + sectionId + "/data" + "?access_token=" + token
	params3 = {
        "granularity": "all",
        "metric": "traffic",
        "start": "2020-10-18T15:36:06-07:00",
        "end": "2020-10-19T15:36:06-07:00",
        "filter": {"type": "and","fields": [{"type": "selector","dimension": "clientMac","value": clientMac}]}
    }
	r = requests.post(url3, json=params3, verify=False)
	hostname = r.json()['data'][0]['hostname']
	clientIp = r.json()['data'][0]['clientIp']
	print clientMac, clientTraffic, hostname, clientIp