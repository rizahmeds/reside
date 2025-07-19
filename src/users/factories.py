import factory
from factory.django import DjangoModelFactory

from users.models import CustomUser, LandLoard, Tenant


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser
        django_get_or_create = ("email",)

    email = factory.Faker("email")


class LandLoardFactory(DjangoModelFactory):
    class Meta:
        model = LandLoard

    user = factory.SubFactory(CustomUserFactory)


class TenantFactory(DjangoModelFactory):
    class Meta:
        model = Tenant

    user = factory.SubFactory(CustomUserFactory)
