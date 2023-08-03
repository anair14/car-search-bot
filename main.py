import json
import csv
import time
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S CST")

def main():
    cars_data = []
    while True:
        car_name = input("Enter car name (or 'exit' to stop): ")
        if car_name.lower() == 'exit':
            break
        mileage = float(input("Enter mileage (miles): "))
        price = float(input("Enter price (in USD): "))
        link = input("Enter link: ")
        current_time = get_current_time()
        car_entry = {
            "car_name": car_name,
            "mileage": mileage,
            "price": price,
            "link": link,
            "time": current_time
        }
        cars_data.append(car_entry)
    # Save data to JSON file
    with open('./output/cars_data.json', 'w') as json_file:
        json.dump(cars_data, json_file, indent=4)
    # Save data to CSV file
    csv_columns = ["car_name", "mileage", "price", "link", "time"]
    with open('./output/cars_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        for data in cars_data:
            writer.writerow(data)

if __name__ == "__main__":
    main()