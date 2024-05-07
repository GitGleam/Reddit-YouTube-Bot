# Import necessary libraries
import praw
import random
import os
import webbrowser
import re
from datetime import datetime, timedelta
import time

# Initialize Reddit bot with your credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    username='YOUR_REDDIT_USERNAME',
    password='YOUR_REDDIT_PASSWORD',
    user_agent='YOUR_USER_AGENT_NAME'
)

# Specify the subreddit to monitor
subreddit = reddit.subreddit("Sub4Sub")

# Create a file to store replied posts if it doesn't exist
if not os.path.isfile("posts_replied_to.txt"):
    with open("posts_replied_to.txt", 'w'):
        pass

# Define possible replies, you can have as many as you want or only 1
possible_replies = [
    "YOUR_REPLY_WITH_YOUR_YOUTUBE_LINK_1",
    "YOUR_REPLY_WITH_YOUR_YOUTUBE_LINK_2",
    "YOUR_REPLY_WITH_YOUR_YOUTUBE_LINK_3",
    "YOUR_REPLY_WITH_YOUR_YOUTUBE_LINK_4",
    "YOUR_REPLY_WITH_YOUR_YOUTUBE_LINK_5",
    # Add more replies as needed
]

# Define the function to comment on submissions
def docomment():
    print("Bot started - Commenting on new posts")
    
    # Get the current time
    current_time = datetime.utcnow()
    # Calculate the time threshold (7 hour ago)
    threshold_time = current_time - timedelta(hours=7)
    
    # Iterate through the newest submissions
    for submission in subreddit.new(limit=None):
        # Check if the submission creation time is within the last hour
        if datetime.utcfromtimestamp(submission.created_utc) >= threshold_time:
            # Load IDs of already replied posts
            with open("posts_replied_to.txt", 'r') as file:
                done = file.read().split(',')
            
            # Check if the submission has not been replied to
            if submission.id not in done:
                # Extract YouTube link from the submission's text using regex
                youtube_link = re.search(r'(https?://(?:www\.)?youtube\.com/\S+|https?://(?:www\.)?youtu\.be/\S+)', submission.selftext)
                
                # Check if a YouTube link is found
                if youtube_link:
                    youtube_url = youtube_link.group(0)
                    print("Opening YouTube link:", youtube_url)
                    # Open the YouTube link in the default web browser
                    webbrowser.open(youtube_url)
                    # Wait for 5 minutes after opening the YouTube video
                    time.sleep(300)
                
                # Choose a random reply from the list
                random_reply = random.choice(possible_replies)
                print("Replying to post:", submission.title)
                # Reply to the submission
                submission.reply(random_reply)
                # Wait for 9 seconds before proceeding
                for i in range(9):
                    time.sleep(1)
                    print(i)
                # Append the ID of the replied post to the file
                with open("posts_replied_to.txt", "a") as posts_replied_to:
                    posts_replied_to.write(submission.id + ",")
                    # Update the list of replied posts
                    done.append(submission.id)
            else:
                print("Skipping the submission (already replied to).")
        # Proceed to the next submission immediately without waiting if a submission is skipped
        continue

# Define the main function to run the bot continuously
def go():
    while True:
        try:
            docomment()
        except KeyboardInterrupt:
            print("\nOk stopping bot")
            exit(0)
        except Exception as error:
            # Log the error
            if not os.path.isfile("logs.txt"):
                open("logs.txt", 'w').write('')
            now = datetime.now()
            date = now.strftime("%m/%d/%Y %H:%M:%S")
            file = open("logs.txt", 'a')
            file.write("\n"+date)
            file.write("\n"+str(error))
            print("Unknown error, find the error in logs.txt")
            print('Waiting for 10 min')
            # Wait for 5 minutes before retrying
            time.sleep(300)
            # Continue running the bot
            continue
        # Wait for 10 minutes before checking for new submissions again
        print("Waiting for 10 minutes before checking for new submissions again")
        time.sleep(600)

# Start the bot
go()
