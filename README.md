# Reddit API Fetch Script

This script uses PRAW library to fetch 5 latest posts of a certain subreddit. It handles authentication, API errors, and some of the most common errors.

## Necessities

Beforehand you should have:
- Python 3 installed
- Reddit API credentials (Client ID, Client Secret, and User Agent)
- Necessary Python packages installed

## Installation

1. Clone or download this repo.
2. Navigate to project folder:
   ```bash
   cd project_folder
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps.
2. Click Create App and choose Script as the type.
3. Copy the `client_id` and `client_secret` from the app details.
4. Create a `.env` file in the project directory and add the following:
   ```env
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   USER_AGENT=your_user_agent_here
   ```

## Script run

Run the script:
```bash
py reddit_fetch.py
```

Modify the function call at the bottom of the script:
```python
fetch_posts("your_subreddit_here")
```

## Error Handling

The script includes exception handling for:
- Network errors
- API rate limits
- Authentication failures
- Invalid or restricted subreddits

## Author
Ornel Mero

