from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def add_expense(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExpenseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            expense = Expense(**form.cleaned_data)
            expense.save()
            return render(request, 'add_expense.html', {'form': form, 'message':'Data was submitted.'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})