"""
.. module:: newhart.account.views
   :platform: Unix, Windows
   :synopsis: Views module for account app.

.. moduleauthor:: info@gahan-corporation.com
"""
# pylint: disable=no-member,invalid-name
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView

from account.models import Account
from account.models import AccountForm

# Create your views here.


def index(request):
    """Render the index for the account app.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    :raises: AttributeError, KeyError
    """
    context = {'accounts': Account.objects.all().order_by('number').values()}
    if request.method == "POST":
        formset = AccountForm(
            request.POST,
        ).as_table()
        if formset.is_valid():
            formset.save()
    else:
        formset = AccountForm().as_table()

    context.update({'formset': formset})
    return render(request, 'account/account.html', context)


def delete(request, account_id):
    """Delete an account and all related data.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    """
    Account.objects.filter(id=account_id).delete()
    print(request)

    return redirect('accounts_list')


class AccountUpdate(FormView):
    """Generic view for updating Account."""

    #: This view references the Account model.
    model = Account
    #: Only list number and name fields.
    fields = [
        'number', 'name'
    ]
    #: Set the template file name suffix.
    template_name_suffix = '_update'
