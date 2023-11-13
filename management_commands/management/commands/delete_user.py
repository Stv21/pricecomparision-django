# management_commands/management/commands/delete_user_command.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Deletes a user from the database'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user to delete')

    def handle(self, *args, **kwargs):
        username = kwargs['username']

        try:
            user = User.objects.get(username=username)
            user.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted user: {username}'))
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'User with username {username} does not exist'))
