# importing Flask and other modules
from flask import Flask, request, render_template 
import requests, json
  
# Flask constructor
app = Flask(__name__)   
  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       return "Data Entered: "+ recipient_phone_number + user_message + send_date + time 
       
    return render_template("form.html")


@app.route('/notify', methods=['GET'])
def notify():
    import Twilio as tw
    import database as db
    pn = request.args.get("recipient")
    userPn = request.args.get("userPhone")
    userName = request.args.get("userName")
    msg = request.args.get("message")
    sendDate = request.args.get("sendDate")
    sendTime = request.args.get("sendTime")
    
    db.sendToDatabase(pn,msg,sendDate,sendTime,userPn,userName)
    tw.welcomeText(userName,userPn,msg,sendDate)
    myresult = db.getData()
 
    result = {
        "success": True,
        "phone_num": pn
        }
    return json.dumps(result)

@app.route('/done')
def done():
    return render_template("form.html")

if __name__=='__main__':
   app.run()

