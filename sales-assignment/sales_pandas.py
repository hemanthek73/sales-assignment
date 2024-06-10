import pandas as pd
#file path
file_path = './sales-data.txt' 
sales_data = pd.read_csv(file_path, sep=",")

# Convert 'Date' column to datetime,
# because the date in a data set is in string format performing date-based calculations, require the dates to be in a datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# total sales in a store
total_sales = sales_data['Total Price'].sum()
print(f"Total Sales: {total_sales}")

# Calculate month-wise sales totals
sales_data['Month'] = sales_data['Date'].dt.to_period('M')
#group by method creates a group for each month, and the sum method calculates the total sales for each group
monthly_sales = sales_data.groupby('Month')['Total Price'].sum()
print("\nMonth-wise Sales Totals:")
print(monthly_sales)

# to find the most quantity item sales
most_popular_items = sales_data.groupby(['Month', 'SKU'])['Quantity'].sum().reset_index()
most_popular_items = most_popular_items.loc[most_popular_items.groupby('Month')['Quantity'].idxmax()]
print("\nMost Popular Item Each Month:")
print(most_popular_items[['Month', 'SKU', 'Quantity']])

# to find most revenue items
most_revenue_items = sales_data.groupby(['Month', 'SKU'])['Total Price'].sum().reset_index()
most_revenue_items = most_revenue_items.loc[most_revenue_items.groupby('Month')['Total Price'].idxmax()]
print("\nItems Generating Most Revenue Each Month:")
print(most_revenue_items[['Month', 'SKU', 'Total Price']])

# For the most popular item, find the min, max, and average number of orders each month
popular_items_orders = sales_data[sales_data.set_index(['Month', 'SKU']).index.isin(most_popular_items.set_index(['Month', 'SKU']).index)]
orders_stats = popular_items_orders.groupby(['Month', 'SKU'])['Quantity'].agg(['min', 'max', 'mean']).reset_index()
print("\nMin, Max, and Average Orders of Most Popular Item Each Month:")
print(orders_stats)

# for generating csv files
monthly_sales.to_csv('monthly_sales.csv')
most_popular_items.to_csv('most_popular_items.csv')
most_revenue_items.to_csv('most_revenue_items.csv')
orders_stats.to_csv('orders_stats.csv')
