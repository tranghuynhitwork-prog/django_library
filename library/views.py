# library/views.py
from django.shortcuts import render
from .models import Sach, TheLoai

def book_list(request):
    the_loai_id = request.GET.get('the_loai')
    sachs = Sach.objects.all().order_by('-id')

    if the_loai_id:
        sachs = sachs.filter(the_loai_id=the_loai_id)

    context = {
        'sachs': sachs,
        'danh_sach_the_loai': TheLoai.objects.all(), 
        'selected_the_loai': int(the_loai_id) if (the_loai_id and the_loai_id.isdigit()) else None,
    }
    return render(request, 'library/book_list.html', context)