from django.shortcuts import render
from django.shortcuts import redirect

from .models import Category
from .forms import CategoryForm

# Create your views here.


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(
        request,
        'categories/category_list.html',
        context
    )


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            return redirect('category_list')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(
        request,
        'categories/category_create.html',
        context
    )