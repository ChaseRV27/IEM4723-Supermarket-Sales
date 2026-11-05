-- Supermarket Sales Analytics System
-- Author: Zachary Pontikes
-- Milestone 1: Initial analysis queries
--
-- Names checked against database/schema.sql.
-- Status: Draft queries; not yet executed or tested.
-- Sales amounts use the sales column, which includes tax.

-- 1. What is the total sales amount, including tax?
SELECT SUM(sales) AS total_sales_including_tax
FROM sales;

-- 2. Which branch generates the most sales?
-- Highest sales appears first; all branches are shown.
SELECT
    branch_id,
    SUM(sales) AS branch_sales_including_tax
FROM sales
GROUP BY branch_id
ORDER BY branch_sales_including_tax DESC, branch_id ASC;

-- 3. Which product line generates the most sales?
-- Highest sales appears first; all product lines are shown.
SELECT
    product_line,
    SUM(sales) AS product_line_sales_including_tax
FROM sales
GROUP BY product_line
ORDER BY product_line_sales_including_tax DESC, product_line ASC;

-- 4. Which payment method is used most frequently?
-- Counts transactions, rather than units purchased.
SELECT
    payment,
    COUNT(*) AS transaction_count
FROM sales
GROUP BY payment
ORDER BY transaction_count DESC, payment ASC;

-- 5. What is the average customer rating across transactions?
SELECT AVG(rating) AS average_customer_rating
FROM sales;
