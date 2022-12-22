from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import conference, journal, book

# Create your views here.

@api_view(['POST'])
def addConference(request):
    try:
        newconference = conference(
            authorName = request.data['authorName'],
            title = request.data['title'],
            typeOfPublication = request.data['typeOfPublication'],
            publisher = request.data['publisher'],
            isbn = request.data['isbn'],
            yearOfPublication = request.data['yearOfPublication'],
            doi = request.data['doi'],
        )
        newconference.save()
        return JsonResponse({
            "status" : "success",
            "msg" : "Conference Added Successfully"
        })

    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "msg" : str(e)
        })


@api_view(['GET'])
def getConferences(request):
    try:
        conferences = conference.objects.all()
        response = []

        i = 0
        # Creates a list of objects as response
        while i < conferences.count():
            entry = {}
            entry["authorName"] = conferences[i].authorName
            entry["title"] = conferences[i].title
            entry["typeOfPublication"] = conferences[i].typeOfPublication
            entry["publisher"] = conferences[i].publisher
            entry["isbn"] = conferences[i].isbn
            entry["yearOfPublication"] = conferences[i].yearOfPublication
            entry["doi"] = conferences[i].doi
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": str(e) })

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
            entry["titleOfManuscript"] = journals[i].titleOfManuscript
            entry["typeOfJournal"] = journals[i].typeOfJournal
            entry["titleOfJournal"] = journals[i].titleOfJournal
            entry["publisher"] = journals[i].publisher
            entry["issn"] = journals[i].issn
            entry["yearOfPublication"] = journals[i].yearOfPublication
            entry["doi"] = journals[i].doi
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": str(e) })

@api_view(['GET'])
def getBooks(request):
    try:
        books = book.objects.all()
        response = []

        i = 0
        # Creates a list of objects as response
        while i < books.count():
            entry = {}
            entry["authorName"] = books[i].authorName
            entry["title"] = books[i].title
            entry["publisher"] = books[i].publisher
            entry["isbn"] = books[i].isbn
            entry["yearOfPublication"] = books[i].yearOfPublication
            entry["doi"] = books[i].doi
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": str(e) })