from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NoteSerializers
from .models import Note
from rest_framework import filters
import django_filters.rest_framework

"""Using notes Manager on Model Note to query data"""
"""Using Serializer to parse as JSON data format"""


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.notes.all().order_by('-timestamp')
    serializer_class = NoteSerializers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('is_important', )
    ordering = ('-timestamp')


"""
# Filtering Only important Notes by using filter() func with is_important filed == True


class ImportantNoteSet(viewsets.ModelViewSet):
    queryset = Note.notes.all().order_by('-timestamp').filter(is_important=True)
    serializer_class = NoteSerializers


# Filtering the non essential notes


class NonImportantNoteSet(viewsets.ModelViewSet):
    queryset = Note.notes.all().order_by('-timestamp').filter(is_important=False)
    serializer_class = NoteSerializers
"""
