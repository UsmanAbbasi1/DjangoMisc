from django.core.management import BaseCommand

from cache_example.tasks import test_task


class Command(BaseCommand):
    """Run task 'test_task' and show example usage of arguments"""

    '''
    as 'positional_argument1' is positional argument, name of argument should not be mentioned while 
    running the command. First 2 values as shown in example i.e 123 and 456 will be stored in 
    'positional_argument1' as list and 789 will be stored in 'positional_argument2' as list
    '''
    help = 'Spawn \'count\' number of tasks. Example usage: python manage.py run_test_task 123 456 789 --count 1'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            help='Number of tasks to spawn'
        )

        '''
        Argument name without '-' shows that it is required and it will be passed as positional argument
        nargs = 2 means that 2 values should be passed for this argument
        '''
        parser.add_argument('positional_argument1',
                            nargs=2)

        parser.add_argument('positional_argument2',
                            nargs=1)

    def handle(self, *args, **options):
        print(args)
        print('/n')
        print(options)
        test_task.delay()
