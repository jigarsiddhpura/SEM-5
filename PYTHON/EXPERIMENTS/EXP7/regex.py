import re 

file = open('./EXP7/sample.txt')
text = file.read()
print(text)
email_pat = r'[\w\+\w]+@[\w\.\+]+.com'
mob_pat = r'[0-9]+[\-*]*[0-9]+[\-*]*[0-9]'
url_pat = r"(https?://|www.)[\w]+\.com/?"
# url_pat = r"(https://|www.|http://)[a-zA-]+\.[a-zA-Z]+"
# url_pat = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
# name_pat = r'M(?:r\.|rs\.|s\.) [a-zA-Z]+'
name_pat = r'M(?:r|rs|s). [\w]+'

print(f"Emails in text field are : {re.findall(email_pat,text)}")
print(f"Phone numbers are : {re.findall(mob_pat,text)}")
print(f"Names are : {re.findall(name_pat,text)}")
# print(f"Urls are : {re.findall(url_pat,text)}")
print(f"Urls are : {[i.group() for i in re.finditer(url_pat,text)]}\n")