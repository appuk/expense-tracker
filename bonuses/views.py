from django.shortcuts import render
from .models import Bonus
from utils.utils import form_validate


# Create your views here.

def add_bonus(request):
    if request.method == 'POST':
        data = request.POST
        message = form_validate(data, 'add bonus')
        if "Invalid" not in message:
            bonus = Bonus(date=data['date'], name=data['name'], in_hand=data['in_hand'], tax=data['tax'], total=data['total'], comments=data['comments'])
            bonus.save()
        return render(request, 'add_bonus.html', {'message': message})
    else:
        return render(request, 'add_bonus.html')