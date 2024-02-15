from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import DoctorList, DoctorVisit, SalesRep, MasterDoctorList, Region, VisitPlan, Product, Supervisor
"""from .models import DailyCallReport
#from .models import product, Product_list, Regions"""

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
  first_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
  last_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
  Speciality = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Speciality'}))
  phone = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
  facility_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facility Name'}))
  city = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
  state = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
  email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
  zip = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip'}))
  notes = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}))
  class Meta:
    model = DoctorList
    exclude = ('user',)

class SupervisorReportForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['phone', 'email']

class SalesRepForm(forms.ModelForm):
    class Meta:
        model = SalesRep
        fields = ['region', 'phone', 'email']

class MasterDoctorForm(forms.ModelForm):
    class Meta:
        model = MasterDoctorList
        fields = ['sales_rep', 'first_name', 'last_name', 'speciality', 'phone', 'Hospital_name', 'location']

class DoctorVisitForm(forms.ModelForm):
    class Meta:
        model = DoctorVisit
        fields = ['sales_rep', 'doctor', 'visit_date', 'visit_notes', 'feedback', 'status', 'supervisor']

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['region_name', 'assigned_rep']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'product_price', 'product_quantity', 'product_category']

class VisitPlanForm(forms.ModelForm):
    class Meta:
        model = VisitPlan
        fields = ['sales_rep', 'doctor', 'visit_date', 'visit_notes', 'feedback']

class DoctorListForm(forms.ModelForm):
    class Meta:
        model = DoctorList
        fields = ['first_name', 'last_name', 'Speciality', 'phone', 'facility_name', 'city', 'state', 'email']