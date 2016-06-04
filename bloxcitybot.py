import requests
import getpass
username = input("Enter username \n")

password = getpass.getpass("Enter password \n")
r = requests.session()
r.post("https://www.bloxcity.com/account/login", data = {'username':username, 'password':password, 'submit':'LOGIN'})

title = input("Enter thread title \n")
body = input("Enter thread body \n")
duration = input("Enter number of seconds to spam \n")
print("*" *60)
for i in range(1,int(duration)):
 r.post("https://www.bloxcity.com/forum/create/2", data={'title':title, 'post':body,'submit':'Create'})
 print("Number of seconds: " + str(i))



