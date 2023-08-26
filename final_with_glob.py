import cv2
import pytesseract
import requests
import time as time
import glob
no=1
try:
    import Image
except ImportError:
    from PIL import Image

#============TimeGet==================#
st = time.time()
import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value) 
    parts[1::2] = map(int, parts[1::2])
    return parts
from datetime import datetime
from datetime import date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
date= today.strftime("%d/%m/%y")

#================PyTesseract===============#
pytesseract.pytesseract.tesseract_cmd = r"D:/Installed_softwares/Tesseract/tesseract.exe"
face_cascade=cv2.CascadeClassifier('cascade.xml')

path = "C:/Users/Hirak/Desktop/Project/Final_with_glob/*.*"
for file in sorted(glob.glob(path),key =numericalSort):
    img=cv2.imread(file)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    faces=face_cascade.detectMultiScale(gray,1.01,7)
    for(x,y,w,h) in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        area=(x,y,x+w,y+h)
    crop_img = img[y:y+h, x:x+w]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("cropped", gray)
    (thresh, bw) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("bw", bw)
    cv2.moveWindow("bw", 540,120)

    fname='C:/Users/Hirak/Desktop/Project/Plates2/masked_img'+str(no)+'.jpg'
    cv2.imwrite(fname,bw)
    fname1='C:/Users/Hirak/Desktop/Project/Plates3/masked_img_gray'+str(no)+'.jpg'
    cv2.imwrite(fname1,gray)
    img1=cv2.imread('C:/Users/Hirak/Desktop/Project/Final/masked_img'+str(no)+'.jpg')
    if(len(pytesseract.image_to_string(Image.open('C:/Users/Hirak/Desktop/Project/Plates2/masked_img'+str(no)+'.jpg')))<=len(pytesseract.image_to_string(Image.open('C:/Users/Hirak/Desktop/Project/Plates3/masked_img_gray'+str(no)+'.jpg')))):
        np=pytesseract.image_to_string(Image.open('C:/Users/Hirak/Desktop/Project/Plates3/masked_img_gray'+str(no)+'.jpg'))
    else:
        np=pytesseract.image_to_string(Image.open('C:/Users/Hirak/Desktop/Project/Plates2/masked_img'+str(no)+'.jpg'))
    no=no+1
    # initializing bad_chars_list 
    bad_chars = [';', ':', '!', "*", " ", "‘", ".",'.','`','~','-','|','<','>','"','=','«','—','“'] 
    
    # printing original string 
    print ("License Plate Characters : " + np) 
    
    # using replace() to 
    # remove bad_chars 
    for i in bad_chars : 
        np = np.replace(i, '')   
    print ("License Plate Characters after removing bad chars : " + np) 
    
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost", user ="root", passwd="", database="car")
    #============================Balance reduction=====================#
    mycursor =mydb.cursor()
    sql = "UPDATE plate SET balance= balance-50 where number= %s"
    val = (np,)
    mycursor.execute(sql,val)
    #===================Phone number taken==============#
    sql1= "SELECT phno from plate where number= %s"
    val1=(np,)
    mycursor.execute(sql1,val1)
    myresult=mycursor.fetchone()
    for row in myresult:
        print("The user's phone number is : " + row)
    #===================Balance selection==============#
    sql2= "SELECT balance from plate where number= %s"
    val2=(np,)
    mycursor.execute(sql2,val2)
    myresult=mycursor.fetchone()
    for bal in myresult:
        print('Your current balance is ' +str(bal))
    mydb.commit()
    #=====================The Message============================#
    msg1='Your car with ' +np
    msg2=' has passed through AEC Toll Booth at '+str(current_time)
    msg3=' hrs on ' +str(date)
    msg4='. Your current balance : Rs.'+str(bal)
    msg=msg1+msg2+msg3+msg4
    print('The following message has been sent. ' +msg)
    #=====================SMS SERVICE============================#
    URL = 'https://www.way2sms.com/api/v1/sendCampaign'
    # get request
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
                'apikey':apiKey,
        'secret':secretKey,
        'usetype':useType,
        'phone': phoneNo,
        'message':textMessage,
        'senderid':senderId
        }
        return requests.post(reqUrl, req_params)
    # get response
    response = sendPostRequest(URL, '5FK16WW2LXMXZXXXPY9R3Q2GCU6ONTQK', '09H4N2YXVFXPDL19', 'stage', row, 'ryshic12@gmail.com', msg )
   
    print("Elapsed time: ", time.time() - st)
    cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()