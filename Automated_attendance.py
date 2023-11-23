import time
import getpass
from tqdm.auto import tqdm
import pyzbar.pyzbar
import pyqrcode
import cv2
import os
import datetime
import mysql.connector
import numpy as np
from PIL import Image
from cryptography.fernet import Fernet
import colorama
from colorama import Back, Style
colorama.init(autoreset=True)

#scanning from web cam

key = b'2jwyEjZD6vCRBPn1Hf8YgyBWRBhtw9S53WefhwxCG6o='

def encrypt(text):
    fernet = Fernet(key)
    en_text = fernet.encrypt(text.encode())
    return en_text


def decrypt(en_text):
    fernet = Fernet(key)
    de_text = fernet.decrypt(en_text).decode()
    return de_text

def scan():
    i = 0
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    while i<1:
        _,frame = cap.read()
        decodeObject = pyzbar.pyzbar.decode(frame)
        for obj in decodeObject:
            name = obj.data
            name2 = decrypt(name)
            #print(name2)
            nn,ii,pp,dd = name2.split("  ")
            P_picture = Image.open("Participant Pictures/"+nn+".jpg")
            P_picture.show()
            #userinput = input("Authenticate Participant and hit Enter otherwise hit CTRL+C")
            db = mysql.connector.connect(
                host="184.168.96.229",
                user="scinnova_ticketing",
                password="27Y]!Q3^r^pe",
                database="scinnova_ticketing"
            )
            c = db.cursor()
            #c.execute("DROP TABLE IF EXISTS Attendance")
            c.execute("CREATE TABLE IF NOT EXISTS Attendance(name VARCHAR(255), teamid VARCHAR(255), phone_no VARCHAR(255), modules VARCHAR(255), status VARCHAR(255), TimeofMark VARCHAR(255))")
            #c.execute("SELECT participant_status FROM Participant WHERE participant_name = {participant_name}".format(participant_name = nn))
            #ss = c.fetchone()
            #print(ss)
            ts = time.time()
            currentDateTime = str(datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"))
            print(currentDateTime)
            print(name2+" "+currentDateTime)
            c.execute("SELECT participant_status FROM Participant WHERE participant_name = %s", (nn,))
            stat = c.fetchall()
            listTostr = '  '.join([str(elem) for elem in stat])
            stat = listTostr.split("'")
            stat = stat[1].split("'")
            stat = str(stat[0])
            #print(stat)
            if stat == "SIGNED OUT":
                ss = "SIGNED IN"
                #print(ss)
            elif stat == "SIGNED IN":
                ss = "SIGNED OUT"
            #print(ss)
            c.execute("UPDATE Participant set participant_status = %s WHERE participant_name = %s", (ss,nn,))
            c.execute("INSERT INTO Attendance(name, teamid, phone_no, modules, status, TimeofMark) VALUES (%s,%s,%s,%s,%s,%s)",
                      (nn, ii, pp, dd, ss, currentDateTime))
            db.commit()
            i += 1

#Database portions
        cv2.imshow("QRcode",frame)
        if cv2.waitKey(1) & 0xff == ord("s"):
            cv2.destroyAllWindows()
            cv2.release()

#Create Database for participants

def database():
    conn = mysql.connector.connect(
        host="184.168.96.229",
        user="scinnova_ticketing",
        password="27Y]!Q3^r^pe",
        database="scinnova_ticketing"
    )
    c = conn.cursor()
    #c.execute("DROP TABLE IF EXISTS Participant")
    c.execute("CREATE TABLE IF NOT EXISTS Participant(participant_name VARCHAR(255), participant_teamid VARCHAR(255), participant_contact VARCHAR(255), participant_modules VARCHAR(255), participant_status VARCHAR(255))")
    conn.commit()
    conn.close()
database()


#Addparticipants
def add_User():
    Li = []
    P_name = str(input("Please Enter Participant's Name\n"))
    P_teamid = str(input("Please Enter Participant's Team Id\n"))
    P_contac = input("Please enter Participant's contact No\n")
    P_modules = input("Please enter Participant's Modules\n")
    P_status = "SIGNED OUT"
    Li.extend((P_name,P_teamid,P_contac,P_modules))
# Using list compression to covnert list to str
    listTostr = '  '.join([str(elem) for elem in Li])
    #print (listTostr)
    print(Back.YELLOW + "Please Verify the Information")
    print("Participant Name         = "+ P_name)
    print("Participant Team ID         = " + P_teamid)
    print("Participant Contact         = " + P_contac)
    print("Participant Modules         = " + P_modules)
    #P_picture = Image.open("Participant Pictures/"+P_name+".jpg")
    #P_picture.show()
    input("Press Enter to continue or CTRL+C to Break Operation")
    conn = mysql.connector.connect(
        host="184.168.96.229",
        user="scinnova_ticketing",
        password="27Y]!Q3^r^pe",
        database="scinnova_ticketing"
    )
    c = conn.cursor()
    c.execute("INSERT INTO Participant(participant_name, participant_teamid, participant_contact, participant_modules, participant_status) VALUES (%s,%s,%s,%s,%s)",
              (P_name, P_teamid, P_contac, P_modules, P_status))
    conn.commit()
    conn.close()
    listTostr = encrypt(listTostr)
    qr = pyqrcode.create(listTostr)
    if not os.path.exists('./QrCodes'):
        os.makedirs('./QrCodes')
    qr.png('./QrCodes/'+P_name+'.png',scale = 8)
# View Database

def viewdatabase():
    conn = mysql.connector.connect(
        host="184.168.96.229",
        user="scinnova_ticketing",
        password="27Y]!Q3^r^pe",
        database="scinnova_ticketing"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM Participant")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def view_person_attendance(P_name):
    conn = mysql.connector.connect(
        host="184.168.96.229",
        user="scinnova_ticketing",
        password="27Y]!Q3^r^pe",
        database="scinnova_ticketing"
    )
    c = conn.cursor()
    c.execute("SELECT name, teamid, status, TimeofMark FROM Attendance WHERE name = %s", (P_name,))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()


def viewattendance():
    conn = mysql.connector.connect(
        host="184.168.96.229",
        user="scinnova_ticketing",
        password="27Y]!Q3^r^pe",
        database="scinnova_ticketing"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM Attendance")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Admin Screen

def afterlogin():
    print("+----------------------------------------+")
    print("|    1. Add New Participant              |")
    print("|    2. View Participants                |")
    print("|    3. View Attendance                  |")
    print("|    4. View Specific Attendance         |")
    print("+----------------------------------------+")
    user_input = input("")
    if user_input == '1':
        add_User()
    if user_input == '2':
        viewdatabase()
    if user_input == '3':
        viewattendance()
    if user_input == "4":
        name = input("Enter the Participants name you want to search: ")
        view_person_attendance(name)


#Login
def login():
    print(Back.CYAN+"Please Enter Password")
    print(Back.YELLOW+"QR code attendance System")
    password = getpass.getpass()
    if password == "SCINN0VA5":
        for i in tqdm(range(4000)):
            print("", end='/r')
        print('------------------------------------------------------------------')
        print(Back.BLUE+'Qr Code Attendance System')
        afterlogin()
    if password != 'SC1N0VA5':
        print("invalid Password")
        login()


#Mainpage
def markattendance():
    print("+---------------------------------+")
    print('|      1. Mark Attendance         |')
    print('|      2. Admin login             |')
    print('+---------------------------------+')
    user_input2 = input('')
    if user_input2 == '1':
        scan()
    if user_input2 == '2':
        login()
markattendance()

