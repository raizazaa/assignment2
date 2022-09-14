from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
    'katalog_list': data_katalog_item,
    'name': 'Raizaz Achmad Asyraf',
    'student_id': '2106657815'
    }
    return render(request, "katalog.html", context)