from django.db import models


from django.db import models
from django.contrib.auth.models import User, Group
import datetime
import random
import string
def generate_unique_code():
    # Generate a random string of length 8 (you can adjust the length and characters)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class DoctorSpecialization(models.Model):
    name=models.CharField(max_length=100)
    Code=models.CharField(max_length=100)

class Organization(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True,null=True)
    code = models.CharField(max_length=100, unique=True,blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code()  # Generate unique code
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
class GroupPermission(Group):  # groups newly added
    group_name = models.CharField(max_length=100)
    Organization = models.ForeignKey(Organization, related_name='groups', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.name)


class Administrator(User):
    name=models.CharField(max_length=100, blank=True, default="User")
    profile_img = models.ImageField(upload_to='Admins', default='/Admins/doctor.jpg')
    bio = models.CharField(max_length=100, blank=True, default="User Here")
    SpecialInformation=models.TextField(null=True,blank=True)
    GraduationFrom=models.CharField(max_length=100)
    GraduationDate = models.DateField(max_length=100)
    IsDoctor=models.BooleanField(default=0)
    DoctorSpecializations = models.ManyToManyField(DoctorSpecialization, related_name='administrators', blank=True,null=True)
    group_in = models.ForeignKey(GroupPermission, related_name='admin',on_delete=models.CASCADE,default=None,null=True)
    Organization = models.ForeignKey(Organization, related_name='administrators', null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"
        permissions = (
            ("AddAdmin", "Can add admin"),
            ("ShowAdmin", "Show all admin"),
            ("DoctorSpecializations", "show doctor in same Specializations"),
        )
    def __str__(self):
        return self.name

class patient(User):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    profile_img = models.ImageField(blank=True,null=True,upload_to='patient', default='/patient/account.png')
    Organization = models.ForeignKey(Organization, related_name='Clinic', null=True, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    @property
    def age(self):
        if self.birth_date:
            age = datetime.date.today() - self.birth_date
            return int(age.days / 365.25)
        return None  # In case birth_date is not set
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patient"
        permissions = ()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_code()  # Generate unique code
        super().save(*args, **kwargs)
