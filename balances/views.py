from django.shortcuts import render
from .models import Balance
from utils.utils import form_validate


# Create your views here.

def add_balance(request):
    if request.method == 'POST':
        print("in post")
        data = request.POST
        message = form_validate(data, 'add balance')
        total = 0
        if "Invalid" not in message:
            total = int(data['bofa1']) + int(data['bofa2']) + int(data['pnc']) + int(data['dcu']) + int(data['fidelity']) + int(data['coastal'])
            balance = Balance(month=data['month'], bofa1=data['bofa1'], bofa2=data['bofa2'], pnc=data['pnc'], dcu=data['dcu'], fidelity=data['fidelity'], coastal=data['coastal'], total=total, comments=data['comments'])
            balance.save()
        return render(request, 'add_balance.html', {'message': message, 'total': total})
    else:
        return render(request, 'add_balance.html')