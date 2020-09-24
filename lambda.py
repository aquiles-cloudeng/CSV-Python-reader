import csv
import json
import boto3
import requests

def lambda_handler(event, context):

    targetbucket = 'BUCKETNAME'
    csvkey = 'CSVFILE.csv'
    jsonkey = 'JSONKEY.json'
    
    s3 = boto3.resource('s3')
    csv_object = s3.Object(targetbucket, csvkey)
    csv_content = csv_object.get()['Body'].read().splitlines()
    s3_client = boto3.client('s3')
    l = []
    
    for line in csv_content:
        x = json.dumps(line.decode('utf-8')).split(';')
        indicador = str(x[1])
        scada = "Scada"
        
        if scada in indicador:
            nroDocumento = str(x[0])
            nroDocumento = nroDocumento.replace('"','' )
            fechaReposicion = str(x[2])
            y = { "nroDocumento": nroDocumento,"fechaReposicion":fechaReposicion}
            l.append(y)
        else:
            nroDocumento = str(x[1])
            fechaReposicion = str(x[2])
            horarioReposicion = str(x[3])
            fechaReposicion = fechaReposicion.replace("/", "-", 3)
            y = { "nroDocumento": nroDocumento,"fechaReposicion":fechaReposicion + " " + horarioReposicion}
            l.append(y)
            
        print(l)

    sendPost(y)
        
def getAPIToken():

    url = 'TOKEN-GET-URL(this is private so I deleted it)'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'client_id': 'CLIENTID',
        'client_secret': 'SECRETKEY',
        'username': 'USERNAME',
        'password': 'PASSWORD',
        'grant_type': 'password'
    }

    response = requests.request("POST", url, headers=headers, data=params, verify=False)
    print(response.request.url)
    response = response.json()
    token = response['access_token']
    return token
        
def sendPost(y):
    token = getAPIToken()
    headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
            }
    url = 'URL-TO-SEND-POST'
    requestpost = requests.post(url, headers=headers2, json=y, verify=False)
    print(requestpost)
    response_data = requestpost.json()
    print(response_data)