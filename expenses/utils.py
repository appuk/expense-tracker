def form_validate(data, form):
    if form == 'add expense':
        mandatory_feilds = ['date','name','category','tax', 'tip', 'total']
    invalid = []
    for feild in mandatory_feilds:
        if data[feild] == '':
            invalid.append(feild)
    if invalid:
        return 'Invalid entry for the feilds: ' + ', '.join(invalid)
    else:
        return 'Expense added!!'