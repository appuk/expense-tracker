from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def add_expense(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        data = request.POST
        expense = Expense(date=data['date'], name=data['name'], category=data['category'], tax=data['tax'], tip=data['tip'], total=data['total'], comments=data['comments'])
        expense.save()
        return render(request, 'add_expense.html', {'message':'Expense added!!'})
    else:
        return render(request, 'add_expense.html')