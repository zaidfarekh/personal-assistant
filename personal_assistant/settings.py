try:
    from personal_assistant.common import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, '../statics')


# ANYMAIL : mailgun configuration
ANYMAIL = {
    "MAILGUN_API_KEY": "< your api key at mailgun >",
    "MAILGUN_SENDER_DOMAIN": "< your sender domain at mailgun >"
}
EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
DEFAULT_FROM_EMAIL = "ahmadiga1985@hotmail.com"
