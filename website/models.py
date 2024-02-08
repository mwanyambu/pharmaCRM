from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.name
  
class DoctorList(models.Model):
  """
  Model representing a doctor in the CRM system.
  """
  #user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
  created_at = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  Speciality = models.CharField(max_length=50, default='General')
  phone = models.CharField(max_length=20)
  facility_name = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  email = models.CharField(max_length=100)
  #products_prescribing = models.ManyToManyField(product, default=None, blank=True)
  

  def __str__(self):
    """
    Returns a string representation of the doctor's full name.
    """
    return f"{self.first_name} {self.last_name}"
  
class Product_list(models.Model):
  doctor = models.ForeignKey(DoctorList, on_delete=models.CASCADE)
  product = models.ForeignKey(product, on_delete=models.CASCADE)

  def __str__(self):
    return self.doctor.user.username + ' - ' + self.product.name
  
class Regions(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  doctors = models.ManyToManyField(DoctorList, related_name='regions')

  def __str__(self):
    return self.name

class DailyCallReport(models.Model):
  doctor = models.ForeignKey(DoctorList, on_delete=models.CASCADE)
  call_date = models.DateField()
  call_time = models.TimeField()
  details = models.TextField()
  

