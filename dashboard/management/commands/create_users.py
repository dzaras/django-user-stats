from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates test users with random join dates'

    def handle(self, *args, **kwargs):
        base_date = datetime.now()
        for i in range(100):
            join_date = base_date - timedelta(days=random.randint(0, 30))
            User.objects.create_user(
                username=f'user{i}',
                password='testpass123',
                date_joined=join_date
            )
        self.stdout.write(self.style.SUCCESS('✅ 100 users created successfully.'))