import mysql.connector
import pandas as pd

names = []
teamID = []
contacts = []
Modules = []
State = []
TimeStamp = []


def viewdatabase():
    conn = mysql.connector.connect(
        host="addYourServerIpAddress",
        user="AddYourUserName",
        password="AddPassword",
        database="AddDatabaseName"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM Attendance")
    rows = c.fetchall()

    for row in rows:
        names.append(row[0])
        teamID.append(row[1])
        contacts.append(row[2])
        Modules.append(row[3])
        State.append(row[4])
        TimeStamp.append(row[5])
    conn.close()


    data = pd.DataFrame({"TimeStamp": TimeStamp,
                         "Names": names,
                         "TeamID": teamID,
                         "Contacts": contacts,
                         "Modules": Modules,
                         "State": State})

    writer = pd.ExcelWriter("Attendance.xlsx", engine='xlsxwriter')
    data.to_excel(writer, sheet_name="Data", index=False)
    writer.save()


viewdatabase()

