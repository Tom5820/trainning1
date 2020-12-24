import shopify
import requests
import csv
import json


API_KEY ='e5123d4bacd76fe99e576b44964c481b'
PASSWORD ='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'
shop_url = "https://%s:%s@nhl58.myshopify.com/admin/api/2020-10/customers.json" % (API_KEY, PASSWORD)
response = requests.get(shop_url)
data_json = response.json()
f = csv.writer(open("test.csv", "w"))

for x in data_json["customers"]:
    f.writerow([x["id"],
                x["email"],
                x["accepts_marketing"],
                x["created_at"],
                x["updated_at"],
                x["first_name"],
                x["last_name"],
                x["orders_count"],
                x["state"],
                x["total_spent"],
                x["last_order_id"],
                x["note"],
                x["verified_email"],
                x["multipass_identifier"],
                x["tax_exempt"],
                x["phone"],
                x["tags"],
                x["last_order_name"],
                x["currency"]
                 ])
