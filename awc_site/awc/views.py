from django.conf import settings
from django.db.models import Q
from django.shortcuts import render

User = settings.AUTH_USER_MODEL


def shared_list(request):
    # shares = Shared.objects.all()  # 모든걸 받는다
    # return render(request, 'awc/list.html')
    return render(request, 'awc/list.html')


def shared_main(request):
    # shares = Shared.objects.all()
    return render(request, 'awc/main.html')


def shared_page(request):
    return render(request, 'awc/page.html')


def shared_notice(request):
    # shares = Shared.objects.all()
    return render(request, 'awc/notice.html', )


def shared_download(request):
    # shares = Shared.objects.all()
    return render(request, 'awc/download.html')


def shared_test(request):
    msg2 = "구조를 파악합시다"
    return render(request, 'awc/test.html', {'key': msg2})


def search_url(request):
    return render(request, 'awc/search_url.html')


def search_file(request):
    return render(request, 'awc/search_file.html')


def search_done(request, word):
    return render(request, 'awc/search_done.html', {'word': word})


def show_space(request):
    return render(request, 'space/show_space.html')


def searching(request, search_word):
    return render(request, 'awc/search_done.html')
