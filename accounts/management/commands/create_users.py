from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import User
import secrets


class Command(BaseCommand):
    help = 'Create users in the User model'

    def handle(self, *args, **kwargs):
        users_data = [
            # Add user credentials here - use dictionary
            {
                'username': 'test.user',
                'gender': 'Male',
                'email': 'testuser@gmail.com',
                'dob': '2000-01-01',
                'mobile_no': '+254112345678',
                'password': 'morikeli',
            },
            {
                'username': 'brenda.jones',
                'gender': 'Female',
                'email': 'bjones@gmail.com',
                'dob': '2000-01-01',
                'mobile_no': '+254112345678',
                'password': 'morikeli',
            },
            {
                'username': 'sarah.jones',
                'gender': 'Female',
                'email': 'sarahj@gmail.com',
                'dob': '2000-01-01',
                'mobile_no': '+254112345678',
                'password': 'morikeli',
            },
        ]

        for user_data in users_data:
            try:
                user = User.objects.create_user(**user_data)
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user_data["username"]}'))
            
            except IntegrityError:    # if the user credentials exists, print the message below.
                self.stdout.write(self.style.ERROR(f'User account with credentials {user_data["email"]} exists!'))
                continue    # continue saving other user credentials.

            # Send welcome email to the user
            # self.send_welcome_email(user, user_data["password"])
        self.stdout.write(self.style.SUCCESS('User accounts created successfully!'))
    

    def send_welcome_email(self, user, password):
        subject = 'Welcome to DSC uchaguzi online'
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        message = f'''
        {user.first_name} {user.last_name}
        Welcome to GDSC uchaguzi online.

        Your login credentials:
        Email: {user.email}
        Password: {password}

        If you have any questions or need assistance, feel free to contact us.

        Best regards,
        Your Website Team
        '''

        send_mail(subject, message, from_email, [to_email])