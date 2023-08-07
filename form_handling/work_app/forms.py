from django import forms
from django.core import validators


class UserForm(forms.Form):
    name = forms.CharField(help_text='Please enter your username area',
                           widget=forms.TextInput(attrs={'placeholder': "Username"}))
   #  name = forms.CharField(label="Username", initial='Juel',
   #                         help_text='Please enter your username', widget=forms.Textarea(attrs={'id': 'my_area', 'class': 'class_1 class_2'}))
    email = forms.EmailField(label="UserEmail")
    file = forms.FileField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    size_category = [('Large', 'Large'), ('Medium',
                                          'Medium'), ('Small', 'Small')]
    size = forms.ChoiceField(choices=size_category,
                             widget=forms.SelectMultiple)
   #  select = forms.ChoiceField(choices=size_category, widget=forms.RadioSelect)
    questions_list = [('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3')]
   #  Questions = forms.MultipleChoiceField(choices=questions_list)
    check = forms.MultipleChoiceField(
        choices=questions_list, widget=forms.CheckboxSelectMultiple)


# class valid_form(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     def clean(self):
#         clean_data = super().clean()
#         valName = self.cleaned_data['name']
#         valEmail = self.cleaned_data['email']
#         if len(valName) < 10:
#             raise forms.ValidationError(
#                 "Enter your name at least 10 characters")
#         if '.com' not in valEmail:
#             raise forms.ValidationError(
#                 "Your provided email is not valid type example@example.com")


def check_pass(value):
    if len(value)<10:
        raise forms.ValidationError("Pass must be at least 10 characters")



class valid_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message="Input lenth must be at least 10 charaters"), validators.MaxLengthValidator(20, message="Input lentgh can be maximum 20 charaters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Not a valid email address")])
   #  age = forms.IntegerField(validators=[validators.MinValueValidator(18, message="Age must be at least 18")])
   #  text = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(20, message="Text must be at least 20 charactars")])
   #  file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='only pdf files are allowed')]) 
    password=forms.CharField(widget=forms.PasswordInput,validators=[check_pass])
    re_password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        clean_data = super().clean()
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['re_password']
        if pass1 != pass2:
            raise forms.ValidationError("Re-password not matched with tha password")
        
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message = 'File Extension must be ended with .pdf')])

  
