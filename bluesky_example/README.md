# BlueSky Canada scraper

A daily scraper that searches BlueSky for posts mentioning "Canada" and saves them to a CSV file.

## What it does

- Searches BlueSky for recent posts containing "Canada"
- Runs automatically every day at 2 AM UTC via GitHub Actions
- Saves results to `bluesky_canada_posts.csv`
- Updates the file daily, removing duplicates

## Setup

1. **Fork or create this repository on GitHub**

2. **Add BlueSky credentials as secrets**
   - Go to your repository's Settings > Secrets and variables > Actions
   - Click "New repository secret"
   - Add `BLUESKY_USERNAME` with your BlueSky handle (e.g., `yourname.bsky.social`)
   - Add `BLUESKY_PASSWORD` with your BlueSky password (or app password)

3. **Enable GitHub Actions**
   - Go to your repository's Settings > Actions > General
   - Under "Workflow permissions", select "Read and write permissions"
   - Click Save

## Manual trigger

You can manually trigger the scraper from GitHub:
- Go to Actions tab
- Click "Daily BlueSky Scraper"
- Click "Run workflow"

## Files

- `scrape_bluesky.py` - Main scraping script
- `.github/workflows/daily-scrape.yml` - GitHub Actions workflow
- `pyproject.toml` - Python dependencies
- `bluesky_canada_posts.csv` - Output data file (created after first run)

## Customization

To search for different terms, edit `scrape_bluesky.py` and change `'Canada'` to your desired search term.

To change the schedule, edit the cron expression in `.github/workflows/daily-scrape.yml`.
