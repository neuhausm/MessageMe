import requests
X_RAPID_API_KEY = '5a598827cb1df771daa8746eac794d4b'
TWILIO_PHONE_NUMBER = '+19177465798'
SID = 'AC2971234654291b575ae9c6c249759e49'

def sendText(pn,msg):
    from requests.auth import HTTPBasicAuth
    TO_NUMBER = pn 
    MESSAGE_BODY = msg 
    url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(SID)
    params = {"From":TWILIO_PHONE_NUMBER,"Body":MESSAGE_BODY,"To":TO_NUMBER}
    print(params)
    basic = HTTPBasicAuth(SID,X_RAPID_API_KEY)
    response = requests.post(url, auth=basic, data=params)
    return response.text

  
def welcomeText(userName,userPn,msg,sendDate):
    from requests.auth import HTTPBasicAuth
    TO_NUMBER = userPn 
    MESSAGE_BODY = "Welcome " + userName + " to MessageMe!" +"\nYour message: " + msg + ", will be sent on: " + sendDate
    url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(SID)
    params = {"From":TWILIO_PHONE_NUMBER,"Body":MESSAGE_BODY,"To":TO_NUMBER}
    print(params)
    basic = HTTPBasicAuth(SID,X_RAPID_API_KEY)
    response = requests.post(url, auth=basic, data=params)
    return response.text