from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    """Extra user data.
    
    Fields:

    facebook_user_id: User ID from the Facebook API.  This is populated if 
                      the user chooses to register/login with Facebook."""
    user = models.ForeignKey(User)
    facebook_user_id = models.TextField()

# Create your models here.
