# This is a piece of code to create a Reddit bot using the PRAW API
# The bot monitors posts in the Drexel subreddit and responds to posts containing the keyword "Drexel" with the message "Go Dragons!"
# The bot is designed to handle Reddit's rate limits to avoid interrruptions
# Run "pip install praw" in your system if you don't have this module installed before running this 

import praw
import time
import random

# Reddit API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
username = 'your_username'
password = 'your_password'
user_agent = 'your_user_agent'

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

# Define the subreddit and keyword
subreddit_name = 'Drexel'
keyword = 'Drexel'
response_message = 'Go Dragons!'

# Function to add random delays
def random_delay(min_seconds, max_seconds):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

# Function to check and respond to new posts
def respond_to_posts():
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=10):
            if keyword.lower() in submission.title.lower():
                print(f"Found a post with '{keyword}': {submission.title}")
                submission.reply(response_message)
                print("Replied with the message.")
                random_delay(30, 60)  # Add random delay to avoid rate limiting
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the bot continuously
while True:
    respond_to_posts()
    time.sleep(600)  # Wait 10 minutes before checking for new posts again
