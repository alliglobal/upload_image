from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = ImageForm()


    images = Image.objects.all().order_by('-created_at')
    return render(request, 'images/upload.html', {
    'form': form,
    'images': images
    })