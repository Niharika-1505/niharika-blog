import os
import re

from dotenv import load_dotenv

# read key-value pairs from the .env file and store them as environment variables
load_dotenv()

# Gmail credentials
SMTP_LOGIN = os.environ.get("My_EMAIL")
SMTP_PASS = os.environ.get("My_SecretKey")

# secret key
SECRET_KEY = os.environ.get("SECRET_KEY")

# Heroku PostgreSQL URL
# if DATABASE_URL variable is not set, it will use the DB file instead
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///blog.db")  # or other relevant config var

# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# DATABASE_URL = (uri, "sqlite:///blog.db")
