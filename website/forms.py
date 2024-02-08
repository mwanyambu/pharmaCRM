from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import DoctorList
from .models import DailyCallReport
from .models import product, Product_list, Regions

class SignUpForm(UserCreationForm):
  """
  Form for user sign up.

  Inherits from UserCreationForm and adds additional fields for email, first name, and last name.
  """

  email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
  first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
  last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'Username'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class AddRecordForm(forms.ModelForm):
  """
  Form for adding a doctor record.

  Inherits from ModelForm and is used to create a form for adding a doctor record.
  """

  #first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Doctor's Name", "class":"form-control"}), label="")
  #last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
  #speciality = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Speciality", "class":"form-control"}), label="")
  #location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}), label="")
  #phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
  #email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")

  class Meta:
    model = DoctorList
    exclude = ('user',)

class DailyReportForm(forms.ModelForm):
  """
  Form for adding a daily call report.

  Inherits from ModelForm and is used to create a form for adding a daily call report.
  """

  class Meta:
    model = DailyCallReport
    fields = ('doctor', 'call_date', 'call_time', 'details')
    widgets = {
      'doctor': forms.Select(attrs={'class':'form-control'}),
      'call_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
      'call_time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
      'details': forms.Textarea(attrs={'class':'form-control', 'rows':3})
    }

class AddProductForm(forms.ModelForm):
  """
  Form for adding a product record.

  Inherits from ModelForm and is used to create a form for adding a product record.
  """

  class Meta:
    model = product
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'description': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
      'price': forms.NumberInput(attrs={'class':'form-control'}),
    }

class AddProductListForm(forms.ModelForm):
  """
  Form for adding a product list record.

  Inherits from ModelForm and is used to create a form for adding a product list record.
  """

  class Meta:
    model = Product_list
    fields = '__all__'
    widgets = {
      'doctor': forms.Select(attrs={'class':'form-control'}),
      'product': forms.Select(attrs={'class':'form-control'}),
    }

class AddRegionForm(forms.ModelForm):
  """
  Form for adding a region record.

  Inherits from ModelForm and is used to create a form for adding a region record.
  """

  class Meta:
    model = Regions
    fields = '__all__'
    widgets = {
      'user': forms.Select(attrs={'class':'form-control'}),
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'doctors': forms.SelectMultiple(attrs={'class':'form-control'}),
    }


