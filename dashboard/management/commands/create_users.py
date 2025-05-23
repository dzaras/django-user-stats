from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates test users with random join dates (last 30 days)'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='user0').exists():
            self.stdout.write(self.style.WARNING('⚠️ Test users already exist. Skipping creation.'))
            return

        base_date = datetime.now()
        for i in range(100):
            join_date = base_date - timedelta(days=random.randint(0, 30))
            User.objects.create_user(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password='testpass123',
                date_joined=join_date
            )
        self.stdout.write(self.style.SUCCESS('✅ 100 test users created successfully.'))
