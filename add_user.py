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
import colorama
from colorama import Back, Style
colorama.init(autoreset=True)
from cryptography.fernet import Fernet
import pandas as pd
import pyautogui
import time

input_file = r"members.xlsx"
file = pd.read_excel(input_file)
P_name = list(file['Name'])
P_institute = list(file['Institution'])
P_teamid = list(file['TeamID'])
P_contac = list(file['Contact'])
P_modules = list(file['Modules'])

key = b'2jwyEjZD6vCRBPn1Hf8YgyBWRBhtw9S53WefhwxCG6o='

def encrypt(text):
    fernet = Fernet(key)
    en_text = fernet.encrypt(text.encode())
    return en_text


def decrypt(en_text):
    fernet = Fernet(key)
    de_text = fernet.decrypt(en_text).decode()
    return de_text



def add_User(P_name, P_institute ,P_teamid, P_contac, P_modules):
    Li = []
    #P_status = "SIGNED OUT"
    Li.extend((P_name,P_institute,P_teamid,P_contac,P_modules))
# Using list compression to covnert list to str
    listTostr = '  '.join([str(elem) for elem in Li])
    #print (listTostr)
    print(Back.YELLOW + "Please Verify the Information")
    print("Participant Name            = " + P_name)
    print("Participant Isntitution     = " + P_institute)
    print("Participant Team ID         = " + P_teamid)
    print("Participant Contact         = " + P_contac)
    print("Participant Modules         = " + P_modules)
    #try:
    #    P_picture = Image.open("Participant Pictures/"+P_name+".jpg")
    #except:
    #    P_picture = Image.open("Participant Pictures/"+P_name+".png")
    #P_picture.show()
    #input("Press Enter to continue or CTRL+C to Break Operation")
    conn = mysql.connector.connect(
        host="184.168.96.229",
        user="scinnova_ticketing",
        password="27Y]!Q3^r^pe",
        database="scinnova_ticketing"
    )
    c = conn.cursor()
    P_status = "SIGNED OUT"
    #c.execute("DROP TABLE IF EXISTS Participant")
    #x = input("   ")
    c.execute("CREATE TABLE IF NOT EXISTS Participant(participant_name VARCHAR(255), participant_institute VARCHAR(255) ,participant_teamid VARCHAR(255), participant_contact VARCHAR(255), participant_modules VARCHAR(255), participant_status VARCHAR(255))")
    c.execute("INSERT INTO Participant(participant_name, participant_institute, participant_teamid, participant_contact, participant_modules, participant_status) VALUES (%s,%s,%s,%s,%s,%s)",
              (P_name, P_institute, P_teamid, P_contac, P_modules, P_status))
    conn.commit()
    conn.close()
    listTostr = encrypt(listTostr)
    qr = pyqrcode.create(listTostr)
    #qr = pyqrcode.create(listTostr)
    if not os.path.exists('./QrCodes'):
        os.makedirs('./QrCodes')
    qr.png('./QrCodes/'+P_name+'.png',scale = 8)



PNumber = len(P_name)
for Index in range(PNumber):
    add_User(P_name[Index], P_institute[Index] ,P_teamid[Index], P_contac[Index], P_modules[Index])