from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
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
            user = User.objects.create_user(**user_data)

            # Send welcome email to the user
            self.send_welcome_email(user)

        self.stdout.write(self.style.SUCCESS('Users created successfully'))

    def send_welcome_email(self, user):
        subject = 'Welcome to DSC uchaguzi online'
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        message = f'''
        {user.first_name} {user.last_name}
        Welcome to DSC uchaguzi online

        Your login credentials:
        Email: {user.email}
        Password: {user.password}

        If you have any questions or need assistance, feel free to contact us.

        Best regards,
        Your Website Team
        '''

        send_mail(subject, message, from_email, [to_email])