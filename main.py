# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd
# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")
# View employees table
employee_data = pd.read_sql("""
    SELECT * FROM employees
""", conn)
print("______________________Employee Data_____________________")
print(employee_data)
print("________________________End Employee Data________________")
# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)
print("______________________First Five________________________")
print(df_first_five)
print("______________________End First Five____________________")
# STEP 3
# Reverse the column order
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)
print("______________________Five Reverse______________________")
print(df_five_reverse)
print("______________________End Five Reverse__________________")
# STEP 4
# Rename employeeNumber to ID
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)
print("______________________Alias_____________________________")
print(df_alias)
print("______________________End Alias_________________________")
# STEP 5
# Classify employees by role
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle IN (
                'President',
                'VP Sales',
                'VP Marketing'
            )
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)
print("______________________Executive_________________________")
print(df_executive)
print("______________________End Executive_____________________")
# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)
print("______________________Name Length_______________________")
print(df_name_length)
# STEP 7
# Get the first two letters of each job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)
print("______________________Short Title_______________________")
print(df_short_title)
# STEP 8
# Calculate the sum of rounded total prices
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered))
    AS total_price
    FROM orderDetails
""", conn).values[0]

print(sum_total_price)
# STEP 9
# Extract the day, month, and year from orderDate
df_day_month_year = pd.read_sql("""
    SELECT
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)
print("______________________Day Month Year____________________")
print(df_day_month_year)
# Close the database connection
conn.close()