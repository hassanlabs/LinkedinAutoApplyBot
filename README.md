LinkedIn Auto-Apply Bot

📌 Overview

This is an automation bot built using Python and Playwright to streamline job searching and applications on LinkedIn. It allows users to search for jobs, filter relevant listings, and interact with job postings automatically.

🚀 Features

Login automation: Uses stored session cookies for authentication.

Job search: Allows users to input job title and location.

Easy Apply detection: Finds jobs with Easy Apply options (feature in progress).

🛠 Installation & Setup

1️⃣ Clone the Repository

2️⃣ Install Dependencies
Ensure you have python 3.7+ installed. 
pip install -r requirements.txt

3️⃣ Create a .env File
To store your LinkedIn login credentials, create a .env file in the project root:
Add the following content (replace with actual credentials):
LINKEDIN_EMAIL=your-email@example.com
LINKEDIN_PASSWORD=your-secure-password

📝 Notes

If login fails, verify your credentials in .env.

Make sure your LinkedIn account has no CAPTCHA or multi-factor authentication enabled, or use cookies for session-based login.

🤝 Contributions

Feel free to fork this repo and contribute! Pull requests are welcome.

