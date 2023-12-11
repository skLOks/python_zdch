from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):


	data = {
		"PlaceOfSudy": "Алабуга Политех",
		"Group": "Python 1",
		"Specialization": "Младший специалист",
		"InfoForMe": "Хочу стать Java разработчиком приложений для Android"
	}
	return render(request, "index.html", context=data)

def about(request):

	data = {
		"FIO": "Хохряков Илья Сергеевич",
		"Height": 175,
		"Weight": 60,
		"Age": 16
	}
	return render(request, "about.html", context=data)

def contacts(request):

	data = {
		"Номер телефона:": "+79193039322",
		"Телеграмм:": "@Iluhahohruakov",
	}
	return render(request, "contacts.html", {"data": data.keys(), "values": data.values()})

def form(request):
	return render(request, "form.html")