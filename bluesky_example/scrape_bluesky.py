"""
Add overview
"""

import pandas as pd
from atproto import Client # Explain why this import is different to the one above
from datetime import datetime, timezone
import os # Explain why os is needed

def scrape_bluesky_canada():
    """Add an explaination of what this function `scrape_bluesky_canada` does"""
    
    # Initialize client and login
    client = Client()
    username = os.environ.get('BLUESKY_USERNAME')
    password = os.environ.get('BLUESKY_PASSWORD')
    
    if not username or not password:
        raise ValueError("BLUESKY_USERNAME and BLUESKY_PASSWORD environment variables must be set")
    
    client.login(username, password)
    print(f"Searching BlueSky for 'Canada' at {datetime.now(timezone.utc)}")
    
    # Search for posts mentioning Canada
    # limit=100 gets recent posts, adjust as needed
    response = client.app.bsky.feed.search_posts(params={'q': 'Canada', 'limit': 100})
    
    # Extract post data into a simple list
    posts_data = []
    for post in response.posts:
        posts_data.append({
            'text': post.record.text,
            'author': post.author.handle,
            'created_at': post.record.created_at,
            'uri': post.uri,
            'scraped_at': datetime.now(timezone.utc).isoformat()
        })
    
    print(f"Found {len(posts_data)} posts")
    
    # Convert to DataFrame
    new_df = pd.DataFrame(posts_data)
    
    # Load existing data if it exists, otherwise start fresh
    csv_file = 'bluesky_canada_posts.csv'
    if os.path.exists(csv_file):
        existing_df = pd.read_csv(csv_file)
        # Combine old and new data, remove duplicates based on URI
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df = combined_df.drop_duplicates(subset=['uri'], keep='last')
        print(f"Updated file with {len(new_df)} new posts. Total: {len(combined_df)} posts")
    else:
        combined_df = new_df
        print(f"Created new file with {len(combined_df)} posts")
    
    # Save to CSV
    combined_df.to_csv(csv_file, index=False)
    print(f"Saved to {csv_file}")

# Explain what these next two lines do
if __name__ == "__main__":
    scrape_bluesky_canada()
