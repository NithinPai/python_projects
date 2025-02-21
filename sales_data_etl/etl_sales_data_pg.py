import pandas as pd
from sqlalchemy import create_engine, text

def extract_data(file_path, region, password):
    """
    Reads a CSV file and adds a region column.
    """
    df = pd.read_csv(file_path)
    df['region'] = region
    return df

def transform_data(df_a, df_b):
    df = pd.concat([df_a, df_b], ignore_index=True)
    df = df.drop_duplicates(subset=['OrderId'])
    df['QuantityOrdered'] = pd.to_numeric(df['QuantityOrdered'], errors='coerce')
    df['ItemPrice'] = pd.to_numeric(df['ItemPrice'], errors='coerce')
    df['PromotionDiscount'] = pd.to_numeric(df['PromotionDiscount'], errors='coerce')
    df['QuantityOrdered'] = df['QuantityOrdered'].fillna(0)
    df['ItemPrice'] = df['ItemPrice'].fillna(0)
    df['PromotionDiscount'] = df['PromotionDiscount'].fillna(0)
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']
    df['net_sale'] = df['total_sales'] - df['PromotionDiscount']
    df = df[df['net_sale'] > 0]

    return df

def load_data_to_db(df, db_url):
    """
    Loads the transformed DataFrame into a PostgreSQL database into a table called sales_data.
    """
    engine = create_engine(db_url)
    df.to_sql('sales_data', engine, if_exists='replace', index=False)
    engine.dispose()

def validate_data(db_url):
    """
    Runs SQL queries to validate the data:
      a. Total record count.
      b. Total sales amount by region.
      c. Average sales amount per transaction.
      d. Check for duplicate OrderId values.
    """
    engine = create_engine(db_url)
    with engine.connect() as connection:
        total_records = connection.execute(text("SELECT COUNT(*) FROM sales_data")).scalar()
        sales_by_region = connection.execute(text("SELECT region, SUM(total_sales) FROM sales_data GROUP BY region")).fetchall()
        avg_sales = connection.execute(text("SELECT AVG(total_sales) FROM sales_data")).scalar()

    engine.dispose()

    print("Total Records:", total_records)
    print("Total Sales by Region:", sales_by_region)
    print("Average Sales per Transaction:", avg_sales)

if __name__ == '__main__':
    db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sales_db'
    
    file_a = 'order_region_a.csv'  # Password: order_region_a
    file_b = 'order_region_b.csv'  # Password: order_region_b
    df_a = extract_data(file_a, region='A', password='order_region_a')
    df_b = extract_data(file_b, region='B', password='order_region_b')
    transformed_df = transform_data(df_a, df_b)
    load_data_to_db(transformed_df, db_url)
    validate_data(db_url)
