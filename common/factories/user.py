import factory
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttribute(lambda x: fake.email())
    password = factory.LazyAttribute(lambda x: fake.password())

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class AdminUserFactory(UserFactory):
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_superuser(*args, **kwargs)
