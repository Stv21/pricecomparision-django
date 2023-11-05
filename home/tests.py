from django.test import TestCase
from django.core import mail
from home.models import PriceAlert
from userproject.tasks import check_prices_and_send_email

#from .tasks import check_prices_and_send_email

class EmailSendingTestCase(TestCase):
    def setUp(self):
        # Create a PriceAlert with desired_price and actual_price
        self.price_alert = PriceAlert.objects.create(
            url='https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYSCIIOB&marketplace=FLIPKART&q=IPHONE15&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=7e654fde-98fd-42b9-99ec-fc3543be5097.MOBGTAGPAQNVFZZY.SEARCH&ppt=hp&ppn=homepage&ssid=in8q5h3pkzdprrb41698384342661&qH=98b3206691794a40',
            user_email='stevenmas29@gmail.com',
            desired_price=70000.00,
            actual_price=79900.00,
        )

    def test_email_sent_when_price_drops(self):
        # Simulate a price drop (set price_below_desired_range to True)
        self.price_alert.price_below_desired_range = True
        self.price_alert.save()

        # Call the email function
        check_prices_and_send_email()

        # Check if an email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Price Alert: Price Dropped Below Desired Range')
    
    def test_email_not_sent_when_price_within_range(self):
        # Simulate a price within the desired range
        self.price_alert.price_below_desired_range = False
        self.price_alert.save()

        # Call the email function
        check_prices_and_send_email()

        # Check if no email was sent
        self.assertEqual(len(mail.outbox), 0)
