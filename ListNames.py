import os
import pandas as pd

path = r"C:\Users\marte\Downloads\Compressed\QrCodes"
ExcelPath = r"C:\Users\marte\Downloads\Participants' Data.xls"
ListDir = os.listdir(path)

file = pd.read_excel(ExcelPath)
NamesList = list(file["Name"])

Names = []
for element in ListDir:
    FName = element.replace('.jpg', '')
    FName = FName.replace('.JPG', '')
    FName = FName.replace('.jpeg', '')
    FName = FName.replace('.png', '')
    Names.append(FName)

print(Names)
print(NamesList)

for name in Names:
    if name not in NamesList:
        print(name)

#Shaun Gabriel D_Silva
#Shaun Gabriel D'Silva
