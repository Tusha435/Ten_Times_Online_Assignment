# PostgreSQL to CSV Exporter

This is a simple Python script that connects to a PostgreSQL database and exports table data to a CSV file using the `psycopg2` library.

## Features

- Connects to a PostgreSQL database
- Exports all records from a specified table into a CSV file
- Automatically includes column headers in the CSV output

## Prerequisites

Before using this script, ensure that you have the following installed:

- Python 3.x
- PostgreSQL
- `psycopg2` Python package

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/postgresql-csv-exporter.git
   cd postgresql-csv-exporter
Create a Virtual Environment (Optional but Recommended):

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
Install Required Dependencies:

Install psycopg2 and any other dependencies listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can install psycopg2 manually:

bash
Copy code
pip install psycopg2
Usage
Edit Database Configuration:

Open the script and modify the database connection details in the psycopg2.connect() function:

python
Copy code
connection = psycopg2.connect(
    database="newsdb",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
Run the Script:

Run the script to export the data from the PostgreSQL table to a CSV file:

bash
Copy code
python export_to_csv.py
CSV Output:

After running the script, a CSV file named output.csv will be generated in the project directory. The file will contain all the data from the specified table, with the first row representing column headers.

Example
bash
Copy code
$ python export_to_csv.py
Data successfully exported to 'output.csv'
