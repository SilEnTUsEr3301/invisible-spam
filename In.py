import amino
import time
import requests

client=amino
email=input("Email: ")
password=input("Password: ")
client.login(email=email,password=password)

print("logged in")

n=input("Community/chat link: ")
fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]
print(cid)
subclient=amino.SubClient(comId=cid,profile=client.profile)

print("Joined community")

@client.event("on_text_message")
def on_text_message(data):
	while True:
			subclient.send_message(chatId=data.message.chatId,message=" .",messageType=109)
			print(f"Text spam started")

print("Spam Bot started")			
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()			
