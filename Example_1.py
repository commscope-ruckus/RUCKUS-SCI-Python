import requests # library used for HTTP requests
import warnings # library used for warnings

# disable warning messages when the server does not have a valid SSL certificate
warnings.filterwarnings("ignore", message="Unverified HTTPS request ") 

ipaddress = input("What is the SCI IP Address? ")
username = input("What is the username? ")
password = input("What is the password? ")

# 1st API call - get the authentication token
url1 = "https://" + ipaddress + "/api/users/login" 
params1 = {'username':username,'password':password} # body parameters
r = requests.post(url1, json= params1,verify=False) # verify=False allows requests when the server has an invalid certificate
token = r.json()['id'] # the authentication token stored in variable named token
print ("token: ", token) 

reportId = input("What is the Report ID? ")
sectionId = input("What is the Section ID? ")
startDate = input("What is the start date (YYYY-MM-DD)? ")
endDate = input("What is the end date (YYYY-MM-DD)? ")

# 2nd API call - get a report/section
url2 = "https://" + ipaddress + "/api/reports/" + reportId + "/sections/" + sectionId + "/data" + "?access_token=" + token
params2 = {'start':startDate, 'end':endDate}
s = requests.post(url2, json=params2, verify=False)
print (s.json()) # prints the entire response
