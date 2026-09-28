"""
Coffee Shop App - a beginner-friendly OOP project in Python.

OOP concepts used:
  * Class & Object   -> Coffee, Order, CoffeeShop
  * Inheritance      -> Espresso, Latte, Cappuccino, Mocha inherit from Coffee
  * Encapsulation    -> Order keeps its items in a "private" list (_items)
  * Polymorphism     -> every coffee has its own describe() behaviour
  * Composition      -> an Order HAS coffees, a CoffeeShop HAS a menu and orders
"""


# ---------------------------------------------------------------
# 1. The parent (base) class
# ---------------------------------------------------------------
class Coffee:
    # Price multiplier for each size
    SIZES = {"small": 1.0, "medium": 1.3, "large": 1.6}

    def __init__(self, name, base_price, size="medium"):
        self.name = name
        self.base_price = base_price
        self.size = size

    def get_price(self):
        """Price depends on the size chosen."""
        return round(self.base_price * self.SIZES[self.size], 2)

    def describe(self):
        return f"{self.size.capitalize()} {self.name}"

    def __str__(self):
        return f"{self.describe()} - Rs. {self.get_price()}"


# ---------------------------------------------------------------
# 2. Child classes (Inheritance)
# ---------------------------------------------------------------
class Espresso(Coffee):
    def __init__(self, size="medium"):
        super().__init__("Espresso", 120, size)

    def describe(self):
        return f"{self.size.capitalize()} Espresso (strong & bold)"


class Latte(Coffee):
    def __init__(self, size="medium", milk="whole"):
        super().__init__("Latte", 180, size)
        self.milk = milk

    def get_price(self):
        price = super().get_price()
        if self.milk == "oat":  # oat milk costs extra
            price += 30
        return price

    def describe(self):
        return f"{self.size.capitalize()} Latte with {self.milk} milk"


class Cappuccino(Coffee):
    def __init__(self, size="medium"):
        super().__init__("Cappuccino", 160, size)

    def describe(self):
        return f"{self.size.capitalize()} Cappuccino (extra foam)"


class Mocha(Coffee):
    def __init__(self, size="medium"):
        super().__init__("Mocha", 200, size)

    def describe(self):
        return f"{self.size.capitalize()} Mocha with chocolate"


# ---------------------------------------------------------------
# 3. Order class (holds many coffees)
# ---------------------------------------------------------------
class Order:
    TAX_RATE = 0.05  # 5% tax

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self._items = []  # underscore = "private", use methods to access

    def add_item(self, coffee):
        self._items.append(coffee)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        return None

    def is_empty(self):
        return len(self._items) == 0

    def subtotal(self):
        return sum(item.get_price() for item in self._items)

    def tax(self):
        return round(self.subtotal() * self.TAX_RATE, 2)

    def total(self):
        return round(self.subtotal() + self.tax(), 2)

    def show(self):
        print(f"\n--- Order for {self.customer_name} ---")
        if self.is_empty():
            print("  (nothing yet)")
        for i, item in enumerate(self._items, start=1):
            print(f"  {i}. {item}")
        print(f"  Subtotal: Rs. {self.subtotal()}")

    def print_bill(self):
        print("\n" + "=" * 40)
        print("          COFFEE SHOP BILL")
        print("=" * 40)
        print(f"Customer: {self.customer_name}")
        print("-" * 40)
        for item in self._items:
            print(f"{item.describe():<28} Rs. {item.get_price()}")
        print("-" * 40)
        print(f"{'Subtotal':<28} Rs. {self.subtotal()}")
        print(f"{'Tax (5%)':<28} Rs. {self.tax()}")
        print(f"{'TOTAL':<28} Rs. {self.total()}")
        print("=" * 40)
        print("Thank you! Enjoy your coffee ☕\n")


# ---------------------------------------------------------------
# 4. The CoffeeShop class (runs the whole app)
# ---------------------------------------------------------------
class CoffeeShop:
    def __init__(self, name):
        self.name = name
        # Menu maps a number to a coffee class
        self.menu = {
            "1": Espresso,
            "2": Latte,
            "3": Cappuccino,
            "4": Mocha,
        }

    def show_menu(self):
        print("\n----------- MENU -----------")
        for key, coffee_class in self.menu.items():
            sample = coffee_class("small")  # small size shows the starting price
            print(f"  {key}. {sample.name:<12} from Rs. {sample.get_price()}")
        print("----------------------------")

    def ask_size(self):
        while True:
            size = input("Size (small / medium / large): ").strip().lower()
            if size in Coffee.SIZES:
                return size
            print("Please type small, medium or large.")

    def create_coffee(self, choice):
        coffee_class = self.menu[choice]
        size = self.ask_size()

        if coffee_class is Latte:
            milk = input("Milk (whole / oat): ").strip().lower()
            if milk not in ("whole", "oat"):
                print("Unknown milk, using whole milk.")
                milk = "whole"
            return Latte(size, milk)

        return coffee_class(size)

    def run(self):
        print(f"\n☕ Welcome to {self.name}! ☕")
        customer = input("What's your name? ").strip() or "Guest"
        order = Order(customer)

        while True:
            print("\nWhat would you like to do?")
            print("  1. See menu")
            print("  2. Add a coffee")
            print("  3. View my order")
            print("  4. Remove an item")
            print("  5. Checkout")
            print("  6. Quit")
            action = input("Choose (1-6): ").strip()

            if action == "1":
                self.show_menu()

            elif action == "2":
                self.show_menu()
                choice = input("Pick a coffee number: ").strip()
                if choice in self.menu:
                    coffee = self.create_coffee(choice)
                    order.add_item(coffee)
                    print(f"Added: {coffee.describe()}")
                else:
                    print("Invalid choice, try again.")

            elif action == "3":
                order.show()

            elif action == "4":
                order.show()
                if not order.is_empty():
                    try:
                        num = int(input("Item number to remove: "))
                        removed = order.remove_item(num - 1)
                        if removed:
                            print(f"Removed: {removed.describe()}")
                        else:
                            print("No such item.")
                    except ValueError:
                        print("Please enter a number.")

            elif action == "5":
                if order.is_empty():
                    print("Your order is empty!")
                else:
                    order.print_bill()
                    break

            elif action == "6":
                print("Goodbye! Come back soon 👋")
                break

            else:
                print("Please choose a number from 1 to 6.")


# ---------------------------------------------------------------
# 5. Start the program
# ---------------------------------------------------------------
if __name__ == "__main__":
    shop = CoffeeShop("Python Brew Cafe")
    shop.run()
