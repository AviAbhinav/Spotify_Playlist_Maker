# Prerequisites

1. Install Spotipy:
   - Run: pip install spotipy

2. Get Spotify API Credentials:
   - Create a Spotify Developer account: https://developer.spotify.com/dashboard
   - Create an app and get:
     - Client ID
     - Client Secret

3. Set Up Environment Variables:
   - Linux/macOS:
     export SPOTIPY_CLIENT_ID='your_client_id'
     export SPOTIPY_CLIENT_SECRET='your_client_secret'
     export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
   - Windows (Command Prompt):
     set SPOTIPY_CLIENT_ID=your_client_id
     set SPOTIPY_CLIENT_SECRET=your_client_secret
     set SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

4. Test Authentication:
   - Run a basic script to fetch user details:
     python spotify_test.py

5. Handle Errors:
   - INVALID_CLIENT: Check Client ID and Client Secret.
   - ModuleNotFoundError: Ensure Spotipy is installed (`pip install spotipy`).
   - Redirect URI Mismatch: Ensure the redirect URI in the script matches what is set in the Spotify Developer Dashboard.

