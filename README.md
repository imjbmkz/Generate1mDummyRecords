# Fake Data Generator

This script generates a specified number of fake records and saves each record as a JSON file in a designated folder. It uses the `Faker` library to create realistic-looking data.

## Features

- Generates fake identity, contact details, and location data.
- Saves each record as a separate JSON file.
- Deletes any existing folder with dummy files before creating new ones.
- Allows control over the number of records generated via command-line arguments.

## Requirements

- Python 3.x
- `Faker` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Create and activate virtual environment.
  ```sh
  python -m venv env
  source env/Scripts/activate
  ```
3. Install the required packages from file:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Clone the repository or download the script.
2. Run the script from the command line:

    ```sh
    python generate_fake_data.py [number_of_records]
    ```

    - `number_of_records` (optional): The number of fake records to generate. Defaults to 1,000,000 if not specified.
3. Run using Docker.
  ```sh
  docker build -t pydatagen .
  docker run pydatagen
  ```

## Example

To generate 100,000 fake records:

```sh
python generate_fake_data.py 100000
```

## Data Generated

Each record generated by the script includes the following fields:

- **Identity**
  - `id`: A unique identifier for the record.
  - `full_name`: A randomly generated full name.
  - `ssn`: A randomly generated Social Security Number.
  - `dob`: A randomly generated date of birth in the format `YYYY-MM-DD`.

- **Contact Details**
  - `email`: A randomly generated email address.
  - `phone`: A randomly generated phone number.

- **Location**
  - `address`: A randomly generated street address.
  - `city`: A randomly generated city name.
  - `state`: A randomly generated state name.
  - `zipcode`: A randomly generated ZIP code.
  - `country`: A randomly generated country name.

## Script Details

The script performs the following steps:

1. **Control the Number of Records**: Checks if a number of records is provided as a command-line argument. If not, defaults to 1,000,000 records.
2. **Delete Existing Folder**: Deletes the existing `files` folder if it exists.
3. **Recreate the Folder**: Creates a new `files` folder.
4. **Generate Fake Data**: Uses the `Faker` library to generate fake data for each record, including identity, contact details, and location.
5. **Save Data**: Saves each record as a JSON file in the `files` folder.

## Dependencies

- `json`: For handling JSON data.
- `sys`: For accessing command-line arguments.
- `pathlib`: For handling file paths.
- `shutil`: For removing directories.
- `Faker`: For generating fake data.
- `tqdm`: For displaying a progress bar.

## License

This project is licensed under the MIT License.
