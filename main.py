import praw
import prawcore
import os
from dotenv import load_dotenv

def fetch_posts(name, post_num= 5):
    try:
        # Load env variables from .env
        load_dotenv()

        # Reddit API client
        reddit = praw.Reddit(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            user_agent=os.getenv("USER_AGENT")
        )

        subreddit = reddit.subreddit(name)

        # Prints top 'hot' posts
        for submission in subreddit.hot(limit=post_num):
            print("-" * 60)
            print("Title: ", submission.title)
            print("Author: ", submission.author)
            print("Upvotes: ", submission.score)

    # Error Handling
    except prawcore.exceptions.RequestException:
        print("Network error. Check your internet connection.")

    except prawcore.exceptions.TooManyRequests:
        print("Error. Rate-limited.")

    except prawcore.exceptions.OAuthException:
        print("Error. Check ID, user agent, and secret.")

    except prawcore.exceptions.NotFound:
        print(f"Error. Subreddit r/{name} not found.")

    except prawcore.exceptions.PrawcoreException as e:
        print(f"Error: {e} ")

    except Exception as e:
        print("Unexpected error: ", e)

# Fetches latest posts from wanted subreddit
fetch_posts("mma")
