from django.views.decorators.http import require_GET
from django.http import JsonResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Create your views here.
@require_GET
def greetings(request):
    name = str(request.GET.get("visitor_name")).strip('"')
    ip = request.META.get("REMOTE_ADDR")
    if not ip:
        ip = request.META.get("HTTP_X_FORWARDED_FOR")

    city_response = requests.get(
        f"https://ipinfo.io/json?token={os.getenv('IPINFO_TOKEN')}"
    )
    city = city_response.json().get("city")
    ip = city_response.json().get("ip")

    temp_response = requests.get(
        f"http://api.weatherapi.com/v1/current.json?q={city}&key={os.getenv('WEATHERAPI_KEY')}"
    )
    temperature = temp_response.json().get("current").get("temp_c")

    context = {
        "client_ip": ip,
        "location": city,
        "greeting": f"Hello, {name}!, the temperature is {temperature} degrees Celcius in {city}",
    }
    return JsonResponse(context)
