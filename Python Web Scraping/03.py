import json, requests

subreddit = 'powershell'

r = requests.get(
    'http://www.reddit.com/r/{}.json'.format(subreddit),
    headers={'user-agent': 'Mozilla/5.0'}
)

# view structure of an individual post
print(r.json()['data']['children'])

#for post in r.json()['data']['children']:
#    print('Title:',post['data']['title'])
#    print('URL:', post['data']['url'])
#    print('ups',post['data']['ups'])
#    print('Num of comments',post['data']['num_comments'])#, post['data']['selftext'])
