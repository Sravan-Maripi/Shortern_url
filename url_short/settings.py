import os
SQL_ALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
SQL_ALCHEMY_NOTIFICATIONS_TRACK=False
ADMIN_PASSWORD=os.environ.get('ADMIN_PASSWORD')
ADMIN_USERNAME=os.environ.get('ADMIN_USERNAME')
