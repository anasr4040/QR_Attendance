import os
import shutil


pathKarachi = r"C:\Users\marte\Downloads\Compressed\ID PICTURES - KARACHI TEAMS"
pathCedar = r"C:\Users\marte\Downloads\Compressed\ID PICTURES - CEDAR"

ListDirK = os.listdir(pathKarachi)
ListDirC = os.listdir(pathCedar)


for folder in ListDirK:
    pathTeam = r"C:\Users\marte\Downloads\Compressed\ID PICTURES - KARACHI TEAMS" + f"\{folder}"
    ImagesList = os.listdir(pathTeam)
    for image in ImagesList:
        source = pathTeam + f"\{image}"
        destination = r"C:\Users\marte\Desktop\ANAS\ANAS\PROJECTS\QR_CODE Attendance system\Participant Pictures" + f"\{image}"
        shutil.copy(source, destination)
print("Karachi Teams Done")


for folder in ListDirC:
    pathTeam = r"C:\Users\marte\Downloads\Compressed\ID PICTURES - CEDAR" + f"\{folder}"
    ImagesList = os.listdir(pathTeam)
    for image in ImagesList:
        source = pathTeam + f"\{image}"
        destination = r"C:\Users\marte\Desktop\ANAS\ANAS\PROJECTS\QR_CODE Attendance system\Participant Pictures" + f"\{image}"
        shutil.copy(source, destination)

print("Cedar Teams Done")

