from twitter import *

consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

print(t.statuses.home_timeline())

t.statuses.update(status="Hello world, using python")

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
