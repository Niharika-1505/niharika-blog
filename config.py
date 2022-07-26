import os

from dotenv import load_dotenv

# read key-value pairs from the .env file and store them as environment variables
load_dotenv()

# Mailtrap credentials
SMTP_LOGIN = os.environ["My_EMAIL"]
SMTP_PASS = os.environ["My_SecretKey"]

# secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# Heroku PostgreSQL URL
# if DATABASE_URL variable is not set, it will use the DB file instead
DATABASE_URL = os.getenv("DATABASE_URL",  "sqlite:///blog.db")