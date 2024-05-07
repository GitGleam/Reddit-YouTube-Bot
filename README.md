# Reddit YouTube Bot
The Reddit YouTube Bot is a Python script designed to automate interactions on Reddit by monitoring a specified subreddit for new submissions extract the Youtube link and watch it and commenting back on reddit with a random reply (chosen by you) containing YouTube own links. This bot is particularly useful for promoting YouTube content within relevant subreddit communities.
**Features:**
1. Submission Monitoring: The bot continuously monitors a specified subreddit (default: "Sub4Sub" this can be changed) for new submissions.
2. YouTube Link Extraction: It extracts YouTube links from the text of submissions using regular expressions, ensuring accurate identification of YouTube URLs and opens it in a webrowser.
3. Randomized Replies: The bot selects a random reply containing a YouTube link from a predefined list of possible replies. This randomness adds variety and prevents repetitive comments. (the replies can be added in ```main.py``` replacing ```YOUR_REPLY_WITH_YOUR_YOUTUBE_LINK_1``` DO NOT REMOVE THE QUOTATION MARKS.
4. Duplicate Prevention: To avoid spamming the same submission multiple times, the bot maintains a list of replied posts in a text file and checks against it before commenting on new submissions.
5. Error Handling and Logging: The script is equipped with robust error handling mechanisms to catch and log exceptions. Errors are logged in a separate file ("logs.txt") for easy troubleshooting.

***Usage:***
1. Configuration: Before running the script, users need to configure it with their Reddit API credentials ```(client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET', username='YOUR_REDDIT_USERNAME', password='YOUR_REDDIT_PASSWORD', user_agent='YOUR_USER_AGENT_NAME')``` desired subreddit to monitor by default is "Sub4Sub", and possible reply messages containing own YouTube links.
2. Execution: Once configured, users can execute the script, and it will start monitoring the specified subreddit, commenting on new submissions as appropriate.

***Note: Users are strongly encouraged to replace placeholder values (client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET', username='YOUR_REDDIT_USERNAME', password='YOUR_REDDIT_PASSWORD', user_agent='YOUR_USER_AGENT_NAME') with their actual credentials and configurations prior to executing the script. These can be obtained from https://old.reddit.com/prefs/apps/*** 

How to obtain reddit API: 
1. Login to https://old.reddit.com/prefs/apps/
2. Select Create App
3. Select Script
4. Name can be whatever you like 
5. Description can be whatever you like
6. Redirect URL (http://localhost:8080) is a simple one to use
7. Then click create app.
Once your app is created you will see ***personal use script*** which is the client id that needs to be replaced in the script (main.py) ***secret*** is the client secret in the script and ***user agent*** is the name of the app. 

***Requirements***
1. Python 3.x: The script is written in Python, so you'll need a Python interpreter installed on your system. You can download Python from the official website: python.org.
2. PRAW (Python Reddit API Wrapper): PRAW is a Python package that provides a convenient way to interact with the Reddit API. You can install it using pip, the Python package installer. Run the following command in your terminal or command prompt: ```pip install praw``` This will install the latest version of PRAW along with its dependencies.

***How to execute***
Open terminal or comand prompt and move to path with ```cd PATH_OF_THE_SCRIPT_MAIN.PY```
Tthen run the command ```python main.py```
