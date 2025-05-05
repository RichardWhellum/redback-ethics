import pandas as pd
import faker as faker
from console_ui import *
from file_generation import *

# Entry point of the script
file_types, sensitivity, count = console_ui()

fake = faker.Faker("en_AU")
print(fake.paragraph(nb_sentences=10))