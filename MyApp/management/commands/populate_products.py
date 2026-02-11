from django.core.management.base import BaseCommand
from MyApp.models import Product

class Command(BaseCommand):
    help = 'Populate database with sample products'

    def handle(self, *args, **options):
        # Clear existing products
        Product.objects.all().delete()

        # Sample products
        products = [
            {
                'name': 'Premium Smartphone',
                'description': 'Latest technology with amazing camera and 5G connectivity',
                'price': 599.99,
                'category': 'electronics',
                'stock': 50,
                'rating': 4.8,
                'reviews_count': 2345
            },
            {
                'name': 'Smart Watch',
                'description': 'Track your fitness and stay connected with our advanced smartwatch',
                'price': 299.99,
                'category': 'electronics',
                'stock': 75,
                'rating': 4.6,
                'reviews_count': 1892
            },
            {
                'name': 'Wireless Headphones',
                'description': 'Crystal clear sound with noise cancellation technology',
                'price': 199.99,
                'category': 'electronics',
                'stock': 100,
                'rating': 4.7,
                'reviews_count': 3112
            },
            {
                'name': 'Laptop Pro',
                'description': 'Powerful performance for professionals and creators',
                'price': 1299.99,
                'category': 'electronics',
                'stock': 30,
                'rating': 4.9,
                'reviews_count': 2567
            },
            {
                'name': 'Running Shoes',
                'description': 'Comfortable and stylish running shoes for all terrains',
                'price': 129.99,
                'category': 'fashion',
                'stock': 150,
                'rating': 4.5,
                'reviews_count': 1456
            },
            {
                'name': 'Travel Backpack',
                'description': 'Durable and spacious backpack perfect for any adventure',
                'price': 89.99,
                'category': 'fashion',
                'stock': 200,
                'rating': 4.4,
                'reviews_count': 987
            },
            {
                'name': 'Home Blender',
                'description': 'Powerful blender for smoothies and soups',
                'price': 79.99,
                'category': 'home',
                'stock': 60,
                'rating': 4.3,
                'reviews_count': 654
            },
            {
                'name': 'Gaming Mouse',
                'description': 'Professional gaming mouse with customizable buttons',
                'price': 49.99,
                'category': 'gaming',
                'stock': 120,
                'rating': 4.6,
                'reviews_count': 1234
            },
            {
                'name': 'Mechanical Keyboard',
                'description': 'RGB mechanical keyboard for gaming and typing',
                'price': 149.99,
                'category': 'gaming',
                'stock': 80,
                'rating': 4.5,
                'reviews_count': 892
            },
            {
                'name': 'Yoga Mat',
                'description': 'Non-slip yoga mat for your fitness routine',
                'price': 39.99,
                'category': 'sports',
                'stock': 200,
                'rating': 4.2,
                'reviews_count': 543
            },
        ]

        # Create products
        for product_data in products:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(products)} sample products'))
