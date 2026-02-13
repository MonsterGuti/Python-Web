from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RangeValidator:
    def __init__(self, min_value, max_value, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def min_value(self):
        return self.__min_value

    @min_value.setter
    def min_value(self, value):
        if value < 0:
            raise ValueError('Min value must be positive')

        self.__min_value = value

    def __call__(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)
