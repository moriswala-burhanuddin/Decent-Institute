from django import forms
from .models import Review, Contact

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']
          
# Contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'intrested_course', 'phone_number', 'message']

