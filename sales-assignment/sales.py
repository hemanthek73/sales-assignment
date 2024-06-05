from collections import defaultdict

def read_sales_data(file_path):
    sales_data = []
    with open(file_path, 'r') as file:
        next(file) 
        for line in file:
            date, sku, unit_price, quantity, total_price = line.strip().split(',')
            unit_price = float(unit_price)
            quantity = int(quantity)
            total_price = float(total_price)
            sales_data.append((date, sku, unit_price, quantity, total_price))
    return sales_data

def calculate_total_sales(sales_data):
    total_sales = sum(total_price for _, _, _, _, total_price in sales_data)
    return total_sales

def calculate_monthly_sales(sales_data):
    monthly_sales = defaultdict(float)
    for date, _, _, _, total_price in sales_data:
        month = date[:7]
        monthly_sales[month] += total_price
    return monthly_sales

def calculate_monthly_popular_items(sales_data):
    monthly_items = defaultdict(lambda: defaultdict(int))
    for date, sku, _, quantity, _ in sales_data:
        month = date[:7]
        monthly_items[month][sku] += quantity
      

    monthly_popular_items = {}
    for month, items in monthly_items.items():
        popular_item = max(items, key=items.get)
        monthly_popular_items[month] = (popular_item, items[popular_item])

    return monthly_popular_items

def calculate_monthly_top_revenue_items(sales_data):
    monthly_revenue_items = defaultdict(lambda: defaultdict(float))
    for date, sku, _, _, total_price in sales_data:
        month = date[:7]
        monthly_revenue_items[month][sku] += total_price

    monthly_top_revenue_items = {}
    for month, items in monthly_revenue_items.items():
        top_revenue_item = max(items, key=items.get)
        monthly_top_revenue_items[month] = (top_revenue_item, items[top_revenue_item])

    return monthly_top_revenue_items

def calculate_monthly_popular_item_stats(sales_data, monthly_popular_items):
    monthly_popular_item_stats = {}
    for month, (popular_item, _) in monthly_popular_items.items():
        quantities = [quantity for date, sku, _, quantity, _ in sales_data
                      if date[:7] == month and sku == popular_item]
        min_quantity = min(quantities)
        max_quantity = max(quantities)
        avg_quantity = sum(quantities) / len(quantities)
        monthly_popular_item_stats[month] = (min_quantity, max_quantity, avg_quantity)
    
    return monthly_popular_item_stats

file_path = 'sales-data.txt'
sales_data = read_sales_data(file_path)

total_sales = calculate_total_sales(sales_data)
print("Total sales of the store:", total_sales)

monthly_sales = calculate_monthly_sales(sales_data)
print("Month-wise sales totals:", dict(monthly_sales))

monthly_popular_items = calculate_monthly_popular_items(sales_data)
print("Most popular items in each month:", monthly_popular_items)

monthly_top_revenue_items = calculate_monthly_top_revenue_items(sales_data)
print("Items generating most revenue in each month:", monthly_top_revenue_items)

monthly_popular_item_stats = calculate_monthly_popular_item_stats(sales_data, monthly_popular_items)
print("Min, max, and average number of orders for the most popular item each month:", monthly_popular_item_stats)
