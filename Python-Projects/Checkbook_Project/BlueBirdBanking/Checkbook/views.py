from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

def home(request):
    form = TransactionForm(data=request.POST or None) #Retrieve the transaction form
    #checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account'] #if the form is submitted, retrieve which account
        #the user wants to view
        return balance(request, pk) #call balance function to render that account's Balance Sheet
    content = {'form': form} #saves content to the template as a dictionary
    #adds content of form to page
    return render(request, 'checkbook/index.html', content)

# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) #Retrieve the account form
    #checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #checks whether the form is valid and if so, it saves it
            form.save() #saves new account
            return redirect('index') #returns user back to the home page
    content = {'form': form} #saves content to the template as a dictionary
    #adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

#This function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #retrieve requested account using its pk
    transactions = Transaction.Transactions.filter(account=pk) #retrieve all of that accounts transactions
    current_total = account.initial_deposit #create account total var, starting with initial deposit value
    table_contents = {} #Create a dictionary into which transaction info will be placed
    for t in transactions: #loop thru transactions and determine which is a deposit/withdrawal
        if t.type == 'Deposit':
            current_total += t.amount #if deposit, add amount to balance
            table_contents.update({t: current_total}) #add transaction and total to the dictionary
        else:
            current_total -= t.amount #if withdrawal subtract amount from balance
            table_contents.update({t: current_total}) #add trans. and total to dict.
    #Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

#This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) #retrieves the transaction form
    #checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account'] #retrieve which account the transaction was for
            form.save()
            return balance(request, pk) #upon adding a new transaction, user is redirected to the balance sheet
    #pass content to the template in the dictionary
    content = {'form': form}
    #adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
