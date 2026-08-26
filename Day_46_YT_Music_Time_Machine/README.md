# Day 46: Musical Time Machine (YouTube Music Edition)

## Project Overview

A web scraping and API integration script that travels back in time to a user-specified date, scrapes the Billboard Hot 100 chart for that exact week, and automatically generates a functional playlist in the user's YouTube Music library.

## Skills Demonstrated

* **Web Scraping (BeautifulSoup):** Navigating the DOM of a historical Billboard Hot 100 archive to extract 100 song titles using specific class attributes (`class_="chart-entry__title"`).
* **Third-Party API Integration (`ytmusicapi`):** Authenticating and communicating with the unofficial YouTube Music API to search for tracks, extract video IDs, and push POST requests to create and populate a new playlist.
* **Exception Handling:** Implementing `try/except` blocks to catch `ValueError` for incorrect date formats and `RequestException` for network connectivity issues.

## 🎓 Acknowledgements & Custom Upgrades

The foundational concept for this "Time Machine" project originates from the "100 Days of Code™: The Complete Python Pro Bootcamp". 

**Custom R&D:** The original course curriculum relies on the Spotify API (`spotipy`). However, I completely re-engineered this module to interface with the **YouTube Music API** (`ytmusicapi`). I would also like to acknowledge the use of AI as a collaborative troubleshooting tool during this process—configuring the specific header authentication (`headers_auth.json`) for YT Music, especially while operating within the Opera GX browser, presented unique technical friction that required advanced debugging to resolve.

## How to Run

Ensure the file (`yt_time_machine.py`) and your valid `headers_auth.json` authentication file are in the directory. 

```bash
python yt_time_machine.py
