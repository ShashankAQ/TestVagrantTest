#Shashank A
#Number:9900024141
#Mail:Shashankashok94@gmail.com
#year of passing:2024

def calculate_gst(unit_price, gst_rate, quantity):
    return (unit_price * gst_rate / 100) * quantity



def calculate_total_amount(price, gst, quantity):
    return (price + gst) * quantity
#utilizing dictionaries to establish relations
products = [
    {"name": "leather Walet", "price": 1100, "gst": 18, "quantity": 1},
    {"name": "umbrella", "price": 900, "gst": 12, "quantity": 4},
    {"name": "cigarette", "price": 200, "gst": 28, "quantity": 3},
    {"name": "honey", "price": 100, "gst": 0, "quantity": 2}
]


max_gst_product = 0
max_gst_amount = 0
total_payment = 0

for i in products:
    gst_amount = calculate_gst(i["price"], i["gst"], i["quantity"])
    total_amount = calculate_total_amount(i["price"], gst_amount, i["quantity"])

    total_payment = total_payment+ total_amount

    if gst_amount >max_gst_amount:
        max_gst_amount=gst_amount
        max_gst_product=i["name"]


print("product with maximum gst:", max_gst_product)
print("Maximum GST Amount:", max_gst_amount)
print("Total :", total_payment)








