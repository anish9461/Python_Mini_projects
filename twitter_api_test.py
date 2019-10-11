import twitter
import json
def oauth_login():
    CONSUMER_KEY = 'E7OnADELkfOLyaNgsrGYo44Cy'
    CONSUMER_SECRET ='XTfMIVnjJq4NL7nTpkQfK6xv7XGFp6oNIWsQnxJZBXN07pHQYT'
    OAUTH_TOKEN = '2894739414-3bIFbIHQmEsCHREt5m7IfjfctYaa3gJFJg5hBbn'
    OAUTH_TOKEN_SECRET = 'IuzLQvWfCdxmywDCBlfvROnk66vrpoZQ6aj4nBgKMEF9R'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    print('login successful')
    return twitter_api

twitter_api = oauth_login()
world_trends = twitter_api.trends.place(_id=1)
us_trends = twitter_api.trends.place(_id= 23424977)

# print(json.dumps(world_trends,indent=1))
# print(json.dumps(us_trends,indent=1))

# print only the names of the trends
for trends in [i['trends'] for i in us_trends]:
    for names in [i['name'] for i in trends]:
        print(names)