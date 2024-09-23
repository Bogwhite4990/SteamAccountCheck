# SteamAccountCheck

**⚠️ DISCLAIMER: This script is for testing purposes only. Use at your own risk! ⚠️**

## Overview

This script automates the login process for the Steam store using Selenium WebDriver. It checks the login credentials stored in a text file and logs successful logins to a separate file.

## Requirements

- Python 3.x
- Selenium library
- GeckoDriver (for Firefox)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:

   ```bash
   pip install selenium
   Download GeckoDriver and ensure it is accessible in your system's PATH.

# Usage
1. Create a text file named accounts.txt in the same directory as the script. Each line should contain credentials in the format: username:password
2. Run the script: python script_name.py (Replace script_name.py with the name of your script file.)
3. The script will attempt to log in to Steam using the provided credentials. Successful logins will be saved to valid_accounts.txt.

# Notes
- Ensure that your accounts.txt is formatted correctly; each entry should be on a new line.
- The script runs in headless mode by default. You can change this by modifying the headless option in the script.
- If you encounter any issues, ensure that the element XPaths are still valid, as they may change over time.
