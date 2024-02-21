from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Create users in the User model'

    def handle(self, *args, **kwargs):
        users_data = [
            {
                'email': 'kimonesmuske@gmail.com', 
                'password': 'Rongo@2024', 
                'gender': 'Male', 
                'mobile_no': '+1234567890', 
                'dob': '1990-01-01',
                'username': 'Kim',
                'first_name': 'Onesmus',
                'last_name': 'Muimi',
                'age': '21',
                },
            # Add more user data as needed
        ]

        for user_data in users_data:
            User.objects.create_user(**user_data)

        self.stdout.write(self.style.SUCCESS('Users created successfully'))
