from django import forms

class Form(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email