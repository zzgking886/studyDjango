from testDjango.models import Book
from rest_framework import serializers


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name','userId')

    # name = serializers.CharField(max_length=100)
    # userId = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.name = attrs['name']
            instance.userId = attrs['userId']
            return instance
        return Book(**attrs)
