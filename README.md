# 🛍️ The Essence Decor - Procedural Python Shopping Cart Application (1st semester project)

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Code Style: PEP8](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/mmaazwk27/Shopping-Cart-Python-semester-project)

![Academic Project](https://img.shields.io/badge/License-Academic-blueviolet?style=for-the-badge&logo=bookstack&logoColor=white)&nbsp;
![Made in Pakistan](https://img.shields.io/badge/Made%20In-Pakistan-006600?style=for-the-badge&logo=pakistan&logoColor=white)

Welcome to **The Essence Decor** — a simple, interactive console-based 🖥️ shopping cart app built with pure procedural Python.

---

## 🧾 Overview

This CLI-based application simulates an online store for **home decor products**, enabling users to:

- 👤 Create accounts
- 🔐 Login securely
- 🛒 Browse and manage shopping carts
- 🧾 View order history
- 💳 Checkout and generate billing info

Data is saved using simple `.txt` files — perfect for learning file handling and procedural programming.

---

## ✨ Features

- 👥 **User Management**: Account creation, validation, secure login
- 🛍️ **Product Catalog**: 11 curated items with prices
- 🧺 **Cart Operations**: Add/remove items, quantity tracking
- 📜 **Order History**: Timestamped records of past purchases
- 📁 **Data Storage**: Text-based persistence (accounts, user files)
- 🧭 **Clear Navigation**: Intuitive CLI menus with input validation
- 💰 **Billing**: Real-time total cost calculations

---

## ▶️ How to Use

1. 🟢 Run the script: `shop code.py`
2. 🏠 Main Menu:
   - `1` ➤ Create New Account
   - `2` ➤ Login to Existing Account
   - `3` ➤ Exit
3. 🛍️ Inside your account:
   - View products
   - Add/remove items from cart
   - View cart and total
   - Checkout
   - View past orders
   - Logout

---

## 🛒 Product List

| 🏷️ Product Name        | 💵 Price (Rs.) |
|------------------------|----------------|
| Organizers             | 1000           |
| Rugs                   | 6000           |
| Side Coffee Tables     | 990            |
| Mirror                 | 3900           |
| Book Shelves           | 10000          |
| Flower Pots            | 500            |
| Wall Art Decors        | 200            |
| TV Console             | 14000          |
| Hanging Swings         | 16000          |
| Bean Bags              | 5000           |
| Wall Clocks            | 5000           |

---

## 📁 File Structure

- `accounts.txt` – Stores login credentials
- `{username}.txt` – Each user’s personal info + shopping history

---

## 🧠 Code Structure

The application uses **procedural programming** and includes:

- **Dictionaries**:
  - `process_menu`: product → price
  - `menu`: serial → product
  - `cart`: product → quantity
  - `user_account`: temp account info
  - `read_data`: saved accounts

- **Functions**:
  - `view_menu()` 🧾
  - `view_cart()` 🛒
  - `add_to_cart()` ➕
  - `rem_cart()` ➖
  - `create_account()` 🆕
  - `login()` 🔐

---

## ⚙️ Dependencies

- Python 3.x ✅
- No external libraries required ❌📦

---

## 🚀 Future Enhancements

- 🛡️ Password encryption/hashing
- 🗃️ Switch to SQLite or JSON for structured data
- 🌐 Web UI with Flask or Django
- 🧠 AI-based product suggestions
- 📊 Enhanced analytics dashboard


---

# 👨‍💻 Author 

**Muhammad Maaz Wali Khan**
-- 🔗 [GitHub: @mmaazwk27](https://github.com/mmaazwk27)
- ### Collaborator
    **Eman Zaheer**
-- 🔗 [GitHub: @emanzaheer](https://github.com/emanzaheer)

## 🙌 Thanks for Checking Out The Essence Decor!

Enjoy coding and happy shopping! 🎉🛍️
