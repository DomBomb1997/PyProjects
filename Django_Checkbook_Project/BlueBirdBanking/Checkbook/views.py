from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction
# This function will render the Home page when requested
def home(requested):
    form = TransactionForm(data=request.POST or None) # Retrieve Trasaction form
    # Checks if request method is POST
    if request.method == 'POST'
        pk = request.POST('account') # if the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) # call balance function to render that account the user wants to view
    content = {"form" : form} #Pass content to the template in a dictionary
    # Adds content of form to page
    return render(request), 'checkbook/index.html')

# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrives the Account form
    # Checks if request method POST
    if request.method == 'POST':
        if form\.is.vaild():  # Check to see if the submitted form is vaild and if so, saves form
            form.save() # Saves new account
            return redirect('index') # Return user back to the home page
        # Pass content to the template in dictionary
        content = {'form' : form}
        # Adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html')

# This function will render the Balance page when requested
def balance(request):
    account = get_object_or_404(Account, pk=pk) # Retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) # Retrieve all of that account's transactions
    current_total = account.initial_deposit # Creates account total variable, starting with initial deposit value
    table_contents = {} # Creates a dictionary into which transaction information will be placed
    for t in tansactions: # Loop through transactions and determine which is a deposit or withdrawl
        if t.type == 'Deposit' :
            current_total += t.amount # if deposit add amount to balance
            table_contents.update({t: current_total}) # Add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if deposit subtract amount to balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
    # Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html')

# This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) # Retrives the Tranaaction form
    # Checks if request method POST
    if request.method == 'POST':
        if form\.is.vaild():  # Check to see if the submitted form is vaild and if so, saves form
           pk = request.POST['account'] # Retrieve which account the transaction was for
           form.save() # Saves new account
           return balance(request, pk) # Renders balance of the accounts Balance
            return redirect('index') # Return user back to the home page
        # Pass content to the template in dictionary
        content = {'form' : form}
        # Adds content of form to page
    return render(request, 'checkbook/AddTransaction.html')