
CREATE TABLE branches (
    branch_id VARCHAR(20) PRIMARY KEY,
    city VARCHAR(50) NOT NULL
);


CREATE TABLE sales (
    invoice_id VARCHAR(20) PRIMARY KEY,
    branch_id VARCHAR(20) REFERENCES branches(branch_id),
    customer_type VARCHAR(20),
    gender VARCHAR(10),
    product_line VARCHAR(50),
    unit_price NUMERIC(10,2),
    quantity INTEGER,
    tax_5_percent NUMERIC(12,4),
    sales NUMERIC(12,4),
    sale_date DATE,
    sale_time TIME,
    payment VARCHAR(20),
    cogs NUMERIC(12,2),
    gross_margin_percentage NUMERIC(12,9),
    gross_income NUMERIC(12,4),
    rating NUMERIC(3,1)
);


