# tasks.py
from django.core.mail import send_mail
from home.models import PriceAlert

def check_prices_and_send_email():
    # Query the PriceAlert model to find products with prices below the desired range
    alerts_to_notify = PriceAlert.objects.filter(price_below_desired_range=True)

    for alert in alerts_to_notify:
        # Send an email to the user
        subject = 'Price Alert: Price Dropped Below Desired Range'
        message = f'The price of the product at {alert.url} has dropped below your desired range.'
        from_email = '202201029.stevenmsn@gmail.com'
        recipient_list = [alert.user.email]

        send_mail(subject, message, from_email, recipient_list)
