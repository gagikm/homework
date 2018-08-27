from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FrequentlyAskedQuestion, Testimonial

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    cell_phone = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cell_phone', 'email', 'password1', 'password2')


class FAQForm(forms.ModelForm):

	class Meta:
		model = FrequentlyAskedQuestion
		fields = ('question', 'answer')

class TestimonialForm(forms.ModelForm):

	class Meta:
		model = Testimonial
		fields = ('styling_goal', 'testimonial')
