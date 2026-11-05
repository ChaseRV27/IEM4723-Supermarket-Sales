
# Database

This folder contains the PostgreSQL database files for the Supermarket Sales Analytics System.

The PostgreSQL database has been created, and 1,000 supermarket sales transactions have been successfully imported and verified.

## Planned Files

- `schema.sql` — Defines the supermarket sales database table.
- `README.md` — Documents the database setup and development progress.

## Current Status

The PostgreSQL database has been created and is running
inside a Docker container.

Completed database work:
- Created the branches table.
- Created the sales table with primary and foreign keys.
- Created the sales_import table for importing CSV data.
- Imported 1,000 supermarket sales records.
- Verified that all 1,000 transactions are stored in
  the sales table.

Database files:
- schema.sql - Creates the branches and sales tables.
- import.sql - Creates the temporary import table.
- load_sales.sql - Transfers data into the sales table.

Remaining work:
- Document how teammates can set up PostgreSQL.
- Connect PostgreSQL to the Streamlit dashboard.
- Test the complete database and dashboard system.
- Complete final project documentation.

## PostgreSQL Connection Information

Database name: supermarket_sales
Database user: supermarket_user
Docker container: supermarket-postgres
Host: localhost
Port: 5433

## Database Tables

- branches: Stores branch names and cities.
- sales: Stores 1,000 supermarket transactions.
- sales_import: Holds the original imported CSV data.

## Dashboard Integration

The Streamlit dashboard currently reads directly
from the CSV file.

The PostgreSQL database has been created and tested,
but it has not yet been connected to Streamlit.

The database currently runs locally on my computer.
Other team members will need their own PostgreSQL
container or a shared database connection.

Database passwords should not be uploaded to GitHub.


## How to Set Up PostgreSQL

1. Install and open Docker Desktop.
2. Open the supermarket sales project in VS Code.
3. Open a PowerShell terminal.
4. Run the following command to create the PostgreSQL container:

```powershell
docker run --name supermarket-postgres -e POSTGRES_USER=supermarket_user -e POSTGRES_PASSWORD=YOUR_PRIVATE_PASSWORD -e POSTGRES_DB=supermarket_sales -p 5433:5432 -v supermarket_pgdata:/var/lib/postgresql/data -d postgres:17
```

Replace YOUR_PRIVATE_PASSWORD with a private password.
Do not upload passwords to GitHub.

This command is only needed once when creating the container.

To start an existing container:

```powershell
docker start supermarket-postgres
```

To verify PostgreSQL is running:

```powershell
docker ps --filter "name=supermarket-postgres"
```

The database tables and sales data must be loaded separately using the SQL files in this folder.


## Creating the Database Tables

Open PowerShell in the main project folder.

Run the following command to create the branches
and sales tables:

```powershell
Get-Content -Raw .\database\schema.sql | docker exec -i supermarket-postgres psql -U supermarket_user -d supermarket_sales -v ON_ERROR_STOP=1
```

Create the CSV import table:

```powershell
Get-Content -Raw .\database\import.sql | docker exec -i supermarket-postgres psql -U supermarket_user -d supermarket_sales -v ON_ERROR_STOP=1
```

## Importing the Supermarket Sales Data

First, add the three supermarket branches:

```powershell
docker exec supermarket-postgres psql -U supermarket_user -d supermarket_sales -c "INSERT INTO branches (branch_id, city) VALUES ('Alex', 'Yangon'), ('Cairo', 'Mandalay'), ('Giza', 'Naypyitaw');"
```

Copy the CSV file into the Docker container:

```powershell
docker cp "data\SuperMarket Analysis.csv" supermarket-postgres:/tmp/supermarket.csv
```

Import the CSV into the sales_import table:

```powershell
docker exec supermarket-postgres psql -U supermarket_user -d supermarket_sales -c "COPY sales_import FROM '/tmp/supermarket.csv' WITH (FORMAT csv, HEADER true);"
```

Transfer the imported records into the sales table:

```powershell
Get-Content -Raw .\database\load_sales.sql | docker exec -i supermarket-postgres psql -U supermarket_user -d supermarket_sales -v ON_ERROR_STOP=1
```

## Verifying the Database

Check the number of transactions:

```powershell
docker exec supermarket-postgres psql -U supermarket_user -d supermarket_sales -c "SELECT COUNT(*) FROM sales;"
```

Expected result: 1000 transactions.

These setup and import commands are intended for
a new, empty database. Do not repeat the import
on a database that already contains the sales records.

