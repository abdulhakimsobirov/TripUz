from django.core.exceptions import ValidationError
import re
from django.forms.forms import Form
import phonenumbers

class PhoneValidator:
    requires_context = False
    @staticmethod
    def validate(value):
        try:
            item = phonenumbers.parse("+"+value)
            if not phonenumbers.is_valid_number(item):
                return False
        except:
                return False

        if len(value) != 12 or not value.startswith("998"):
            return False
        return True

    def __call__(self, value):
        if not PhoneValidator.validate(value):
            raise ValidationError("Enter the phone number correctly...")