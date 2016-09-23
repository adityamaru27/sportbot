import os
from slackclient import SlackClient
import time

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)

def listchannels():
	channels_call = slack_client.api_call("im.list", token=SLACK_TOKEN, scope="im:read")
	if channels_call.get('ok'):
		slack_client.api_call("chat.postMessage", token=SLACK_TOKEN, channel='D2DFH5WAZ', text="What sport would you like to know about!")
	return None

def interaction():
	if slack_client.rtm_connect():
		while True:
			x =  slack_client.rtm_read()
			for words in x:
				if "type" in words:
					if words["type"] == "message" and "text" in words:
						message = words["text"]
						if message == "sport" or message == "sports":
							channels = listchannels()
							if channels:
								print ("Channels: ")
								for c in channels:
									print c
									# if "name" in c:
									# 	if c["name"] == "adityamaru":
									# 		slack_client.rtm_send_message(c["id"], "Which sport would you like to know about!")
			time.sleep(1)
	else:
		print "Not able to connect"			
	
if __name__ == '__main__':
	interaction()
    # # channels = listchannels()
    # if channels:
    #     print("Channels: ")
    #     for c in channels:
    #         print(c['name'] + " (" + c['id'] + ")")
    # else:
    #     print("Unable to authenticate.")		

