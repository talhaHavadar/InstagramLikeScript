# This script written by Talha Havadar
from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError
import sys

access_token = "1447106861.66a7a6f.2e43bd3dc3874e01baf98b092ba82355" # Your access token generated from 'get_access_token.py' script from python-instagram github repository
user_id = "1447106861" # Your userid given by 'get_access_token.py' script
client_id = "66a7a6fc2a08489bb9b5066a316895da" # Your client id from instagram developer site
client_secret = "dacc9503772147268d01789dc0b141b9" # Your client secret from instagram developer site
my_username = "talhahavadar"
api = InstagramAPI(access_token = access_token, client_secret = client_secret)
content, next_ = api.user_follows(user_id=user_id)

bros = [
	"gulgunpekmezci",
	"neslihanatn",
	"esmaorduluu",
	"gurcan.aldemir"
]

def amILikeThisPost(media_id = None):
	if media_id == None:
		print("Error: no parameter at amILikeThisPost please send media id.")
		sys.exit(1)
		pass
	likes = api.media_likes(media_id = media_id)
	amILike = False
	if len(likes) > 0:
		print("Users who likes this post: ")
		for like in likes:
			print(like.username)
			if like.username == my_username:
				amILike = True
	return amILike

def isBuddy(username):
	for bro in bros:
		if bro == username:
			return True
	return False

def main():
	for user in content:
		if isBuddy(user.username):
			print("User: %s" % (user.full_name))
			privateUser = False
			try:
				print("Getting medias for the user...")
				recent_media, next_ = api.user_recent_media(user_id = user.id, count= 20)
			except  InstagramAPIError:
				print("%s has private profile." % (user.full_name))
				privateUser = True
			# For debug purpose only
			#recent_media, next_ = api.user_recent_media(user_id = user_id, count= 2)
			#privateUser = False
			# End of debug statements
			if not privateUser:
				print("%s has not private profile." % (user.full_name))
				for media in recent_media:
					print("Media type: ", media.type, "Link: ", media.link)
					if not amILikeThisPost(media.id):
						api.like_media(media.id)
						print("Media was successfully liked by %s." % (my_username))
		else:
			print("User: %s is not my buddy." % (user.full_name))

if __name__ == "__main__":
	main()