import os
import json
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

SESSION_FILE = "../linkedin_session.json"


def is_valid_session():
    """Check if the session file exists and contains valid data."""
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                data = json.load(f)
                return bool(data)  # Ensure file isn't empty
        except (json.JSONDecodeError, IOError):
            print("⚠️ Session file is invalid or corrupted. Deleting and performing fresh login...")
            os.remove(SESSION_FILE)
            return False
    return False


def login_to_linkedin():
    """Perform a fresh login and save session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for silent execution
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.linkedin.com/login")

        # Load environment variables
        load_dotenv()
        email = os.getenv("LINKEDIN_EMAIL")
        password = os.getenv("LINKEDIN_PASSWORD")

        if not email or not password:
            print("⚠️ Please set your LinkedIn credentials as environment variables!")
            return None

        # Enter credentials and log in
        page.fill('[id="username"]', email)
        page.fill('[id="password"]', password)
        page.click("button[type='submit']")
        page.wait_for_load_state("load")  # Ensure page loads fully

        # Save session for future logins
        context.storage_state(path=SESSION_FILE)
        print("✅ Logged in successfully! Session saved.")

        return page  # Return page object for further actions


def login_with_session(playwright):
    """Use saved session to log in and return the browser, context, and page."""
    browser = playwright.chromium.launch(headless=False)  # Keep browser open
    context = browser.new_context(storage_state=SESSION_FILE)
    page = context.new_page()

    page.goto("https://www.linkedin.com/feed/")
    print("✅ Logged in using saved session!")

    return browser, context, page  # Return all objects


if __name__ == "__main__":
    if is_valid_session():
        use_session = input("🔹 Session file found. Use saved session? (y/n): ").strip().lower()
        if use_session == 'y':
            page = login_with_session()
        else:
            print("🔄 Performing fresh login...")
            page = login_to_linkedin()
    else:
        print("⚠️ No valid session file found. Logging in from scratch...")
        page = login_to_linkedin()
