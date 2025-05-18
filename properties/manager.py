from django.db.models.manager import Manager


class PropertyManager(Manager):
    def create_property(self, land_loard, property_type, **address):
        property_data = {
            "land_loard": land_loard,
            "property_type": property_type,
            **address,
        }

        # create the property object
        property = self.model(**property_data)
        property.save(using=self._db)
        print("Created property....")


class RoomsManager(Manager):
    def create_room(self, property, room_no, tenant, base_rent):
        room_data = {
            "property": property,
            "room_no": room_no,
            "tenant": tenant,
            "base_rent": base_rent,
        }

        # create the room object
        room = self.model(**room_data)
        room.save(using=self._db)
        print("Created room with uid %s", str(room.room_no))
