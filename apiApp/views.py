import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"
    response = requests.get(url)
    if request.method == "GET":
        if response.status_code == 200:
            page = response.text
            soup = BeautifulSoup(page, 'html.parser')
            main = soup.findAll("div", class_="pollutant-item")
            # print(main)
            pollutant_data = []
            for div in main:
                div.find()
                name = div.find("div", class_="name").get_text()
                value = div.find("div", class_="value").get_text()
                pollutant_data.append({"name":name,"value":value})

            return JsonResponse({"code":200, "status":True,"data":pollutant_data}, safe=False)
        else:
            return JsonResponse({"code":500, "error":"Something went wrong while scrapping the data."})
    else:
        return JsonResponse({"code":405, "error":"Method Not Allowed"})
