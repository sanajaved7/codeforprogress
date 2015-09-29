from django.shortcuts import render
from .models import Person

def home(request):
	person = Person.objects.get(first_name="a")
	
	# addperson = Person.objects.create(first_name="Nicki", last_name="Minaj", about_me="The best ever.")
	
	# addperson.save()

	peoplelist = Person.objects.all()

	homeText = "some text"
	context = {'person': person, "peoplelist": peoplelist, "sometext": homeText}

	return render(request=request, template_name='home.html', context=context)

def about(request):
	about_text = "hi hello yes wee!"
	context = {"about_text": about_text}
	return render(request=request, template_name='about.html', context=context)

def page2(request):
	return render(request, 'page2.html', {})

def page3(request):
	return render(request, 'page3.html', {})