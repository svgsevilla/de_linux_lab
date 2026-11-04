import csv
from pathlib import Path

products = {}

with open("../datasets/products.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products[row["product_id"]] = float(row["unit_price"])

total_revenue = 0

with open("../datasets/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = products[row["product_id"]]
        quantity = int(row["quantity"])

        total_revenue += price * quantity

Path("../output").mkdir(exist_ok=True)

with open("../output/report.txt", "w") as report:
    report.write("Daily Revenue Summary\n")
    report.write("=====================\n")
    report.write(f"Total Revenue: ${total_revenue:,.2f}\n")

print("Transformation completed.")
print(f"Total Revenue: ${total_revenue:,.2f}")