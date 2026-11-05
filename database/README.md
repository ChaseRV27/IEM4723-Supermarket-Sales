
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
- Complete database documentation and additional testing.
- Connect the PostgreSQL database to the Streamlit dashboard.
- Commit and push database files to GitHub.
