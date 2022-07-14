def sendMessage():
    import Twilio as tw
    import database as db 

    data = db.getData()
    for i in data:
        print(i)
        tw.sendText(i['phone_num'],i['msg']) 
sendMessage()