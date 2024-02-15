from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Supervisor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  sales_reps_assigned = models.ManyToManyField('SalesRep', related_name='supervisors_assigned', blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)

  def __str__(self):
    return self.user.username

class SalesRep(models.Model):
  """
  Model representing a sales representative in the CRM system.
  """

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
  region = models.CharField(max_length=50)
  phone = models.CharField(max_length=20)
  email = models.EmailField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    """
    Returns a string representation of the sales representative's username.
    """
    return self.user.username
  



class MasterDoctorList(models.Model):
  """
  Model representing a master doctor list in the CRM system.
  """
  created_at = models.DateTimeField(auto_now_add=True)
  sales_rep = models.ForeignKey(SalesRep, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  speciality = models.CharField(max_length=50)
  phone = models.CharField(max_length=20)
  Hospital_name = models.CharField(max_length=100, verbose_name='Hospital Name')
  location = models.CharField(max_length=100)

  def __str__(self):
    """
    Returns a string representation of the doctor's full name.
    """
    return f"{self.first_name} {self.last_name}"
  
class DoctorVisit(models.Model):
  """
  Model representing a doctor visit in the CRM system.
  """
  created_at = models.DateTimeField(auto_now_add=True)
  sales_rep = models.ForeignKey(SalesRep, on_delete=models.CASCADE)
  doctor = models.ForeignKey(MasterDoctorList, on_delete=models.CASCADE)
  visit_date = models.DateField()
  visit_notes = models.TextField()
  feedback = models.TextField()
  status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending')
  supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    """
    Returns a string representation of the doctor's full name.
    """
    return f"{self.doctor} {self.visit_date}"

class Region(models.Model):
  """
  Model representing a region in the CRM system.
  """
  region_name = models.CharField(max_length=50)
  assigned_rep = models.ForeignKey(SalesRep, on_delete=models.CASCADE, related_name='assigned_region')

  def __str__(self):
    """
    Returns a string representation of the region's name.
    """
    return self.region_name
  
class Product(models.Model):
  """
  Model representing a product in the CRM system.
  """
  product_name = models.CharField(max_length=50)
  product_description = models.TextField()
  product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
  product_quantity = models.IntegerField()
  product_category = models.CharField(max_length=50)

  def __str__(self):
    """
    Returns a string representation of the product's name.
    """
    return self.product_name
  
class VisitPlan(models.Model):
  """
  Model representing a visit plan in the CRM system.
  """
  sales_rep = models.ForeignKey(SalesRep, on_delete=models.CASCADE)
  doctor = models.ForeignKey(MasterDoctorList, on_delete=models.CASCADE)
  visit_date = models.DateField()
  visit_notes = models.TextField()
  feedback = models.TextField()

  def __str__(self):
    """
    Returns a string representation of the doctor's full name.
    """
    return f"{self.doctor} - {self.visit_date}"
  

class DoctorList(models.Model):
  """
  Model representing a doctor in the CRM system.
  """
  created_at = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  Speciality = models.CharField(max_length=50, default='General')
  phone = models.CharField(max_length=20)
  facility_name = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  email = models.CharField(max_length=100)

  

  def __str__(self):
    """
    Returns a string representation of the doctor's full name.
    """
    return f"{self.first_name} {self.last_name}"
