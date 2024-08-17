import factory
from factory.django import DjangoModelFactory

from properties.models import Property, Rooms
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


class PropertyFactory(DjangoModelFactory):
    class Meta:
        model = Property

    land_loard = factory.SubFactory(LandLoardFactory)
    address = factory.Faker("address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    country = factory.Faker("country")
    zip_code = factory.Faker("postcode")


class RoomsFactory(DjangoModelFactory):
    class Meta:
        model = Rooms

    property = factory.SubFactory(PropertyFactory)
    tenant = factory.SubFactory(TenantFactory)