# enumerate() is a built-in Python function that adds a counter (index) to an iterable and returns both the index and the value of each item during a loop.

shopping_cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "HDMI Cable"]
target_product = "Monitor"

print(f"Searching for: {target_product}...")

# Check items and capture their exact location index
for index, product in enumerate(shopping_cart):
    if product == target_product:
        print(f" Found it! '{product}' is located at Index position [{index}] in your array list.")
        break
else:
    print("Item not found in the cart.")
