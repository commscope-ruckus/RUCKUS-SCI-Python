import requests
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request ")

# 1st API call - get the authentication token
ipaddress = "12.33.223.89"
url1 = "https://" + ipaddress + "/api/users/login"
params1 = {'username':'admin','password':'####M@ck7777'} 
r = requests.post(url1, json= params1,verify=False)
token = r.json()['id']
print ("token: ", token)

# 2nd API call - get report/section with client mac address and traffic
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

# 3rd API call - get report/section with client ip address and hostname
reportId = "1"
sectionId = "14"
url3 = "https://" + ipaddress + "/api/reports/" + reportId + "/sections/" + sectionId + "/data" + "?access_token=" + token
params3 = {
    "granularity": "all",
    "metric": "traffic",
    "start": "2020-10-18T15:36:06-07:00",
    "end": "2020-10-19T15:36:06-07:00"
}
r = requests.post(url3, json=params3, verify=False)

# iterate through the items of the previous response, fetch the client mac address and traffic,
# then iterate through the response of the 2nd call using the client mac address as a filter
for i in range(0, len(s.json()['data']) - 1):
    clientMac = s.json()['data'][i]['key']
    clientTraffic = s.json()['data'][i]['value']
    for dict in r.json()['data']:
        if dict['clientMac'] == clientMac:
            hostname = dict['hostname']
            clientIp = dict['clientIp']
    print (clientMac, clientTraffic, hostname, clientIp)
