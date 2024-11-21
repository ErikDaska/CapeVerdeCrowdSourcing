from django.shortcuts import render
from rest_framework.decorators import api_view
import random


def index(request):
    return render(request, 'build/index.html')

@api_view(['POST'])
def load_new_phrase(request):
    pass
