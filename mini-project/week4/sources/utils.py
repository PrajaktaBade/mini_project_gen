
import csv
import os

def clear_screen():
        os.system('clear')

def load_csv(file_name, fieldnames):
    """Load a CSV file as a list of dictionaries."""
    data = []

    # Check if the file exists and is not empty
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        print(f"⚠️ File '{file_name}' is empty or missing. Returning empty list.")
        return data

    with open(file_name, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=fieldnames)
        header = next(reader, None)  # Skip the header row
        if header and set(header.values()) != set(fieldnames):
            # Header row mismatch, fallback to treating it as data
            file.seek(0)  # Go back to beginning
            reader = csv.DictReader(file, fieldnames=fieldnames)
            next(reader)  # Skip the first line manually
        for row in reader:
            data.append(row)
    return data


def save_csv(file_name, fieldnames, data):
    """Save a list of dictionaries to a CSV file with headers."""
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
