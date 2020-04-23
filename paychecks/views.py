from django.shortcuts import render
from .models import Paycheck
from utils.utils import form_validate


# Create your views here.
def add_paycheck(request):
    if request.method == 'POST':
        data = request.POST
        message = form_validate(data, 'add paycheck')
        if "Invalid" not in message:
            paycheck = Paycheck(date=data['date'], name=data['name'], tax=data['tax'], benefits=data['benefits'], in_hand=data['in_hand'],total=data['total'], comments=data['comments'])
            paycheck.save()
        return render(request, 'add_paycheck.html', {'message': message})
    else:
        return render(request, 'add_paycheck.html')