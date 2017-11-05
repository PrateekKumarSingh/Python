from twitter import *

consumer_key = '37HLDWddhRzyaWaE6RqnPtVJa'
consumer_secret = 'lk5jXOB5CLbhC0q3e1wT4JJHivWrI61ucCNeZZyXvFxh2eOZko'
token = '3148634719-hPvEK7Joz35v5uKkkCHwj65FFAiQis5r0eYgWtm'
token_secret = 'J6AV3pAmfXrj7nUOtm8LOjdHNyeNS8u1PaWohYnAb8eT5'

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
