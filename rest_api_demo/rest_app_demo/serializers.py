from .models import Note
from rest_framework import serializers

"""Creating a Serializer for Note Model to indicate which fields will be parsed"""


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'note_header', 'note_body', 'is_important', 'timestamp')
