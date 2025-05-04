import pandas as pd
import faker
import random
from datetime import datetime
import json

def generate_csv(sensitivity):
    fake = faker.Faker("en_AU")
    data = []
    num_rows = random.randint(50, 500)  # Random number of rows between 50 and 500

    # Map sensitivity levels
    sensitivity_map = {
        "1": "Low",
        "2": "Medium",
        "3": "High",
        "4": "Mixed"
    }
    sensitivity_label = sensitivity_map.get(str(sensitivity), "Unknown")

    # Generate a unique file name with timestamp and sensitivity level
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"dummy_data_{sensitivity_label}_{timestamp}.csv"

    for _ in range(num_rows):
        row = {}

        # Low sensitivity data
        row["Name"] = fake.name()
        row["Email"] = fake.email()

        if sensitivity_label in ["Medium", "High", "Mixed"]:
            row["Phone"] = fake.phone_number()
            row["Address"] = fake.address()

        if sensitivity_label in ["High", "Mixed"]:
            row["Date of Birth"] = fake.date_of_birth(minimum_age=18, maximum_age=90)
            # Faker doesn't generate Australian Medicare or TFN numbers, so we can fake an SSN for now
            row["SSN"] = fake.ssn()

        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)

def generate_json(sensitivity):
    fake = faker.Faker("en_AU")
    data = []
    num_records = random.randint(10, 50)  # Random number of user profiles per file

    # Sensitivity mapping
    sensitivity_map = {
        "1": "Low",
        "2": "Medium",
        "3": "High",
        "4": "Mixed"
    }
    sensitivity_label = sensitivity_map.get(str(sensitivity), "Unknown")

    # Unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"dummy_data_{sensitivity_label}_{timestamp}.json"

    for _ in range(num_records):
        profile = {
            "user_id": fake.uuid4(),
            "profile": {
                "name": fake.name(),
                "email": fake.email()
            },
            "preferences": {
                "language": fake.language_name(),
                "timezone": "Australia/Melbourne",
                "marketing_opt_in": fake.boolean()
            },
            "account": {
                "created_at": fake.date_time_between(start_date='-5y', end_date='now').isoformat(),
                "last_login": fake.date_time_between(start_date='-30d', end_date='now').isoformat(),
                "account_status": random.choice(["active", "suspended", "closed"])
            }
        }

        # Add Medium sensitivity fields
        if sensitivity_label in ["Medium", "High", "Mixed"]:
            profile["profile"]["phone"] = fake.phone_number()
            profile["profile"]["address"] = fake.address()

        # Add High sensitivity fields
        if sensitivity_label in ["High", "Mixed"]:
            profile["profile"]["dob"] = str(fake.date_of_birth(minimum_age=18, maximum_age=90))
            profile["account"]["api_key"] = f"AKIA{fake.random_number(digits=16, fix_len=True)}"
            profile["account"]["ssn"] = fake.ssn()

        data.append(profile)

    # Save JSON to file
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ JSON file created: {file_name}")