import factory
from django.contrib.auth import get_user_model

from posts.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence")
    body = factory.Faker("text")
    author = factory.SubFactory("accounts.tests.factories.UserFactory")
