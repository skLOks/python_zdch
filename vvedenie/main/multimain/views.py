from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, **inters):
	a = [i for i in inters.keys()]
	b = [i for i in inters.values()]
	res = ""
	for i in range(len(a)):
		res += f"{a[i]}: {b[i]}<br>"
		


	return HttpResponse(f"""Имя: Хохряков Илья
						<p> {res}</p>""")

def about(request):
	return HttpResponse("Приехал из Челябинской области город Усть-Катав <br> успееваемость средняя, аттестат без 3 <br> не люблю учиться")

def getcontacts(request):
	return HttpResponse("Ссылка на GitHub - <a href='https://github.com/skLOks'>https://github.com/skLOks</a><br>Telegram - <a href='https://t.me/Iluhahohruakov'>https://t.me/Iluhahohruakov</a><br>Номер телефона - +7 919-303-9322")