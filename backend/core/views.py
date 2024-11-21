from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Phrases
def index(request):
    return render(request, 'build/index.html')


@api_view(['POST'])
def savePhrase(request):
    portuguesePhrase = request.data['portuguesePhrase']
    translatedPhrase = request.data['translatedPhrase']
    if translatedPhrase == "" or portuguesePhrase == "":
        return Response({"message": "Both fields are required!"}, status=400)

    if Phrases.objects.filter(portuguesePhrase=portuguesePhrase).exists():
        return Response({"message": "This phrase already exists!"}, status=400)

    if Phrases.objects.filter(translatedPhrase=translatedPhrase).exists():
        return Response({"message": "This phrase already exists!"}, status=400)


    phrase = Phrases(portuguesePhrase=portuguesePhrase, translatedPhrase=translatedPhrase)
    phrase.save()
    return Response({"message": "Phrase saved successfully!"}, status=200)


@api_view(['POST'])
def load_new_phrase(request):
    pass
