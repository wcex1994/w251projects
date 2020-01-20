# -*- coding: utf-8 -*-
  

import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
from ibm_botocore.client import Config
import ibm_boto3
import time

# Define MQTT constants
HOST = "172.18.0.2"
PORT = 1883
TOPIC = "hw03cloud"

# Reference: https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/ee1d0b44-0fce-4cf6-8545-e1dc961d0668/view?access_token=c0489b861ab65f63be7e3c5ce962003a2a0197660e67ecb140c477c2e11b5fe3
# Reference: https://cloud.ibm.com/docs/services/cloud-object-storage/libraries?topic=cloud-object-storage-python#python-examples-multipart-transfer
# Define upload large file function:
credentials = {
        "apikey": "BZ0K1O6GUWMHwwWtgr7-apihCKTgmZ050Wjq5n1E1mF_",
        "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
       #"endpoints":"https://s3.us-south.cloud-object-storage.appdomain.cloud",
        "iam_apikey_description": "Auto-generated for key 23c88bd6-d998-4b34-b3b8-9e153904944c",
        "iam_apikey_name": "w251haileywu-hw3",
        "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/91fca120c43f487dab0bde3d66227187::serviceid:ServiceId-a7d5560b-1146-4871-b450-873022444d51",
        "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/91fca120c43f487dab0bde3d66227187:a068536e-1950-450c-b9c1-91fbfd0e697d::"
    }
IBM_AUTH_ENDPOINT= 'https://iam.cloud.ibm.com/identity/token'
cos_resource = ibm_boto3.resource("s3",
        ibm_api_key_id=credentials['apikey'],
        ibm_service_instance_id=credentials['resource_instance_id'],
        #ibm_service_instance_id=credentials['iam_serviceid_crn'],
        ibm_auth_endpoint=IBM_AUTH_ENDPOINT,
        config=Config(signature_version='oauth'),
        endpoint_url=credentials['endpoints'])

def get_buckets():
    print("Retrieving list of buckets")
    try:
        buckets = cos.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}".format(bucket.name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

def on_connect(clnt, user, flags, rc):
    mqttclient.subscribe(TOPIC)
    print('user connected!')
    print("connected with rc:" + str(rc))

i = 0

def on_message(client, userdata, msg):
    print ("message received!",str(len(msg.payload)))
    get_buckets()
    global i
    global path
    # Defining the image name that will be in the bucket
    name = 'face'+str(i)+'.png'
    try:
        bucketname = 'w251haileywu-hw3'
        #upload_large_file(bucketname,name, msg.payload)
        #cos_resource.Object(name='251haileywu-hw3').put_object(Key=name, Body=msg.payload)
        cos_resource.Object(bucketname,name ).put(Body=msg.payload)
    except Exception as e:
        print(Exception, e)
    i+=1
    #print("Imagee Stored")


mqttclient = mqtt.Client('uploadimg')
mqttclient.on_connect = on_connect
mqttclient.connect(HOST, PORT)
mqttclient.on_message = on_message
print('message function is proper')

time.sleep(5)

# go into a loop
mqttclient.loop_forever()
