class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return f"{self.title} - ${self.price}"

class CartItem:
    def __init__(self, book, quantity):
        self.book = book
        self.quantity = quantity

    def total_price(self):
        return self.book.price * self.quantity

    def __repr__(self):
        return f"{self.book.title} x {self.quantity} - ${self.total_price()}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, book, quantity):
        for item in self.items:
            if item.book == book:
                item.quantity += quantity
                break
        else:
            self.items.append(CartItem(book, quantity))

    def remove_item(self, book):
        self.items = [item for item in self.items if item.book != book]

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for item in self.items:
                print(item)

    def total_price(self):
        return sum(item.total_price() for item in self.items)

if __name__ == "__main__":
    # Create some books
    book1 = Book("Python Programming", 29.99)
    book2 = Book("Learning Python", 24.99)

    # Create a shopping cart
    cart = Cart()

    # Add books to the cart
    cart.add_item(book1, 2)
    cart.add_item(book2, 1)

    # View cart
    print("Your cart contains:")
    cart.view_cart()

    # Total price
    print(f"\nTotal price: ${cart.total_price():.2f}")

    # Remove a book and view cart again
    print("\nRemoving 'Python Programming' from the cart...\n")
    cart.remove_item(book1)
    cart.view_cart()

    # Total price after removal
    print(f"\nTotal price after removal: ${cart.total_price():.2f}")
