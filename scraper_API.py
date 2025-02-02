import requests
from bs4 import BeautifulSoup
import csv
import time

# ScraperAPI key
API_KEY = "243934cc1d24728c1f2a3abd7a876136"

# ScraperAPI URL
SCRAPERAPI_URL = "https://api.scraperapi.com/"

def fetch_url(url, retries=3, delay=2):
    """
    Fetches the content of a URL using ScraperAPI with retries.
    """
    params = {
        "api_key": API_KEY,
        "url": url,
        
        
    }
    
    
    for attempt in range(retries):
        try:
            response = requests.get(SCRAPERAPI_URL, params=params, timeout=30)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Attempt {attempt + 1}: Failed to fetch {url} - Status code: {response.status_code}")
                time.sleep(delay)  # Wait before retrying
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}: Error occurred - {e}")
            time.sleep(delay)
    
    return None

def scrape_job_listings():
    """
    Scrapes job listings from Indeed using ScraperAPI.
    """
    base_url = "https://in.indeed.com/jobs?q=&l=Kerala&from=searchOnHP&vjk=9b10a9b4f8f94195"

    job_data = []

    for page in range(3):  # Adjust number of pages to scrape
        start = page * 10
        url = f"{base_url}&start={start}"
        print(f"Scraping page {page + 1}...")

        html_content = fetch_url(url)
        if html_content:
            soup = BeautifulSoup(html_content, "html.parser")
            

            job_cards = soup.find_all("div", class_="job_seen_beacon")

            for job_card in job_cards:
                # Extract job title
                title_tag = job_card.find("h2", class_="jobTitle")
                title = title_tag.text.strip() if title_tag else "N/A"

                # Extract company name
                company_tag = job_card.find("span", {"data-testid": "company-name"})
                company = company_tag.text.strip() if company_tag else "N/A"

                # Extract location
                location_tag = job_card.find("div", {"data-testid": "text-location"})
                location = location_tag.text.strip() if location_tag else "N/A"

                # Extract salary (if available)
                salary_tag = job_card.find("div", {"data-testid": "attribute_snippet_testid"})
                salary = salary_tag.text.strip() if salary_tag else "N/A"

                # Extract job information
                information_tag = job_card.find("div", {"data-testid": "jobsnippet_footer"})
                Information = information_tag.text.strip() if information_tag else "N/A"

                # Append the job data
                job_data.append({
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "salary": salary,
                    "Information": Information
                })
        else:
            print(f"Skipping page {page + 1} due to fetch failure.")

    # Save results to CSV
    save_to_csv(job_data)

def save_to_csv(data):
    """
    Saves job data to a CSV file.
    """
    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Company", "Location", "salary", "Information"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} jobs to jobs.csv")

if __name__ == "__main__":
    print("Starting job scraper...")
    scrape_job_listings()
    print("Scraping completed!")
