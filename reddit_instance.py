from dotenv import load_dotenv
load_dotenv()

import os
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_ID = os.getenv("SECRET_ID")
PASSWORD = os.getenv("PASSWORD")

import praw
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_ID,
    password=PASSWORD,
    user_agent="reddit_assign by u/Narrow_Block_8755",
    username="Narrow_Block_8755",
)

# print(reddit.read_only)

from llm_groq import CallGroq
def posting(username = "u_Narrow_Block_8755"):
    subreddit = reddit.subreddit(username)
    subreddit.submit(title="Daily Blog", selftext=CallGroq())

# reddit.read_only = True

from llm_groq import CommentGroq
def commenting(url):
    submission = reddit.submission(url = url)
    reply = CommentGroq(post = submission.selftext)
    submission.reply(reply)

def thread(url):
    comment = reddit.comment(url = url)
    reply = CommentGroq(post = comment.body)
    comment.reply(reply)

# print(commenting("https://www.reddit.com/user/Narrow_Block_8755/comments/1i5tq4m/ai_generated_content/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button"))