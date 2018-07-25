# pip install praw
import praw

reddit = praw.Reddit(
    client_id='_MupVEzusqnB4g',
    client_secret='OE88oDY9ZJZYlXUYLLM--A-R3gs',
    password='Durg@v@ti@123',
    user_agent='PrawTut',
    username='Prateeksingh1590')

subreddit = reddit.subreddit('powershell')

hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        #print(dir(submission))
        print(
            'Title: {}, fullname: {}, ups: {}, downs: {}, flair: {} url: {} views: {} comments: {} timeUTC: {}'.
            format(submission.title, submission.fullname, submission.ups,
                   submission.downs, submission.link_flair_text, submission.url,
                   submission.view_count, submission.num_comments,
                   submission.created_utc))
