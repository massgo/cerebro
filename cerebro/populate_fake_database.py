from django.utils.timezone import datetime

import random
import string

# Set environment to work with Django (allows us to easily import and work with
# Django ORM)
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cerebro.settings")
django.setup()

from main.models import AGAMember

""" 
This script creates 50 :class:`AGAMember`s whose fields are populated
with random stuff (of the appropriate type).
"""

def random_gen(N):
    """Generate a random string w/ uppercase letters and integers
   
    Args:
        N (int): Size of random string to be returned

    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

# Create 50 random AGAMembers
for ii in range(50):
    AGAMember.objects.create(
            name = random_gen(25),
            aga_id = random.randint(1, 1000),
            chapter = random_gen(25),
            state = random_gen(25),
            rating = random.randint(1, 1000)*.001,
            sigma = random.randint(1, 1000)*.001,
            expiry = datetime.now(),
            updated = datetime.now(),
            mtype = random_gen(25)
    )
