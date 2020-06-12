from django.db import models
from django.contrib.auth.models import User
from datetime import *


USER_TYPE = (
    (1, "Admin"),
    (2, "User")
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)   #This line binds this extended profile with user
    profile_image = models.ImageField(upload_to="userAdmin/ProfileImage", blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateTimeField(auto_now=True)
    usr_type = models.IntegerField(choices=USER_TYPE, default=2)
    usr_ip = models.GenericIPAddressField()
    user_browser = models.CharField(max_length=100, blank=True, null=True, default="")
    def __str__(self):
        return str(self.user)
    class Meta:
        db_table="UserProfile"


class Chellenge(models.Model):
    chellengeName = models.CharField(max_length=50, blank=False, null=False)
    chellengeDesc = models.TextField(max_length=1000, blank=True, null=True)
    def __str__(self):
            return self.chellengeName   #You will get the list with the Challenge name
    class Meta:
            db_table="Chellenge"

class TopicList(models.Model):
    Chellenge = models.ForeignKey(Chellenge, on_delete=models.CASCADE)  #one too many or many to one relaton
    Topic = models.CharField(max_length=50, blank=False, null=False)
    TopicDesc = models.TextField(max_length=1000, blank=True, null=True)
    def __str__(self):
        return  str(self.Topic)+' :  '+self.TopicDesc
    class Meta:
            db_table="TopicList"

class Comment(models.Model):
    #id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chellenge_id = models.ForeignKey(Chellenge, on_delete=models.CASCADE)
    date_comment = models.DateTimeField(default = datetime.today )  #This one works exact time of current location
    message = models.TextField('Message Field')
    def __str__(self):
        return str(self.user_id) + '    :   ' + str(self.chellenge_id) + '    :   ' +self.message
    class Meta:
            db_table="Comment"

