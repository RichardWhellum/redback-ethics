import pandas as pd
import faker
import random
from datetime import datetime
import json
from docx import Document
from fpdf import FPDF

class DummyDataGenerator:
    def __init__(self, sensitivity):
        self.sensitivity = str(sensitivity)
        self.fake = faker.Faker("en_AU")
        self.sensitivity_map = {
            "1": "Low",
            "2": "Medium",
            "3": "High",
            "4": "Mixed"
        }
        self.sensitivity_label = self.sensitivity_map.get(self.sensitivity, "Unknown")

    def get_sensitive_data(self):
        if self.fake.boolean():
            if self.sensitivity_label == "Low":
                return f"Name: {self.fake.name()}, Email: {self.fake.email()}"
            elif self.sensitivity_label == "Medium":
                return f"Phone: {self.fake.phone_number()}, Address: {self.fake.address()}"
            elif self.sensitivity_label == "High":
                return f"SSN: {self.fake.ssn()}, Credit Card: {self.fake.credit_card_number()}"
            elif self.sensitivity_label == "Mixed":
                return (f"Name: {self.fake.name()}, Phone: {self.fake.phone_number()}, "
                        f"Address: {self.fake.address()}, SSN: {self.fake.ssn()}")
        return None

    def generate_csv(self):
        data = []
        num_rows = random.randint(50, 500)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"dummy_data_{self.sensitivity_label}_{timestamp}.csv"

        for _ in range(num_rows):
            row = {
                "Name": self.fake.name(),
                "Email": self.fake.email()
            }
            if self.sensitivity_label in ["Medium", "High", "Mixed"]:
                row["Phone"] = self.fake.phone_number()
                row["Address"] = self.fake.address()
            if self.sensitivity_label in ["High", "Mixed"]:
                row["Date of Birth"] = self.fake.date_of_birth(minimum_age=18, maximum_age=90)
                row["SSN"] = self.fake.ssn()

            data.append(row)

        pd.DataFrame(data).to_csv(file_name, index=False)
        print(f"✅ CSV generated: {file_name}")

    def generate_json(self):
        data = []
        num_records = random.randint(10, 50)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"dummy_data_{self.sensitivity_label}_{timestamp}.json"

        for _ in range(num_records):
            profile = {
                "user_id": self.fake.uuid4(),
                "profile": {
                    "name": self.fake.name(),
                    "email": self.fake.email()
                },
                "preferences": {
                    "language": self.fake.language_name(),
                    "timezone": "Australia/Melbourne",
                    "marketing_opt_in": self.fake.boolean()
                },
                "account": {
                    "created_at": self.fake.date_time_between(start_date='-5y', end_date='now').isoformat(),
                    "last_login": self.fake.date_time_between(start_date='-30d', end_date='now').isoformat(),
                    "account_status": random.choice(["active", "suspended", "closed"])
                }
            }

            if self.sensitivity_label in ["Medium", "High", "Mixed"]:
                profile["profile"]["phone"] = self.fake.phone_number()
                profile["profile"]["address"] = self.fake.address()
            if self.sensitivity_label in ["High", "Mixed"]:
                profile["profile"]["dob"] = str(self.fake.date_of_birth(minimum_age=18, maximum_age=90))
                profile["account"]["api_key"] = f"AKIA{self.fake.random_number(digits=16, fix_len=True)}"
                profile["account"]["ssn"] = self.fake.ssn()

            data.append(profile)

        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

        print(f"✅ JSON generated: {file_name}")

    def generate_txt(self):
        num_paragraphs = random.randint(5, 20)
        paragraphs = []

        for _ in range(num_paragraphs):
            paragraphs.append(self.fake.paragraph(nb_sentences=20))
            sensitive = self.get_sensitive_data()
            if sensitive:
                paragraphs.append(sensitive)

        text_content = "\n\n".join(paragraphs)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"generated_text_{self.sensitivity}_{timestamp}.txt"

        with open(file_name, "w") as file:
            file.write(text_content)

        print(f"✅ Text file generated: {file_name}")

    def generate_docx(self):
        num_paragraphs = random.randint(5, 20)
        doc = Document()

        for _ in range(num_paragraphs):
            doc.add_paragraph(self.fake.paragraph(nb_sentences=20))
            sensitive = self.get_sensitive_data()
            if sensitive:
                doc.add_paragraph(sensitive)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"generated_docx_{self.sensitivity}_{timestamp}.docx"
        doc.save(file_name)

        print(f"✅ Word document generated: {file_name}")

    def generate_pdf(self):
        num_paragraphs = random.randint(5, 20)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        page_width = pdf.w - 2 * pdf.l_margin  # Calculate usable page width

        for _ in range(num_paragraphs):
            paragraph = self.fake.paragraph(nb_sentences=20)
            pdf.set_x(pdf.l_margin)  # Reset X position to the left margin
            pdf.multi_cell(page_width, 10, paragraph, align="L")  # Align text to the left
            sensitive = self.get_sensitive_data()
            if isinstance(sensitive, str) and sensitive.strip():
                pdf.set_x(pdf.l_margin)  # Reset X position for sensitive data
                pdf.multi_cell(page_width, 10, sensitive, align="L")  # Align sensitive data to the left
            pdf.ln(5)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_file = f"generated_pdf_{self.sensitivity}_{timestamp}.pdf"
        pdf.output(pdf_file)

        print(f"✅ PDF generated: {pdf_file}")