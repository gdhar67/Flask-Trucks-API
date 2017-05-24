from flask_marshmallow import Marshmallow
from model import user, user_trucks, truck_details, booking_requests, journey_plans, items

ma = Marshmallow()

# Schema declaration

class UserSchema(ma.ModelSchema):
    class Meta:
        model = user


class Truck_DetailSchema(ma.ModelSchema):
    class Meta:
        model = truck_details



class UsertruckSchema(ma.ModelSchema):
    class Meta:
        model = user_trucks


class BookingrequestSchema(ma.ModelSchema):
    class Meta:
        model = booking_requests


class Journey_planSchema(ma.ModelSchema):
    class Meta:
        model = journey_plans


class ItemsSchema(ma.ModelSchema):
    class Meta:
        model = items



# Schema Initialisation

user_schema = UserSchema()

truck_detail_schema = Truck_DetailSchema()

usertruck_schema = UsertruckSchema()

booking_request_schema = BookingrequestSchema()
booking_requests_schema = BookingrequestSchema(many=True)

journey_plan_schema = Journey_planSchema()
journey_plans_schema = Journey_planSchema(many=True)

items_schema = ItemsSchema()