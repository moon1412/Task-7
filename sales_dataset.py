import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# Step 2: Write SQL query to get total quantity and revenue by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Step 3: Load query result into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Close the database connection
conn.close()

# Step 5: Print the results
print("Sales Summary:")
print(df)

# Step 6: Plot bar chart (Revenue by Product)
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save the chart as an image file
plt.show()
