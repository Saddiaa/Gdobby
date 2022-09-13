from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# from todoapp.models import todo
from django.core.mail import send_mail
# Create your views here.
# def index(request):
#     Todo=todo.objects.all()
#     if request.method=='POST':
        
#         book=todo(title=request.POST.get('title'))
#         book.save()
#         return redirect('/')
#     return render(request,'index.html', {'Todo' : Todo })

def contact_form(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Subject:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        send_mail('You got a mail!', message, '', ['sadiyasha14@gmail.com']) # TODO: enter your email address
        
    return render(request, 'content.html', {})

def index(request):
    
    return render(request,'article.html', {})