from twitter import *

consumer_key = '37HLDWddhRzyaWaE6RqnPtVJa'
consumer_secret = 'lk5jXOB5CLbhC0q3e1wT4JJHivWrI61ucCNeZZyXvFxh2eOZko'
token = '3148634719-pueS4ffeOJdcARm6ZJnah02jjInqjKVN3ExO84r'
token_secret = 'QCp7tIEEY14aa6BmfbY4HADc0GiemENDCyfkmcsraqZXu'

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
# fetches your timline
#data = t.statuses.home_timeline() 

data = t.search.tweets(q='#powershell')
print(t.items())

#print(data)
for status in data['statuses']:
    print('screen_name',status['user']['screen_name'])
    print('text',status['text'])
    #print('description',status['user']['description'])
    #print('profile_image_url',status['user']['profile_image_url'])
    #print('location',status['user']['location'])
    #print('followers_count',status['user']['followers_count'])
    #print('friends_count',status['user']['friends_count'])
    #print('verified',status['user']['verified'])
    #print('retweet_count',status['retweet_count'])
    #print('favorite_count',status['favorite_count'])



#for key, value in data:
#    print(key,value)
#
#for tweet in data:
#    for key, value in tweet.items():
#        if(key == 'user'):
#            print('screen_name',value['screen_name'])
#            print('location',value['location'])
#            print('description',value['description'])
#
#        if(key=='retweet_count' or key == 'favorite_count' or key=='text'):
#            print(key, value)

#t.statuses.update(status="Hello world, using python")

#
#twit = twitter.Api(**creds)
#user = twit.GetUser(screen_name = 'singhprateik')
#print(user)
#
#metric = boto3.client('cloudwatch')
#
#favcount = {
#  'Namespace': 'Twitter/pcgeek86',
#  'MetricData': [
#    {
#      'MetricName': 'FavoriteCount',
#      'Value': user.favourites_count,
#      'Unit': 'Count'
#    },
#    {
#      'MetricName': 'FriendCount',
#      'Value': user.friends_count,
#      'Unit': 'Count'
#    },
#    {
#      'MetricName': 'StatusesCount',
#      'Value': user.statuses_count,
#      'Unit': 'Count'
#    }
#  ],
#}
#metric.put_metric_data(**favcount)
#
#print('Finished writing Twitter metrics')
