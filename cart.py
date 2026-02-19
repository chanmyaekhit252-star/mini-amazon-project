from storage import load_data, save_data
from products import get_product

CARTS_FILE = "carts.json"

def view_cart(username):
    carts = load_data(CARTS_FILE, {})
    cart = carts.get(username, [])

    total = 0
    for item in cart:
        subtotal = item["qty"] * item["price"]
        total += subtotal
        print(item["name"], item["qty"], "x", item["price"], "=", subtotal)

    print("Total:", total)

def add_to_cart(username):
    carts = load_data(CARTS_FILE, {})
    cart = carts.get(username, [])

    pid = input("Product ID: ")
    product = get_product(pid)

    if not product:
        print("Product not found.")
        return

    qty = int(input("Quantity: "))
    if qty <= 0 or qty > product["stock"]:
        print("Invalid quantity.")
        return

    cart.append({
        "product_id": pid,
        "name": product["name"],
        "price": product["price"],
        "qty": qty
    })

    carts[username] = cart
    save_data(CARTS_FILE, carts)
    print("Added to cart.")