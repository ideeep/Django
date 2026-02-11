from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart, CartItem, Order, OrderItem


# Home View
def Home(request):
    products = Product.objects.all()[:6]
    return render(request, 'Home.html', {'products': products})


# Products List View
def products_list(request):
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    
    products = Product.objects.all()
    
    if category:
        products = products.filter(category=category)
    if search:
        products = products.filter(name__icontains=search) | products.filter(description__icontains=search)
    
    categories = Product.CATEGORY_CHOICES
    return render(request, 'products.html', {'products': products, 'categories': categories, 'search': search})


# Product Detail View
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    return render(request, 'product_detail.html', {'product': product, 'related_products': related_products})


# Register View
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        Cart.objects.create(user=user)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    
    return render(request, 'register.html')


# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    
    return render(request, 'login.html')


# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('Home')


# Dashboard View
@login_required(login_url='login')
def dashboard(request):
    user = request.user
    recent_orders = Order.objects.filter(user=user)[:5]
    return render(request, 'dashboard.html', {'recent_orders': recent_orders})


# Add to Cart View
@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')


# View Cart
@login_required(login_url='login')
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.all()
    total = sum(item.get_total() for item in items)
    return render(request, 'cart.html', {'cart': cart, 'items': items, 'total': total})


# Remove from Cart
@login_required(login_url='login')
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')


# Checkout View
@login_required(login_url='login')
def checkout(request):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        items = cart.items.all()
        
        if not items.exists():
            messages.error(request, 'Cart is empty!')
            return redirect('cart')
        
        total_amount = sum(item.get_total() for item in items)
        shipping_address = request.POST.get('shipping_address')
        
        # Create Order
        order = Order.objects.create(
            user=request.user,
            order_id=f"ORD-{request.user.id}-{Order.objects.count() + 1}",
            total_amount=total_amount,
            shipping_address=shipping_address
        )
        
        # Create Order Items
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        # Clear cart
        items.delete()
        
        messages.success(request, f'Order placed successfully! Order ID: {order.order_id}')
        return redirect('order_confirmation', order_id=order.id)
    
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.all()
    total = sum(item.get_total() for item in items)
    return render(request, 'checkout.html', {'items': items, 'total': total})


# Order Confirmation
@login_required(login_url='login')
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})


# About View
def about(request):
    return render(request, 'about.html')

