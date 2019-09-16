from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from sign_up.forms import UserForm
from django.http import HttpResponse

User = settings.AUTH_USER_MODEL


# Create your views here.
def index(request):
    return HttpResponse("메인페이지입니다.")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'sign_up/register_done.html', {'new_user': user_form})
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'sign_up/register.html', {'user_form': user_form})

