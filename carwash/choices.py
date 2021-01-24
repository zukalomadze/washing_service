from django.db.models import IntegerChoices


class CarChoice(IntegerChoices):

    SUV = 1
    Sedane = 2
    Hatchback = 3
    Other = 4