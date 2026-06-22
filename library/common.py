from django.db.models import IntegerField
from django.db.models.functions import Cast
from .models import OsfaRequests

def get_next_request_number(current_year):
     max_number = (OsfaRequests.objects
          .filter(number__startswith=current_year)
          .annotate(number_int=Cast("number", IntegerField()))
          .order_by("-number_int")
          .values_list("number_int", flat=True)
          .first()
     )
     
     new_number = (max_number or 0) + 1

     return format_request_number(str(new_number))

def format_request_number(number: str):
     return f"{number[:4]}-{number[4:]}"
