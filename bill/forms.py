from django import forms
from .models import *

class customerDetailForms(forms.ModelForm): 
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(label='Address',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email_address=forms.CharField(label='Email',required=False,widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone=forms.CharField(label='Phone',widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=Detail
        fields=['name','address','email_address','phone','invoice_number']
        exclude = ['invoice_number']


class productDetaillForms(forms.ModelForm):

    class Meta:
        model=productDetail
        fields=['customer','prod_name','quantity','rate']
       