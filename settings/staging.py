from base import *
import dj_database_url
import settings

DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

#  Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_WPgPzAQeCfea08WkskzTqxii')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_6vCTHyEBILOhXzg3gfMd9U8w')

# paypal environment variables
SITE_URL = 'https://eds-we-are-social.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://eds-we-are-social.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'ed.walker.merchant@hotmail.co.uk'
