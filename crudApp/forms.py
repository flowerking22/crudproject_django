
from django import forms
from .models import Student
 
 
# creating a form
class StudentForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Student
 
        # specify fields to be used
        fields = [
            "sno", 
    "sname",
    "ssalary",
    "saddress"
        ]