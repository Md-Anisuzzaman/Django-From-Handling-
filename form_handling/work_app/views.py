from django.shortcuts import render
from .forms import UserForm, valid_form


def work_app(request):
    return render(request, 'index.html')


def about(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        selected = request.POST.get('select_value')
        print(email, password, selected)
        return render(request, 'about.html', {'email': email, 'password': password, 'selected': selected})
    else:
        return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./work_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'contact.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'contact.html', {'form': form})


def validationForm(request):
    if request.method == 'POST':
        form = valid_form(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            print(form.cleaned_data)
            return render(request, 'validationForm.html', {'form': form})
    else:
        form = valid_form()
    return render(request, 'validationForm.html', {'form': form})


def form(request):
    return render(request, 'form.html')
