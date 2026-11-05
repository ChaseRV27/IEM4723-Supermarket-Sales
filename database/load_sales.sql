
INSERT INTO sales (
    invoice_id,
    branch_id,
    customer_type,
    gender,
    product_line,
    unit_price,
    quantity,
    tax_5_percent,
    sales,
    sale_date,
    sale_time,
    payment,
    cogs,
    gross_margin_percentage,
    gross_income,
    rating
)
SELECT
    invoice_id,
    branch,
    customer_type,
    gender,
    product_line,
    CAST(unit_price AS NUMERIC(10,2)),
    CAST(quantity AS INTEGER),
    CAST(tax_5_percent AS NUMERIC(12,4)),
    CAST(sales AS NUMERIC(12,4)),
    TO_DATE(sale_date, 'MM/DD/YYYY'),
    CAST(sale_time AS TIME),
    payment,
    CAST(cogs AS NUMERIC(12,2)),
    CAST(gross_margin_percentage AS NUMERIC(12,9)),
    CAST(gross_income AS NUMERIC(12,4)),
    CAST(rating AS NUMERIC(3,1))
FROM sales_import;
