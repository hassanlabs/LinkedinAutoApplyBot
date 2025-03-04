from login import login_with_session
from playwright.sync_api import sync_playwright


def search_jobs(page):
    """Search for jobs on LinkedIn and attempt to apply if 'Easy Apply' is available."""

    # Navigate to LinkedIn job search
    page.goto("https://www.linkedin.com/jobs/search/")
    page.wait_for_load_state("load")

    job_title = input("Enter job title or keyword: ").strip()
    location = input("Enter job location: ").strip()

    page.fill('[id*="jobs-search-box-keyword-id"]', job_title)
    page.fill('[id*="jobs-search-box-location-id"]', location)

    page.click('[class*="jobs-search-box__submit-button"]')

    print(f"🔍 Searching for jobs: {job_title} in {location}...")

    page.wait_for_load_state("load")

    job_cards = page.query_selector_all('[class*="job-card-list__entity-lockup"]')
    print(f"✅ Found {len(job_cards)} job listings.")

    for idx, job in enumerate(job_cards[:5]):  # Show first 5 jobs
        try:
            # job.click()  # Click the job listing
            # page.wait_for_timeout(2000)  # Allow job details to load

            title = job.query_selector('[class*="artdeco-entity-lockup__title"]')
            company = job.query_selector('[class*="artdeco-entity-lockup__subtitle"]')

            job_title_text = title.inner_text() if title else 'No title'
            company_text = company.inner_text() if company else 'No company'

            print(f"{idx + 1}. {job_title_text} at {company_text}")

            # Check for Easy Apply button
            easy_apply_button = page.query_selector('[aria-label*="Easy Apply to"]')
            if easy_apply_button:
                print(f"🟢 Found 'Easy Apply' for: {job_title_text}. Clicking...")
                # easy_apply_button.click()
                page.wait_for_timeout(3000)  # Wait for Easy Apply modal to open
            else:
                print(f"❌ No 'Easy Apply' option for {job_title_text}. Skipping...")

        except Exception as e:
            print(f"⚠️ Error processing job {idx+1}: {e}")


with sync_playwright() as p:  # Keep Playwright open
    browser, context, page = login_with_session(p)
    search_jobs(page)
    browser.close()  # Close browser after script finishes
