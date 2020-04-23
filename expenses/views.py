from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Expense, Paycheck, Bonus
from .utils import form_validate

# Create your views here.
def add_expense(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        data = request.POST
        message = form_validate(data, 'add expense')
        if "Invalid" not in message:
            expense = Expense(date=data['date'], name=data['name'], category=data['category'], tax=data['tax'], tip=data['tip'], total=data['total'], comments=data['comments'])
            expense.save()
        return render(request, 'add_expense.html', {'message': message})
    else:
        return render(request, 'add_expense.html')

def add_paycheck(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        message = form_validate(data, 'add paycheck')
        if "Invalid" not in message:
            paycheck = Paycheck(date=data['date'], name=data['name'], tax=data['tax'], benefits=data['benefits'], in_hand=data['in_hand'],total=data['total'], comments=data['comments'])
            paycheck.save()
        return render(request, 'add_paycheck.html', {'message': message})
    else:
        return render(request, 'add_paycheck.html')

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