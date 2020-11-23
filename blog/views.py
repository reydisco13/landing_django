from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings  # RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def home(request):
    my_services = MyService.objects
    experiences = Experience.objects
    prices = Price.objects
    titles = Title.objects.get(pk=1)
    # form
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            number = form.cleaned_data['number']
            send_mail('На консультацию', f'Имя: {name}; Почта: {from_email}; Номер:{number}',
                      settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
            # return redirect('success')
        else:
            return HttpResponse('Неверный запрос.')
    return render(request, 'blog/home.html', {'titles': titles,
                                              'my_services': my_services,
                                              'experiences': experiences,
                                              'prices': prices,
                                              'form': form,
                                              }
                  )

# def success_view(request):
#     return HttpResponse('Приняли! Спасибо за вашу заявку.').

