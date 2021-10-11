#Made by Gabbi Hacked

f="Name/font of bot"

import amino
client=amino.Client()
email=input("Email: ")
password=input("Password: ")
client.login(email=email,password=password)
print("Logged in")
subclient=amino.SubClient(comId="comid",profile=client.profile)
n=int(input("Enter approx number of bots:-"))
x=subclient.get_all_users(start=0,size=n)
j=1
for i,u in zip(x.profile.nickname,x.profile.userId):
	if i:
		try:
			subclient.ban(userId=u, reason="spam joining here",banType=2)
			print(f"{j} ) banned {i}")
			j=j+1
		except:
			pass
	else:
		print("Not a bot id")
print("All done")