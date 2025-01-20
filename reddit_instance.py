import praw

from dotenv import load_dotenv
load_dotenv()

import os
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_ID = os.getenv("SECRET_ID")
PASSWORD = os.getenv("PASSWORD")

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_ID,
    password=PASSWORD,
    user_agent="reddit_assign by u/Narrow_Block_8755",
    username="Narrow_Block_8755",
)

# print(reddit.read_only)

from llm_groq import CallGroq

subreddit = reddit.subreddit("u_Narrow_Block_8755")
subreddit.submit(title="AI Generated Content", selftext=CallGroq())
# reddit.read_only = True

