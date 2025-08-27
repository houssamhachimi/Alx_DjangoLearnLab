from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Create initial groups and assign permissions'

    def handle(self, *args, **kwargs):
        groups = ['Admin', 'Librarian', 'Member']
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Created group {group_name}')
        
        # Assign all permissions to Admin
        content_type = ContentType.objects.get_for_model(CustomUser)
        permissions = Permission.objects.filter(content_type=content_type)
        admin_group = Group.objects.get(name='Admin')
        admin_group.permissions.set(permissions)
        admin_group.save()

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))
