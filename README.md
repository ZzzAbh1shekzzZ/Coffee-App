 ☕ Coffee Shop App (Python OOP)

A beginner-friendly, command-line coffee ordering app built in Python to practice **Object-Oriented Programming (OOP)**. Choose your coffee, pick a size, customise it, and get a printed bill with tax.

 Features

- Menu with four coffees: Espresso, Latte, Cappuccino and Mocha
- Three sizes (small, medium, large) with automatic price changes
- Milk choice for lattes (whole or oat, oat costs extra)
- Add, view and remove items in your order
- Bill with subtotal, 5% tax and total
- Input validation for invalid choices

 OOP Concepts Demonstrated

| Concept | Where it is used |
|---|---|
| **Classes & Objects** | `Coffee`, `Order`, `CoffeeShop` |
| **Inheritance** | `Espresso`, `Latte`, `Cappuccino`, `Mocha` inherit from `Coffee` |
| **Polymorphism** | Each coffee overrides `describe()`; `Latte` overrides `get_price()` |
| **Encapsulation** | `Order` keeps items in a private list (`_items`) and exposes methods |
| **Composition** | An `Order` has coffees; a `CoffeeShop` has a menu and orders |

 Project Structure

```
coffee-shop-app/
├── coffee_app.py   # All classes and the main program
└── README.md
```

 Getting Started

 Requirements
- Python 3.6 or higher (no external libraries needed)

 Run the app

```bash
git clone https://github.com/<your-username>/coffee-shop-app.git
cd coffee-shop-app
python coffee_app.py
```

## Example Output

```
========================================
          COFFEE SHOP BILL
========================================
Customer: Asha
----------------------------------------
Large Latte with oat milk    Rs. 318.0
Small Espresso (strong & bold) Rs. 120.0
----------------------------------------
Subtotal                     Rs. 438.0
Tax (5%)                     Rs. 21.9
TOTAL                        Rs. 459.9
========================================
Thank you! Enjoy your coffee ☕
```

## Ideas for Future Improvements

- [ ] Add more drinks (e.g. `Americano`, `Cold Brew`)
- [ ] Save orders to a file or database
- [ ] Add a `Customer` class with loyalty points
- [ ] Add discount codes
- [ ] Build a GUI with Tkinter or a web version with Flask

## Contributing

Suggestions and improvements are welcome. Fork the repo, make your changes and open a pull request.

## License

This project is open source under the [MIT License](LICENSE).

## Author

Made by **<your-name>** as a Python OOP learning project.
