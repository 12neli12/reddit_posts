import praw
import prawcore
import os
from dotenv import load_dotenv

def fetch_posts(name: str, post_num: int = 5):
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

    # Network issues handling
    except prawcore.exceptions.RequestException:
        print("Network error. Check your internet connection.")

    # API rate-limiting handling
    except prawcore.exceptions.TooManyRequests:
        print("Error. Rate-limited by Reddit.")

    # Authentication issues handling
    except prawcore.exceptions.OAuthException:
        print("Error. Check your ID, user agent, and secret.")

    # Subreddit does not exist
    except prawcore.exceptions.NotFound:
        print(f"Error. Subreddit r/{name} not found.")

    # Access-restricted handling
    except prawcore.exceptions.Forbidden:
        print("Error. Access forbidden.")

    # PRAWCore general exception handling
    except prawcore.exceptions.PrawcoreException as e:
        print(f"Error: {e} ")

    # Catch other errors
    except Exception as e:
        print("Unexpected error: ", e)

# Fetches latest posts from wanted subreddit
fetch_posts("mma")