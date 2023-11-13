from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
import requests
import pandas as pd
from fuzzywuzzy import fuzz
from django.contrib.auth.models import User
from .forms import PriceAlertForm
from .models import PriceAlert
from django.contrib import messages


# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)

        # Log in the new user
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("login")  # Redirect to the login page after successful signup

    return render(request, 'signup.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def convert_dollars_to_rupees(price_in_dollars, exchange_rate=75.0):
    try:
        price_in_rupees = float(price_in_dollars.replace('$', '')) * exchange_rate
        return price_in_rupees
    except ValueError:
        return None
def search_view(request):
    query = request.GET.get('query', '')
    if query:
        flipkart_file = r'static\files\flipkart_com-ecommerce_sample.csv'
        amazon_file = r'static\files\marketing_sample_for_amazon_com-ecommerce__20200101_20200131__10k_data.csv'
        result = compare_prices(flipkart_file, amazon_file, query)
        context = {
            'query': query,
            'products': result['products'],
            'amazon_products': result['amazon_products'],
            'flipkart_products': result['flipkart_products'],
            'best_product': result['best_product'],
            'best_price': result['best_price'],
        } # Add a comma to separate the previous statement from the next
        context['amazon_categories'] = [product['category'].split('|')[0] if isinstance(product['category'], str) else product['category'] for product in result['amazon_products']]
        context['flipkart_categories'] = [product['category'].split('|')[0] if isinstance(product['category'], str) else product['category'] for product in result['flipkart_products']]
        return render(request, 'search_results.html', context)
    else:
        return HttpResponse("Please provide a query for search.")
    
def compare_prices(flipkart_file, amazon_file, product_name, category=None):
    flipkart_data = pd.read_csv(flipkart_file)
    amazon_data = pd.read_csv(amazon_file)

    flipkart_products = flipkart_data[flipkart_data['product_name'].str.lower().str.contains(product_name.lower())]
    amazon_products = amazon_data[amazon_data['Product Name'].str.lower().str.contains(product_name.lower())]

    if category:
        flipkart_products = flipkart_products[flipkart_products['product_category_tree'].str.contains(category)]
        amazon_products = amazon_products[amazon_products['Category'].str.contains(category)]

    flipkart_prices = []
    amazon_prices = []
    
    # Define the maximum number of products for each category
    max_products_per_category = 4

    for index, row in flipkart_products.iterrows():
        name = row['product_name']
        price = row['discounted_price']
        if not pd.isna(price):
            price = float(price)
            url = row['product_url']
            image_links = row['image'].strip('][').replace('"', '').split(', ')
            product_category = row['product_category_tree']  # Add category field

            flipkart_prices.append({'name': name, 'price': price, 'url': url, 'images': image_links, 'category': product_category})
            if len(flipkart_prices) >= max_products_per_category:
                break

    for index, row in amazon_products.iterrows():
        name = row['Product Name']
        price = row['Selling Price']
        if not pd.isna(price):
            price = convert_dollars_to_rupees(price)
            if price is not None:
                url = row['Product Url']
                image_links = row['Image'].split('|')
                product_category = row['Category']  # Add category field

                amazon_prices.append({'name': name, 'price': price, 'url': url, 'images': image_links, 'category': product_category})
                if len(amazon_prices) >= max_products_per_category:
                    break

    if not flipkart_prices and not amazon_prices:
        return f"No results found for {product_name}."

    # Determine the best product based on price
    best_flipkart = None
    flipkart_price = None
    best_amazon = None
    amazon_price = None

    if flipkart_prices:
        best_flipkart = min(flipkart_prices, key=lambda k: k['price'])
        flipkart_price = best_flipkart['price']

    if amazon_prices:
        best_amazon = min(amazon_prices, key=lambda k: k['price'])
        amazon_price = best_amazon['price']

    result = {
        'products': product_name,
        'amazon_products': amazon_prices,
        'flipkart_products': flipkart_prices,
        'best_product': best_flipkart if flipkart_prices and amazon_prices else None,
        'best_price': flipkart_price if flipkart_price < amazon_price else amazon_price if flipkart_prices and amazon_prices else None,
    }
    return result






def logoutUser(request):
    logout(request)
    return redirect("/login")

def search_products(request):
    return HttpResponse("This is the search products view.")

def Electronics(request):
    return render(request, 'Electronics.html')

def Fashion(request):
    return render(request, 'Fashion.html')

def Email(request):
    if request.method == 'POST':
        form = PriceAlertForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            desired_price = form.cleaned_data['desired_price']

            # Save the user's request to the database (PriceAlert model)
            price_alert = PriceAlert(user=request.user, url=url, desired_price=desired_price)
            price_alert.save()

            # Schedule a task to check prices periodically (e.g., using Celery)
            # You need to implement the price checking logic in a Celery task

            # Display a success message to the user
            messages.success(request, 'Price alert has been set up. You will be notified when the price drops below the desired range.')

            return redirect('Email')  # Redirect to the same page after form submission

    else:
        form = PriceAlertForm()

    return render(request, 'Email.html', {'form': form})

def Sports(request):
    return render(request, 'Sports.html')
