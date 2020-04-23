def form_validate(data, form):
    print("in form validate")
    if form == 'add expense':
        mandatory_feilds = ['date','name','category','tax', 'tip', 'total']
        success_message = 'Expense added!!'
    elif form == 'add paycheck':
        mandatory_feilds = ['date','name','benefits','tax', 'in_hand', 'total']
        success_message = 'Paycheck added!!'
    elif form == 'add bonus':
        print("in paycheck validate")
        mandatory_feilds = ['date','name','tax', 'in_hand', 'total']
        success_message = 'Bonus added!!'
    invalid = []
    for feild in mandatory_feilds:
        if data[feild] == '':
            invalid.append(feild)
    if invalid:
        return 'Invalid entry for the feilds: ' + ', '.join(invalid)
    else:
        return success_message