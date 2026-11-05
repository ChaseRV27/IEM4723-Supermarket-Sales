# Supermarket Sales Dataset

## Source and purpose

- Dataset: Supermarket Sales Dataset
- Source: https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales
- CSV file: `SuperMarket Analysis.csv`
- Project: Supermarket Sales Analytics System
- Team: ZAC Analysts
- Dataset inspection and documentation: Zachary Pontikes

The dataset records supermarket transactions with store, customer,
product, pricing, payment, date, time, and customer-rating information.

## Verified dataset characteristics

The downloaded CSV was inspected in Excel.

- Transaction rows: 1,000, excluding the header.
- Columns: 17.
- Earliest transaction date: January 1, 2019.
- Latest transaction date: March 30, 2019.
- All 1,000 Date entries were numeric in Excel.

### Branches and cities

Three distinct branch-city pairs were found:

| Branch | City |
|---|---|
| Alex | Yangon |
| Cairo | Mandalay |
| Giza | Naypyitaw |

Branch labels are recorded exactly as stored in the CSV.

### Product lines

- Electronic accessories
- Fashion accessories
- Food and beverages
- Health and beauty
- Home and lifestyle
- Sports and travel

## Data quality findings

Checks covered the 1,000 transaction rows in Excel range A2:Q1001.

- Empty cells: 0.
- Empty or ordinary-space-only cells: 0.
- Exact matches for common missing-value labels
  (`N/A`, `NA`, `NULL`, `None`, `Unknown`, and `-`): 0.
  This check ignored capitalization.
- Duplicate invoice IDs beyond their first occurrence: 0.

These checks did not identify missing values using the methods above.
They do not establish that every value is accurate or rule out every
possible missing-value representation.

## Data dictionary

Examples below were observed in the first transaction.
PostgreSQL types are recommendations for schema review.

| Column name | Meaning | Example value | Suggested PostgreSQL type |
|---|---|---|---|
| Invoice ID | Identifier for a sale; unique in the checked records | 750-67-8428 | VARCHAR(20) |
| Branch | Store branch label | Alex | VARCHAR(50) |
| City | City where the store branch is located | Yangon | VARCHAR(50) |
| Customer type | Customer classification | Member | VARCHAR(20) |
| Gender | Customer gender recorded in the dataset | Female | VARCHAR(20) |
| Product line | Category of products purchased | Health and beauty | VARCHAR(100) |
| Unit price | Price per unit of the product | 74.69 | NUMERIC(10,2) |
| Quantity | Number of units purchased | 7 | INTEGER |
| Tax 5% | Transaction tax amount at a 5% rate | 26.1415 | NUMERIC(12,4) |
| Sales | Transaction total including tax | 548.9715 | NUMERIC(12,4) |
| Date | Transaction date | 2019-01-05 | DATE |
| Time | Transaction time of day | 13:08:00 | TIME |
| Payment | Payment method used | Ewallet | VARCHAR(30) |
| cogs | Cost of goods sold as labeled in the source dataset | 522.83 | NUMERIC(12,4) |
| gross margin percentage | Gross margin percentage reported by the source | 4.761905 | NUMERIC(10,6) |
| gross income | Gross income amount reported by the source | 26.1415 | NUMERIC(12,4) |
| Rating | Customer rating recorded for the transaction | 9.1 | NUMERIC(4,2) |

## Import and schema considerations

- The transaction-total column is named `Sales`, not `Total`.
- Several CSV headers contain spaces, mixed capitalization, or `%`.
  PostgreSQL column names must be mapped deliberately during import.
- Preserve invoice IDs as text, including their hyphens.
- Observed tax and sales values contain four decimal places.
  Avoid rounding them to two decimal places during import.
- The first transaction date is January 5, 2019, displayed in Excel
  as `1/5/2019`. Confirm month/day/year parsing during CSV import.
- Excel displayed the first transaction time as `1:08:00 PM`,
  equivalent to `13:08:00`. Confirm the raw CSV time format before import.
- The meanings and calculation rules for `cogs`, `gross income`,
  and `gross margin percentage` should be reviewed before interpreting
  them as business profit measures.
- Inspection formulas were saved in a separate Excel workbook.
  Use the original CSV for database import.

## Planned analysis

- Total sales amount, including tax, using `Sales`.
- Sales by branch.
- Sales by product line.
- Transaction counts by payment method.
- Average customer rating.

## Current status and remaining work

Initial dataset inspection and the data dictionary are complete.
PostgreSQL import and SQL execution have not been verified in this work.

Next steps are to review `database/schema.sql`, align analysis queries
with its table and column names, and test the queries after the database
is available.
