# Shop Wise 🛒

This is a Django-based web application for managing an e-commerce platform.
The project includes features for managing products, customers, orders, and shopping carts.

## Check it out!

[Shop Wise project deployed to Render](https://shop-wise-6u6y.onrender.com)

## Installation

Python3 must be already installed.

1. **Clone the repository:**
    ```bash
    git clone https://github.com/vladislav-tsybuliak1/shop-wise.git
    cd django-store
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file for environment variables:**
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/yourdatabase
    ```

5. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```

6. **(Optional) Load data from the prepared fixture to populate db:**
    ```bash
    python manage.py loaddata shop_wise_db_data.json
    ```

7. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
NOTE: If you loaded data from the fixture you can use the following superuser:
  - Login: `admin`
  - Password: `test123test`

8. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Features

- Customer/User authentication and registration
- Product, brand, and category listing, creation, update, and deletion
- Addition products to customer's shopping cart and deletion from it
- Order creation from shopping cart
- Updating orders' statuses
- Customer's reviews for products

## Demo

[Website Interface](demo.png)

## Contact

For any inquiries, please contact [vladislav.tsybuliak@gmail.com](mailto:vladislav.tsybuliak@gmail.com).
