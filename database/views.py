from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import journal

# Create your views here.

@api_view(['POST'])
def addJournal(request):
    try:
        newJournal = journal(
            authorName = request.data['authorName'],
            title = request.data['title'],
            typeOfPublication = request.data['typeOfPublication'],
            publisher = request.data['publisher'],
            isbn = request.data['isbn'],
            yearOfPublication = request.data['yearOfPublication'],
            doi = request.data['doi'],
        )
        newJournal.save()
        return JsonResponse({
            "status" : "success",
            "msg" : "Journal Added Successfully"
        })

    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "msg" : str(e)
        })


@api_view(['GET'])
def getJournals(request):
    try:
        journals = journal.objects.all()
        response = []

        i = 0
        # Creates a list of objects as response
        while i < journals.count():
            entry = {}
            entry["authorName"] = journals[i].authorName
            entry["title"] = journals[i].title
            entry["typeOfPublication"] = journals[i].typeOfPublication
            entry["publisher"] = journals[i].publisher
            entry["isbn"] = journals[i].isbn
            entry["yearOfPublication"] = journals[i].yearOfPublication
            entry["doi"] = journals[i].doi
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": str(e) })