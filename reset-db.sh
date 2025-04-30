from django.core.management.base import BaseCommand
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Deletes DB and migration files, recreates fresh DB, and makes a superuser.'

    def handle(self, *args, **kwargs):
        db_path = settings.DATABASES['default']['NAME']

        # 1. Remove old database
        if os.path.exists(db_path):
            os.remove(db_path)
            self.stdout.write(self.style.SUCCESS(f'✅ Deleted database at {db_path}'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️ No database found at {db_path}'))

        # 2. Remove all migrations (except __init__.py)
        for root, dirs, files in os.walk('.'):
            if 'migrations' in root:
                for file in files:
                    if file != '__init__.py' and file.endswith('.py'):
                        os.remove(os.path.join(root, file))
                    if file.endswith('.pyc'):
                        os.remove(os.path.join(root, file))
        self.stdout.write(self.style.SUCCESS('✅ Deleted all migration files.'))

        # 3. Make migrations and migrate
        os.system('python manage.py makemigrations')
        os.system('python manage.py migrate')
        self.stdout.write(self.style.SUCCESS('✅ Made fresh migrations and migrated.'))

        # 4. Create a superuser automatically
        from django.contrib.auth import get_user_model
        User = get_user_model()

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('✅ Created superuser admin/adminpassword'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Superuser admin already exists.'))

        self.stdout.write(self.style.SUCCESS('🎯 Database reset complete!'))
