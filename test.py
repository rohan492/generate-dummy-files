import random
import json
import csv
from typing import List, Dict, Tuple

def generate_name() -> Tuple[str, str]:
    first_names = [
        "James", "Oliver", "William", "Elijah", "Lucas", "Mason", "Liam", "Noah",
        "Benjamin", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella",
        "Mia", "Evelyn", "Harper", "Olivia", "Logan"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
        "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
        "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
    ]
    return random.choice(first_names), random.choice(last_names)

def generate_email(first_name: str, last_name: str) -> str:
    domains = [
        "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com",
        "protonmail.com", "fastmail.com", "zoho.com", "aol.com", "mail.com",
        "enterprise.co", "techcorp.net", "corporate.io", "company.com",
        "businessmail.org"
    ]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

def generate_job_title() -> str:
    titles = [
        "Software Engineer", "Data Analyst", "Product Manager", "Project Manager",
        "Marketing Specialist", "Business Analyst", "Account Executive",
        "Sales Director", "UX Designer", "DevOps Engineer"
    ]
    return random.choice(titles)

def generate_company() -> str:
    companies = [
        "Digital Dynamics", "Tech Solutions Inc.", "Global Innovations",
        "Smart Technologies", "Future Systems"
    ]
    return random.choice(companies)

def generate_country() -> str:
    countries = [
        "United States", "United Kingdom", "Canada", "Australia", "Germany",
        "France", "Japan", "Singapore"
    ]
    return random.choice(countries)

def generate_linkedin_url(first_name: str, last_name: str) -> str:
    random_number = random.randint(100, 999)
    return f"https://www.linkedin.com/in/{first_name.lower()}-{last_name.lower()}-{random_number}/"

def generate_google_ad_id() -> str:
    return f"GA{random.randint(1000000000, 9999999999)}"

def generate_records(count: int) -> Tuple[List[Dict], List[Dict]]:
    basic_records = []
    enriched_records = []
    
    start_key = 101  # Starting after the existing 100 records
    
    for i in range(count):
        first_name, last_name = generate_name()
        email = generate_email(first_name, last_name)
        
        # Basic record
        basic_record = {
            "firstname": first_name,
            "lastname": last_name,
            "email": email
        }
        
        # Enriched record
        enriched_record = {
            "key": start_key + i,
            "email": email,
            "firstname": first_name,
            "lastname": last_name,
            "jobtitle": generate_job_title(),
            "employeecompany": generate_company(),
            "country": generate_country(),
            "linkedin_url": generate_linkedin_url(first_name, last_name),
            "googleaid": generate_google_ad_id()
        }
        
        basic_records.append(basic_record)
        enriched_records.append(enriched_record)
    
    return basic_records, enriched_records

# Generate 400 new records
basic_records, enriched_records = generate_records(400)

# Save basic records to CSV
with open('Basic_Data_Extended.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['firstname', 'lastname', 'email'])
    writer.writeheader()
    # Write existing records (assuming they're needed)
    # writer.writerows(existing_basic_records)
    writer.writerows(basic_records)

# Save enriched records to JSON
enriched_data = {
    "headers": [
        {"key": 1, "dataIndex": "email", "label": "email", "title": "Email Address", "value": "email"},
        {"key": 2, "dataIndex": "firstname", "label": "firstname", "title": "First Name", "value": "firstname"},
        {"key": 3, "dataIndex": "lastname", "label": "lastname", "title": "Last Name", "value": "lastname"},
        {"key": 4, "dataIndex": "jobtitle", "label": "jobtitle", "title": "Job Title", "value": "jobtitle"},
        {"key": 5, "dataIndex": "employeecompany", "label": "employeecompany", "title": "Company", "value": "employeecompany"},
        {"key": 6, "dataIndex": "country", "label": "country", "title": "Country", "value": "country"},
        {"key": 7, "dataIndex": "linkedin_url", "label": "linkedin_url", "title": "LinkedIn Profile", "value": "linkedin_url"},
        {"key": 8, "dataIndex": "googleaid", "label": "googleaid", "title": "Google Ad ID", "value": "googleaid"}
    ],
    "data": enriched_records
}

with open('Enriched_Data_Extended.json', 'w') as f:
    json.dump(enriched_data, f, indent=2)

print(f"Generated {len(basic_records)} new records")
print("Files saved as 'Basic_Data_Extended.csv' and 'Enriched_Data_Extended.json'")