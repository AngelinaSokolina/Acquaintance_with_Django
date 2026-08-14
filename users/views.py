from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Отправка приветственного письма
            send_mail(
                subject='Добро пожаловать!',
                message=f'Привет, {user.email}! Спасибо за регистрацию на нашем сайте.',
                from_email='noreply@skystore.com',
                recipient_list=[user.email],
                fail_silently=True,
            )
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})