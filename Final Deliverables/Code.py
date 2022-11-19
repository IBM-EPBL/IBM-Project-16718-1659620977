import wiotp.sdk.device
import time
import random
import requests
myConfig = { 
    "identity": {
        "orgId": "ewzh7u",
        "typeId": "fire-management",
        "deviceId":"222030"
    },
    "auth": {
        "token": "17171717"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
count=0
while True:
    temp=random.randint(-40,84)
    hum=random.randint(0,100)
    gas=random.randint(0,100)

    if(temp>68 and gas>80):
        
        myData={'temperature':str(temp)+chr(176)+"C", 'humidity':str(hum)+" %", 'gaslevel':str(gas)+" %", 'condition':"Turn On Harzard-Protection System" }
        
        message='Temperature:'+str(temp)+" C"+'\nHumidity:'+str(hum)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:Turn On Harzard-Protection System"

        url = "https://www.fast2sms.com/dev/bulkV2?authorization=hdp6viwrXqKO43ZSAEG2tNCY8my7LbBWkx1anQgszu0HRD5FPIPRgf7ZDrviQT6d9q1NWHXJ2emU5tBI&route=q&message="+message+"&language=unicode&flash=1&numbers=8925008868"

        response = requests.request("GET", url)
        
        print(response.text)

        print("Turn On Harzard-Protection System")
        
    elif(temp>68 and gas<80):

        myData={'temperature':str(temp)+chr(176)+"C", 'humidity':str(hum)+" %", 'gaslevel':str(gas)+" %", 'condition':"Turn On Fire-Protection System" }

        message='Temperature:'+str(temp)+" C"+'\nHumidity:'+str(hum)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:Turn On Fire-Protection System"

        url = "https://www.fast2sms.com/dev/bulkV2?authorization=hdp6viwrXqKO43ZSAEG2tNCY8my7LbBWkx1anQgszu0HRD5FPIPRgf7ZDrviQT6d9q1NWHXJ2emU5tBI&route=q&message="+message+"&language=unicode&flash=1&numbers=8925008868"

        response = requests.request("GET", url)
        
        print(response.text)

        print("Turn On Fire-Protection System")

    elif(temp<68 and gas>80):

        myData={'temperature':str(temp)+chr(176)+"C", 'humidity':str(hum)+" %", 'gaslevel':str(gas)+" %", 'condition':"Turn On Ventilation System" }

        message='Temperature:'+str(temp)+" C"+'\nHumidity:'+str(hum)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:Turn On Ventilation System"

        url = "https://www.fast2sms.com/dev/bulkV2?authorization=hdp6viwrXqKO43ZSAEG2tNCY8my7LbBWkx1anQgszu0HRD5FPIPRgf7ZDrviQT6d9q1NWHXJ2emU5tBI&route=q&message="+message+"&language=unicode&flash=1&numbers=8925008868"

        response = requests.request("GET", url)
        
        print(response.text)

        print("Turn On Ventilation-Protection System")

    else:

        myData={'temperature':str(temp)+chr(176)+"C", 'humidity':str(hum)+" %", 'gaslevel':str(gas)+" %", 'condition':"SAFE" }
        
        message='Temperature:'+str(temp)+" C"+'\nHumidity:'+str(hum)+" %"+'\nGas-level:'+str(gas)+" %"+"\nCondition:SAFE"

        url = "https://www.fast2sms.com/dev/bulkV2?authorization=hdp6viwrXqKO43ZSAEG2tNCY8my7LbBWkx1anQgszu0HRD5FPIPRgf7ZDrviQT6d9q1NWHXJ2emU5tBI&route=q&message="+message+"&language=unicode&flash=1&numbers=8925008868"

        response = requests.request("GET", url)
        
        print(response.text)

        print("SAFE")
        
    
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)
    
client.disconnect()
