# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=yq@v@^h^cw_1mhi%p=2+bv1qhxcxa5xx06_ood&5&5_&=gj3q'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost', 
        'USER': 'root',
        'PASSWORD': 'Schwartz07!'
    }
}