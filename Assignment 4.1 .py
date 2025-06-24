import csv

data = [
    ["name", "address", "mobile", "email"],
    ["Amit", "Delhi", "9876543210", "amit@example.com"],
    ["Neha", "Mumbai", "9123456789", "neha@example.com"],
    ["Rohit", "Bangalore", "9012345678", "rohit@example.com"],
    ["Simran", "Chennai", "9988776655", "simran@example.com"]
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'data.csv' created successfully.")
