from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project, ContactMessage
from django.conf import settings

def home(request):
    projects = Project.objects.all()
    message_sent = False
    error_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            # Save to DB
            ContactMessage.objects.create(name=name, email=email, message=message)
            # Send email
            try:
                send_mail(
                    f'Portfolio Contact: {name} <{email}>',
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['ma.andreinagutierrez@gmail.com'],
                    fail_silently=False,
                )
                message_sent = True
            except Exception as e:
                error_message = 'Error sending email. Please try again later.'
        else:
            error_message = 'All fields are required.'
    return render(request, 'home.html', {
        'projects': projects,
        'message_sent': message_sent,
        'error_message': error_message
    })