import os
import django
from locust import HttpUser, task, HttpLocust
from user.models import User, Profile
from django.urls import reverse


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BFFs.settings")
django.setup()


class MyProfile(HttpUser):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "email": "test01@test.com",
            "name": "test01",
            "password": "test12!@",
        }
        cls.user_data2 = {
            "email": "test02@test.com",
            "name": "test02",
            "password": "test12!@",
        }

        cls.user = User.objects.create_user("test01@test.com", "test01", "test12!@")
        cls.user2 = User.objects.create_user("test02@test.com", "test02", "test12!@")
        cls.profile_data = {
            "user": cls.user,
            "nickname": "nicktest1",
            "introduction": "introduction test",
            "region": "seoul",
        }
        cls.profile_data2 = {
            "user": cls.user2,
            "nickname": "nicktest1",
            "introduction": "introduction test",
            "region": "seoul",
        }
        cls.user_profile = Profile.objects.update(nickname="nickname1")
        cls.user_profile = Profile.objects.update(region="seoul")
        cls.user2_profile = Profile.objects.update(nickname="nickname2")
        cls.user2_profile = Profile.objects.update(region="seoul")

        cls.access_token = cls.client.post(reverse("login"), cls.user_data).data[
            "access"
        ]
        cls.access_token2 = cls.client.post(reverse("login"), cls.user_data2).data[
            "access"
        ]

    @task
    def my_profile_get_task(self):
        self.client.get("user/1/")  # 실제로 테스트하려는 API엔드포인트 넣기
