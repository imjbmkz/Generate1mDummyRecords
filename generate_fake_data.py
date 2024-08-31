import json
from datetime import datetime
from sys import argv
from pathlib import Path
from shutil import rmtree
from faker import Faker
from tqdm import tqdm

if __name__=="__main__":

    # Some logs
    start_time = datetime.now()
    print(f"{start_time}: App has started")

    # Control the number of records
    if len(argv)>=2:
        records = int(argv[1])
    else:
        records = 500_000

    # Delete existing folder with dummy files
    folder = Path("files")
    if folder.is_dir():
        rmtree(folder)

    # Recreate the folder 
    folder.mkdir(exist_ok=True)

    fake = Faker()

    # Generate 500k fake records
    for i in tqdm(range(1,records + 1)):

        # Dictionary of fake data
        fake_data = {
            # Identity
            "id": i,
            "full_name": fake.name(),
            "ssn": fake.ssn(),
            "dob": fake.date_of_birth().strftime("%Y-%m-%d"),
            
            # Contact details
            "email": fake.email(),
            "phone": fake.phone_number(),
            
            # Location
            "address": fake.address(),
            "city": fake.city(),
            "state": fake.state(),
            "zipcode": fake.zipcode(),
            "country": fake.country(),
        }

        with open(folder / f"{i}.json", "w") as fp:
            json.dump(fake_data, fp)

    # Some logs
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"{end_time}: App has ended. Runtime: {duration}")