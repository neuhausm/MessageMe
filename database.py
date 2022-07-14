import mysql.connector
from datetime import date
PASSWORD = 'yaya2000'
USER = 'root'
HOST = 'localhost'
DATABASE = 'message_schema'

def sendToDatabase(pn,msg,sendDate,sendTime,userPn,userName):
    import mysql.connector
    cnx = mysql.connector.connect(user='root', password='yaya2000',host='localhost',database='message_schema')
    cursor = cnx.cursor()
    sql_data = {'pn':pn,'msg':msg,'sendDate':sendDate,'sendTime':sendTime,'userPn':userPn,'userName':userName}
    add_info = ("INSERT INTO table_2"
               "(id,phone_num, msg,sendDate,sendTime,userName,userPhone) "
               "VALUES (null,%(pn)s, %(msg)s, %(sendDate)s, %(sendTime)s,%(userPn)s,%(userName)s)")
    cursor.execute(add_info,sql_data)
    cnx.commit()

    cursor.close()
    cnx.close()

def getData():
    import mysql.connector
    from datetime import date
    cnx = mysql.connector.connect(user=USER, password=PASSWORD,host=HOST,database=DATABASE)
    cursor = cnx.cursor(dictionary=True)

    todayTemp = date.today()
    today = todayTemp.strftime('%B %d, %Y')

    get_info = ("SELECT * FROM table_2 WHERE sendDate = '%s'" % today)
    cursor.execute(get_info)
    myresult = cursor.fetchall()
    
    print(myresult)
    cursor.close()
    cnx.close()
    return myresult
  
