from steamapi import core, user
import requests

core.APIConnection(api_key="YOURAPIKEY", validate_key=True)
me = user.SteamUser(userurl="YOURUSERNAME")

print("Welcome to the Steam Ripper")

for each in me.owned_games:
	print("Downloading image for %s" %each.name)
	f = open(str(each.name)+".jpg",'wb')
	f.write(requests.get("https://steamcdn-a.akamaihd.net/steam/apps/%s/header.jpg?t=1556716193" % (each._id)).content)
	f.close()	

