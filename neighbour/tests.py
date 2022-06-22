from django.test import TestCase
from django.contrib.auth.models import User
from .models import NeighborHood, Profile, Business, Post

class NeighborTestClass(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="ali",email="ali@gmail.com")
        self.neighbor = NeighborHood(name = 'Fedha',user = user)
        self.neighbor.create_neighborhood()

    def test_get_neighborhood(self):
        my_hood = NeighborHood.find_neighborhood(self.local.id)
        self.assertTrue(len(my_hood)==1)

    def test_save_hood(self):
        self.neighbor.create_neighborhood()
        my_hood =NeighborHood.objects.all()
        self.assertTrue(len(my_hood) > 0)
class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="alinur",email="alinur@gmail.com")
        self.profile = Profile(user=user,bio="This is my profile",contact="072222222",profile_photo="/image")
    def test_isntance(self):
        self.assertTrue(isinstance(self.profile,Profile))
    def save_profile_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class BusinessTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="murimi",email="murimi@gmail.com")
        self.business = Business(user=user,name="Barbershop",email="murimi@gmail.com")
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
    def save_business_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

class PostTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="ludwig",email="ludwig@gmail.com")
        self.posts = Post(user=user,title="politics",content="politics is dirty game")
    def test_instance(self):
        self.assertTrue(isinstance(self.posts,Post))
    def save_post_method(self):
        self.posts.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)


