from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from.models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )

        cls.post = Post.objects.create(
            title = "A good title",
            body="Nice body content",
            author=cls.user,
            color = 'GREEN'
        )

    def test_post_model(self):
        self.assertEqual(self.post.title,"A good title")
        self.assertEqual(self.post.body,"Nice body content")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(self.post.color,"GREEN")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_url_exists_at_correct_location_listview(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_at_correct_location_detailview(self): # new
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)
    
    def test_post_listview(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")     

        
           

    def test_post_detailview(self): # new
        response = self.client.get(reverse("post_detail",
        kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")
        response = ""

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "HELLO",
                "body": "BYE",
                "author": "dyyys0ft",
                "color":"GREEN",
            },
        )
        no_response = self.client.get("/post/"+str(Post.objects.last().id))
        self.assertEqual(no_response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "HELLO")
        self.assertEqual(Post.objects.last().body, "BYE")



    def test_post_updateview(self): 
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "UP",
                "body": "UP T",

            },
            )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "UP")
        self.assertEqual(Post.objects.last().body, "UP T")
        



    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args = "1"))
        self.assertEqual(response.status_code,302)



# Create your tests here.
