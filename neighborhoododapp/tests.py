from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post,NeighbourHood,Business,Profile,User

class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = Profile(user='Levy')
        self.user.save()
        self.user_profile = Profile(user=self.user, profile_picture="photore.png", bio="My bio")
   
    def tearDown(self):
       
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_user_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_user_profile(self):
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)