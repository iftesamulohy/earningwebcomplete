
from datetime import timedelta
from django.db import models
from solo.models import SingletonModel
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Aboutus(SingletonModel):
    name = models.CharField(max_length=50)
    text= models.TextField(max_length=5000)
    class Meta:
        verbose_name = "About Us"

class PrivacyPolicy(SingletonModel):
    title = models.CharField(max_length=50)
    text= models.TextField(max_length=5000)
    class Meta:
        verbose_name = "Privacy Policy"

class Terms(SingletonModel):
    title = models.CharField(max_length=50)
    text= models.TextField(max_length=5000)
    class Meta:
        verbose_name = "Terms & Conditions"


"""
class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True,default="hello@gmail.com")
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False,null=True)
    reffered_by = models.CharField(max_length=30,null=True)
    USERNAME_FIELD = models.CharField(max_length=30,default="hello")
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
"""
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True, default='', unique=True)
    username = models.CharField(max_length=255, blank=True, default='',unique=True)
    balance = models.IntegerField(default=0,null=True,validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    phone_no = models.CharField(max_length=15,blank=True)
    refferedby = models.CharField(max_length=50,blank=True)
    profile_picture = models.ImageField(upload_to='images/profile',null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
class Deposit(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    number=models.CharField(max_length=15,blank=True,null=True)
    trx_id = models.CharField(max_length=50,blank=True,null=True)
    OPTION_A = 'bkash'
    OPTION_B = 'nagad'
    CHOICES = (
        (OPTION_A, 'Bkash'),
        (OPTION_B, 'Nagad'),
        
    )
    payment_method = models.CharField(max_length=10, choices=CHOICES,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    amount = models.IntegerField(blank=True,null=True)
    OPTION_a = 'Complete'
    OPTION_b = 'Pending'
    OPTION_c = 'Canceled'
    CHOICES2 = (
        (OPTION_a, 'Completed'),
        (OPTION_b, 'Pending'),
        (OPTION_c, 'Canceled'), 
        
    )
    status = models.CharField(max_length=10, choices=CHOICES2,blank=True,null=True)
    def __str__(self):
        return f"{self.number}"
class Withdraw(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    number=models.CharField(max_length=15,blank=True,null=True)
    trx_id = models.CharField(max_length=50,blank=True,null=True)
    OPTION_A = 'bkash'
    OPTION_B = 'nagad'
    CHOICES = (
        (OPTION_A, 'Bkash'),
        (OPTION_B, 'Nagad'),
        
    )
    payment_method = models.CharField(max_length=10, choices=CHOICES,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    amount = models.IntegerField(blank=True,null=True,validators=[MinValueValidator(0)])
    OPTION_a = 'Complete'
    OPTION_b = 'Pending'
    OPTION_c = 'Canceled'
    CHOICES2 = (
        (OPTION_a, 'Completed'),
        (OPTION_b, 'Pending'),
        (OPTION_c, 'Canceled'), 
        
    )
    status = models.CharField(max_length=10, choices=CHOICES2,blank=True,null=True)
    def __str__(self):
        return f"{self.number}"
    

class Packages(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    daily_task = models.IntegerField(validators=[MinValueValidator(0)])
    daily_income = models.IntegerField(validators=[MinValueValidator(0)])
    refer_bonus= models.IntegerField(validators=[MinValueValidator(0)])
    plan_validity = models.IntegerField(validators=[MinValueValidator(0)])
    def __str__(self):
        return f"{self.name}"

class PackageOrder(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Packages,on_delete=models.CASCADE, null=True)
    purchase_date = models.DateField()
    expire_date= models.DateField()
    OPTION_a = 'Activate'
    OPTION_b = 'Expired'
    CHOICES2 = (
        (OPTION_a, 'Activate'),
        (OPTION_b, 'Expired'),
        
    )
    status = models.CharField(max_length=10, choices=CHOICES2,blank=True,null=True)
    refferedby = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f"{self.package}"


class Work(models.Model):
    title = models.CharField(max_length=150)
    package= models.ForeignKey(Packages,on_delete=models.CASCADE, null=True,blank=True)
    work_details = models.TextField(max_length=5000)
    work_link = models.URLField(blank=True,null=True)
    reaward_amount = models.IntegerField(validators=[MinValueValidator(0)])
    starting_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    def __str__(self):
        return f"{self.title}"
class CompleteTask(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    work = models.ForeignKey(Work,on_delete=models.CASCADE, null=True,blank=True)
    image = models.ImageField(upload_to='images/screenshots')
    OPTION_g = 'Canceled'
    OPTION_h = 'Approved'
    OPTION_i = 'Pending'
    CHOICES3 = (
        (OPTION_g, 'Canceled'),
        (OPTION_h, 'Approved'),
        (OPTION_i, 'Pending')
        
    )
    status = models.CharField(max_length=10, choices=CHOICES3,blank=True,null=True)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.work}"








    ######################################################################################################
    #utilities
class Utilities(SingletonModel):
    n_text = models.TextField(max_length=5000,null=True,default="সম্মানিত গ্রাহক আপনাদের অবগতির জন্য জানানো যাচ্ছে যে... ")
    joining_bonus= models.IntegerField(validators=[MinValueValidator(0)],null=True)
    app_link=models.URLField(default="#",null=True)
    telegram_link = models.URLField(default="#",null=True)
    free_package= models.ForeignKey(Packages,on_delete=models.CASCADE, null=True,blank=True)
    bkash_guide = models.TextField(max_length=5000,null=True,default="সম্মানিত গ্রাহক আপনাদের অবগতির জন্য জানানো যাচ্ছে যে... ")
    bkash_number = models.CharField(max_length=15,blank=True)
    nagad_guide = models.TextField(max_length=5000,null=True,default="সম্মানিত গ্রাহক আপনাদের অবগতির জন্য জানানো যাচ্ছে যে... ")
    nagad_number = models.CharField(max_length=15,blank=True)
    class Meta:
        verbose_name = "Utilities"