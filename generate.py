import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudproject.settings')
import django
django.setup()
from django.core.exceptions import *
from crudApp.models import *
from faker import Faker
faker = Faker()
from random import*
def generate(n):
    for i in range(n):
        fsno=randint(5,25)
        fsname=faker.name()
        fssalary=randint(100,10000)
        fsaddress=faker.city()
        stu_record=Student.objects.get_or_create(sno=fsno,sname=fsname,ssalary=fssalary,saddress=fsaddress)
generate(10)