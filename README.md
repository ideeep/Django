# ShopHub - E-Commerce Website with Django

Welcome to ShopHub! This is a fully functional e-commerce website built with Django that includes user authentication, product management, shopping cart, and order processing.

## Features

✅ **User Authentication**
- User Registration with email validation
- Secure Login/Logout
- User Dashboard with order history
- Profile management

✅ **Product Management**
- Browse products by category
- Search functionality
- Product details page
- Product ratings and reviews

✅ **Shopping Cart**
- Add/Remove items from cart
- View cart with item quantities
- Real-time cart updates
- Cart persistence per user

✅ **Checkout & Orders**
- Secure checkout process
- Order confirmation page
- Order history tracking
- Order status management

✅ **Admin Panel**
- Manage products
- Manage users
- Track orders
- View sales analytics

## Setup Instructions

### 1. Install Dependencies

```bash
pip install django pillow
```

### 2. Run Migrations

The database has already been set up with the following models:
- User (Django's built-in User model)
- Product
- Cart
- CartItem
- Order
- OrderItem

```bash
python manage.py migrate
```

### 3. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 4. Load Sample Products

```bash
python manage.py populate_products
```

This will add 10 sample products to the database with different categories.

### 5. Run the Development Server

```bash
python manage.py runserver
```

The website will be available at: `http://localhost:8000`

## URL Routes

### Public Routes
- `/` - Home page
- `/products/` - Products listing with filters
- `/product/<id>/` - Product detail page
- `/register/` - User registration
- `/login/` - User login
- `/about/` - About page

### Authenticated Routes (Requires Login)
- `/cart/` - Shopping cart
- `/add-to-cart/<product_id>/` - Add product to cart
- `/remove-from-cart/<item_id>/` - Remove item from cart
- `/checkout/` - Checkout page
- `/order-confirmation/<order_id>/` - Order confirmation
- `/dashboard/` - User dashboard
- `/logout/` - Logout

### Admin Routes
- `/admin/` - Django Admin Panel

## Database Models

### User Model (Django's Built-in)
- username
- email
- password
- first_name
- last_name
- date_joined

### Product Model
- name
- description
- price
- category (Electronics, Fashion, Home, Sports, Books, Gaming)
- stock
- rating
- reviews_count
- created_at
- updated_at

### Cart Model
- user (One-to-One relationship)
- created_at
- updated_at

### CartItem Model
- cart (Foreign Key)
- product (Foreign Key)
- quantity
- added_at

### Order Model
- user (Foreign Key)
- order_id (Unique)
- total_amount
- status (Pending, Confirmed, Shipped, Delivered, Cancelled)
- shipping_address
- created_at
- updated_at

### OrderItem Model
- order (Foreign Key)
- product (Foreign Key)
- quantity
- price

## Admin Panel Features

### Managing Products
1. Go to `/admin/`
2. Login with your superuser credentials
3. Click on "Products"
4. Add new products, edit, or delete existing ones
5. You can bulk edit prices and stock quantities

### Managing Orders
1. Go to Products → Orders in Admin Panel
2. View all orders with details
3. Update order status
4. View order items

### Managing Users
1. Go to Authentication and Authorization → Users
2. View registered users
3. Edit user information
4. Manage user permissions

## How to Use the Website

### For Customers

1. **Register an Account**
   - Click on "Register" button
   - Fill in username, email, and password
   - Click "Create Account"

2. **Login**
   - Click on "Login" button
   - Enter your credentials
   - You'll be redirected to your dashboard

3. **Browse Products**
   - Go to "Products" page
   - Filter by category or search by name
   - Click "View Details" for more information

4. **Add to Cart**
   - View product details
   - Click "Add to Cart" button
   - You'll be redirected to cart

5. **Checkout**
   - Go to your cart
   - Review items and total
   - Click "Proceed to Checkout"
   - Fill in shipping address
   - Click "Place Order"

6. **View Orders**
   - Go to your Dashboard
   - View your order history with status

## Categories Available

- 📱 Electronics
- 👕 Fashion
- 🏠 Home & Living
- ⚽ Sports
- 📚 Books
- 🎮 Gaming

## Sample Products

The database comes with 10 sample products:
1. Premium Smartphone - $599.99
2. Smart Watch - $299.99
3. Wireless Headphones - $199.99
4. Laptop Pro - $1,299.99
5. Running Shoes - $129.99
6. Travel Backpack - $89.99
7. Home Blender - $79.99
8. Gaming Mouse - $49.99
9. Mechanical Keyboard - $149.99
10. Yoga Mat - $39.99

## File Structure

```
DjangoSetup/
├── manage.py
├── db.sqlite3
├── DjangoSetup/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── MyApp/
│   ├── models.py (Product, Cart, Order models)
│   ├── views.py (All application views)
│   ├── urls.py (URL routing)
│   ├── admin.py (Admin configuration)
│   └── management/
│       └── commands/
│           └── populate_products.py (Sample data)
└── template/
    ├── Home.html
    ├── products.html
    ├── product_detail.html
    ├── login.html
    ├── register.html
    ├── cart.html
    ├── checkout.html
    ├── dashboard.html
    ├── order_confirmation.html
    └── about.html
```

## Customization

### Adding New Categories
Edit `MyApp/models.py` and update the `CATEGORY_CHOICES` in the Product model:

```python
CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('fashion', 'Fashion'),
    ('your_category', 'Your Category Name'),
]
```

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Changing Colors
All styling is done with inline CSS. To change the purple gradient color (currently `#667eea` to `#764ba2`), search and replace in template files.

### Customizing Product Fields
To add new fields to products, edit `Product` model in `MyApp/models.py`, then run:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, try:
```bash
python manage.py runserver 8001
```

### Database Issues
To reset the database completely:
```bash
# Delete the database
rm db.sqlite3

# Run migrations again
python manage.py migrate

# Create new superuser
python manage.py createsuperuser

# Load sample products
python manage.py populate_products
```

### CSS Not Showing
CSS is inline in the HTML templates. If styling looks weird, clear your browser cache.

## Security Notes

⚠️ This is a development setup. For production:
1. Set `DEBUG = False` in settings.py
2. Use a proper database (PostgreSQL, MySQL)
3. Set strong `SECRET_KEY`
4. Use environment variables for sensitive data
5. Enable HTTPS
6. Set `ALLOWED_HOSTS` properly
7. Use a production server (Gunicorn, uWSGI)

## Support

For issues or questions, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Django Models: https://docs.djangoproject.com/en/stable/topics/db/models/
- Django Views: https://docs.djangoproject.com/en/stable/topics/http/views/

## License

This project is open source and available for educational and personal use.

---

Happy Shopping! 🛍️
