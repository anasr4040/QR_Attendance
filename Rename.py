import os
import re


path = r'C:\Users\marte\Downloads\Compressed\Scinnova Tickets'
names = os.listdir(path)

"""
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
"""

for name in names:
    res = re.findall(r'\(.*?\)', name)
    ex= ''.join(res)

    New_name = path + f"\{str(ex.strip('()'))}.pdf"
    OldName = path + f"\{name}"
    try:
        os.rename(OldName, New_name)
    except:
        pass
