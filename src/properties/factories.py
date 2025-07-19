import factory
from factory.django import DjangoModelFactory

from users.factories import LandLoardFactory, TenantFactory
from properties.models import Property, Rooms


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
    base_rent = factory.Faker("random_number", digits=4)
