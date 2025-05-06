import pandas as pd
import faker as faker
from console_ui import *
from file_generation import DummyDataGenerator

# Entry point of the script
file_types, sensitivity, count = console_ui()

# Create an instance of DummyDataGenerator
generator = DummyDataGenerator(sensitivity)

# Generate test file
generator.generate_csv()