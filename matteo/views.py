from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact ,Project

def home(request):
    """Homepage con tutti i progetti"""
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'matteo/home.html', {'projects': projects})

def about(request):
    """Pagina about"""
    return render(request, 'matteo/about.html')

def portfolio(request):
    """Pagina portfolio dettagliata"""
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'matteo/portfolio.html', {'projects': projects})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Salva il messaggio nel database
            contact_message = form.save()
            
            # Invia email di notifica
            try:
                send_mail(
                    subject=f'New Contact Form Message from {contact_message.name}',
                    message=f'''
Name: {contact_message.name}
Email: {contact_message.email}
Message: {contact_message.message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                
                # Invia email di conferma all'utente
                send_mail(
                    subject='Thank you for your message - Matteo Anghileri',
                    message=f'''
Hi {contact_message.name},

Thank you for reaching out! I have received your message and will get back to you as soon as possible.

Best regards,
Matteo Anghileri
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[contact_message.email],
                    fail_silently=False,
                )
                
            except Exception as e:
                # Log dell'errore ma il messaggio viene comunque salvato
                print(f"Email error: {e}")
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'matteo/contact.html', {'form': form})