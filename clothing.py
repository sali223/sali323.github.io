class ClothingTracker:
    def __init__(self):
        self.clothes = []

    def add_item(self):
        item = input("Enter the clothing item name: ")
        category = input("Enter the category (e.g., shirt, pants, jacket): ")
        color = input("Enter the color: ")
        size = input("Enter the size: ")

        clothing_item = {
            'name': item,
            'category': category,
            'color': color,
            'size': size
        }

        self.clothes.append(clothing_item)
        print(f"{item} has been added to your clothing tracker.")

    def remove_item(self):
        item_to_remove = input("Enter the name of the item you want to remove: ")
        for i, item in enumerate(self.clothes):
            if item['name'].lower() == item_to_remove.lower():
                del self.clothes[i]
                print(f"{item_to_remove} has been removed from your clothing tracker.")
                return
        print(f"{item_to_remove} not found in your tracker.")

    def view_clothes(self):
        if not self.clothes:
            print("You have no items in your clothing tracker.")
            return

        print("\nYour Clothing Tracker:")
        for i, item in enumerate(self.clothes):
            print(f"{i + 1}. {item['name']} - {item['category']} - {item['color']} - {item['size']}")

    def run(self):
        while True:
            print("\nClothing Tracker Menu:")
            print("1. Add a clothing item")
            print("2. Remove a clothing item")
            print("3. View clothing items")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.view_clothes()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    tracker = ClothingTracker()
    tracker.run()
