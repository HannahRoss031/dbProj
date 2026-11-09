import os
from csi3335f2025 import mysql

# Specifications for reading settings for the app:
class Config:
  # Dynamically construct the URI using the keys from the csi3335f2025.py dictionary
  SQLALCHEMY_DATABASE_URI = (
      f"mysql+pymysql://{mysql['user']}:{mysql['password']}"
      f"@{mysql.get('host', mysql.get('location'))}/{mysql['database']}"
  )
  # current setup is sensitive to @, /, : - ensure proper escaping if necessary