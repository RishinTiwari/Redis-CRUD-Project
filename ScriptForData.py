import csv
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

csv_file = 'MergedOrder.csv'

with open(csv_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        order_id = row['Order_ID']
        order_data = {
            'Order_Date': str(row['Order_Date']),
            'CustomerName': row['CustomerName'],
            'State': row['State'],
            'City': row['City'],
            'Amount': row['Amount'],
            'Profit': row['Profit'],
            'Quantity': row['Quantity'],
            'Category': row['Category'],
            'Sub_Category': row['Sub_Category']
        }
        # Serialize the dictionary to a JSON string before storing it in Redis
        order_data_json = json.dumps(order_data)
        r.hset('orders', order_id, order_data_json)
