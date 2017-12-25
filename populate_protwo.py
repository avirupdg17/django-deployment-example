import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoDemo.settings')

import django
django.setup()

from faker import Faker
from ProTwo.models import User
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        userlist = User.objects.get_or_create(FirstName= fakegen.first_name(),LastName = fakegen.last_name(),Email= fakegen.email())[0]


if __name__ == '__main__':
    print('Populating Script')
    populate(20)
    print('Populating complete')
