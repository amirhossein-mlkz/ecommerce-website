from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class userManager(BaseUserManager):

    def create_user(self, 
                    firstname,
                    lastname,
                    username,
                    #email,
                    phone_number,
                    password = None
                        ):
        self.model = User
        if not phone_number:
            raise 'phone_number is required'
        
        user = self.model(
            #email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, 
                    firstname,
                    lastname,
                    username,
                    phone_number,
                    password = None
                        ):
        
        user = self.create_user(
            username = username,
            firstname = firstname,
            lastname = lastname,
            phone_number = phone_number,
            password=password
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
        

class User(AbstractBaseUser):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    phone_number = models.CharField( max_length=50, unique=True)
    username = models.CharField( max_length=50, unique=True)
    last_login = models.DateTimeField(auto_now=True)
    joinied_date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=500, blank = True)

    #Show account is active or not. it is better deactive instead of delete beacuse of foriegin key
    is_active = models.BooleanField(default=True)
    #show this user can access to admin panel
    is_staff = models.BooleanField(default=False)
    #treats this user as having all permissions 
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname',]

    objects = userManager()

    #standard function
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    #standard function
    def has_module_perms(self, app_label):
        return self.is_superuser

# Create your models here.
