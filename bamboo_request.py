#!/usr/bin/env python

# Hubert Cross
# Sample script that uses HTTP Basic Auth to access REST API on local Bamboo VM

import requests
import json 
import sys
  
# Bamboo VM
URL = "http://192.168.56.2:8085"

# HTTP basic auth
username = "admin"
password = '***'

def printout(string):
	sys.stdout.flush()
	sys.stdout.write(string)

print("Getting latest build results from Bamboo API ...")

URL = "http://192.168.56.2:8085/rest/api/latest/result?os_authType=basic"

# Let's work with JSON
headers = {'Accept' : 'application/json'}

r = requests.get(url = URL, auth=(username, password), headers=headers)

myObject = json.loads(r.text)

# print(myObject["results"]["result"])
# print("\n")
# print(myObject["results"]["result"][0]["planResultKey"])
# print("\n")

for result in myObject["results"]["result"]:
	printout("Build result key: ")
	print(result["buildResultKey"])
	printout("Life-cycle state: ")
	print(result["lifeCycleState"])
	printout("Build State: ")
	print(result["buildState"])
	printout("Build Number: ")
	print(result["buildNumber"])
	printout("\n")


print("Getting build queue details from Bamboo API ...")

URL = "http://192.168.56.2:8085/rest/api/latest/queue?os_authType=basic"

# Let's work with JSON
headers = {'Accept' : 'application/json'}

r = requests.get(url = URL, auth=(username, password), headers=headers)

myObject = json.loads(r.text)

# print(r.text)
# print("\n")
# print(myObject)
# print("\n")

printout("Build Queue Length: ")
print(myObject["queuedBuilds"]["size"])


print("\n")
print("Getting project details from Bamboo API ...")

URL = "http://192.168.56.2:8085/rest/api/latest/project?os_authType=basic"

# Let's work with JSON
headers = {'Accept' : 'application/json'}

r = requests.get(url = URL, auth=(username, password), headers=headers)

myObject = json.loads(r.text)

# print(r.text)
# print("\n")
# print(myObject)
# print("\n")

printout("Total number of projects in Bamboo: ")
print(myObject["projects"]["size"])

for project in myObject["projects"]["project"]:
	printout("Project name: ")
	print(project["name"])
	printout("Project description: ")
	print(project["description"])
	printout("\n")

# printout("Build Queue Length: ")
# print(myObject["queuedBuilds"]["size"])





