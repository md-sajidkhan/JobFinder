from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
import requests
import json

 
# Create your views here.
def home(request):
    return render(request, "index.html" )
    

def api(request, keyword="", location=""):
    if request.method == 'POST':
        key = request.POST.get('keyword_input')
        loc = request.POST.get('location_input')
        response = requests.get(f"https://api.adzuna.com/v1/api/jobs/in/search/1?app_id=e4ae8c31&app_key=60529b4fbb4326e82b6fd80c5fed8ab3&what={key}&what_and=fresher&where={loc}")
        values = response.json()
        value_list = []
        for i in range(10):
            quoted_company_name = json.dumps(values['results'][i]['company']['display_name']) 
            quoted_company_location = json.dumps(values['results'][i]['location']['display_name'])
            quoted_company_salary = json.dumps(values['results'][i]['salary_is_predicted'])
            quoted_company_url = json.dumps(values['results'][i]['redirect_url'])
            company_name = quoted_company_name.replace('"','')
            company_location = quoted_company_location.replace('"','')
            company_salary = quoted_company_salary.replace('"','')
            company_url_2 = quoted_company_url.replace('"','')
            company_url = company_url_2[8:]
            data = {
                'id': i+1,
            'name': company_name,
            'location': company_location,
            'salary': company_salary,
            'url': company_url
            }
            value_list.append(data)
        context = {
            'values' : value_list
            }
        return render(request, "result.html", context=context)

