from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import CustomUserForm
from .utils import save_custom_image
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                #Обробимо форму, що заповнив користувач
                user = form.save(commit=False)
                if 'email' in form.changed_data:
                    user.username = form.cleaned_data['email']
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    user.image_small = save_custom_image(image,size=(300,300), folder='small')
                    user.image_medium = save_custom_image(image,size=(800,800), folder='medium')
                    user.image_large = save_custom_image(image,size=(1200,1200), folder='large')
                user.save()
                login(request, user)
                return redirect('homepage')
            except Exception as e:
                print(str(e))
                messages.error(request, f'Щось пішло не так: {str(e)}')

        else:
            messages.info(request, 'Виникли помилки при заповненні форми')
    else:
        form = CustomUserForm()

    return render(request, "register.html", {"form": form})
