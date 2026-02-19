from storage import load_data, save_data
from products import get_product, update_products
import datetime

ORDERS_FILE = "orders.json"
PRODUCTS_FILE = "products.json"
CARTS_FILE = "carts.json"

def checkout(username):
    carts = load_data(CARTS_FILE, {})
    cart = carts.get(username, [])

    if not cart:
        print("Cart is empty.")
        return

    products = load_data(PRODUCTS_FILE, [])
    total = 0

    for item in cart:
        total += item["qty"] * item["price"]

    order = {
        "order_id": "O" + str(len(load_data(ORDERS_FILE, [])) + 1),
        "username": username,
        "items": cart,
        "total": total,
        "timestamp": str(datetime.datetime.now())
    }

    orders = load_data(ORDERS_FILE, [])
    orders.append(order)
    save_data(ORDERS_FILE, orders)

    carts[username] = []
    save_data(CARTS_FILE, carts)

    print("Order placed. Total:", total)

def view_orders(username):
    orders = load_data(ORDERS_FILE, [])
    for o in orders:
        if o["username"] == username:
            print(o)