from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    profile = models.CharField(max_length=500)
    c_time = models.DateTimeField(auto_now=False)
    m_time = models.DateTimeField(auto_now=True)
    salt = models.UUIDField(default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.user_name + ' ' + self.password
