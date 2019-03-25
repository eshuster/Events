from django.core.exceptions import ValidationError
from datetime import datetime    
from django.utils import timezone
from django.utils.timezone import now

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_start_date(value):
	if value < timezone.now():
		raise ValidationError(
            ('%(value)s has already occured'),
            params={'value': value},
		)