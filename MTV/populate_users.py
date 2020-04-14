import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'rest_api.settings')
import django
django.setup()
## fake population all the above are mandatory settings
import random
from first_api.models import Users
from faker import Faker
fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        # create fake data for that entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        user = Users.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__=='__main__':
    print("populating script!")
    populate(20)
    print("populating complete")