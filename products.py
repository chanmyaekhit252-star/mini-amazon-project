from storage import load_data, save_data

PRODUCTS_FILE = "products.json"

def list_products():
    products = load_data(PRODUCTS_FILE, [])
    for p in products:
        print(p["product_id"], p["name"], "$", p["price"], "Stock:", p["stock"])

def search_products():
    products = load_data(PRODUCTS_FILE, [])
    keyword = input("Search: ").lower()
    for p in products:
        if keyword in p["name"].lower():
            print(p)

def get_product(product_id):
    products = load_data(PRODUCTS_FILE, [])
    for p in products:
        if p["product_id"] == product_id:
            return p
    return None

def update_products(products):
    save_data(PRODUCTS_FILE, products)