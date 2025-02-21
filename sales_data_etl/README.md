## Project 1: Sales Data ETL

### Overview
- Combines sales data from two regions.
- Transforms data by calculating `total_sales` and `net_sale`, adding a region identifier, removing duplicates, and filtering invalid orders.
- Loads the cleaned data into a PostgreSQL database.
- Validates the data using SQL queries.

### Files
- `etl_sales_data_pg.py` – Python script for ETL operations.
- `order_region_a.csv` – Sales data for Region A.
- `order_region_b.csv` – Sales data for Region B.

### How to Run
1. **Install Dependencies:**
- pip install -r requirements.txt
2. **Set Up PostgreSQL:**
- Create a database (e.g., `sales_db`) in PostgreSQL.
- Update the connection string in `etl_sales_data_pg.py` accordingly.
3. **Place the CSV Files:**
- Ensure the CSV files are in the same directory as the script.
4. **Run the Script:**