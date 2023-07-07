import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BFFs.settings")
django.setup()
# user model 보다 위에서 불러와 환경변수를 설정해준다

from locust import task, HttpUser, HttpLocust
from django.urls import reverse
from user.models import User, Profile
from community.models import Community, CommunityAdmin
from feed.models import GroupPurchase, Category


class MyUserTask(HttpUser):
    @task
    def my_profile_get_task(self):
        """user profile get"""
        self.client.get("user/1/")
        self.client.get("user/3/")
        self.client.get("user/4/")
        self.client.get("user/5/")

    @task
    def grouppurchase_data_get_task(self):
        """공구 게시글 상세 get"""
        self.client.get("community/testcomu1/grouppurchase/1/")
        self.client.get("community/testcomu1/grouppurchase/2/")
        self.client.get("community/testcomu1/grouppurchase/3/")
        self.client.get("community/testcomu1/grouppurchase/4/")
        self.client.get("community/testcomu1/grouppurchase/5/")

    # def grouppurchase_data_update_task(self):
    #     """공구 게시글 update"""
    #     self.client.put("community/testcomu1/grouppurchase/1/")
    #     self.client.put("community/testcomu1/grouppurchase/2/")
    #     self.client.put("community/testcomu1/grouppurchase/3/")
    #     self.client.put("community/testcomu1/grouppurchase/4/")
    #     self.client.put("community/testcomu1/grouppurchase/5/")
