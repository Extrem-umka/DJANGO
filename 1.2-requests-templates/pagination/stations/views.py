from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    return redirect(reverse('bus_stations'))


# with open('C:\\Users\\anton.zhulin\\Desktop\\dj-homeworks\\1.2-requests-templates\\pagination\\data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # print(row['Name'], row['Street'], row['District'])


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        l = [row for row in reader]
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(l, 10)
    page = paginator.get_page(page_number)


    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
