from testDjango.models import Book
from testDjango.models import User
from testDjango.models import UserTable
from rest_framework import serializers

# user rest_framework to connect database

class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name','userId')

    # name = serializers.CharField(max_length=100)
    # userId = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance = None):
        if instance:
            instance.name = attrs['name']
            instance.userId = attrs['userId']
            return instance
        return Book(**attrs)


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userId','nickname')

        def restore_object(self, attrs, instance = None):
            if instance:
                instance.userId = attrs['userId']
                instance.nickname = attrs['nickname']
                return  instance
            return User(**attrs)

class UserTableSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTable
        fields = ('userId','userName','userNickName','userSex')

        def restore_object(self, attrs, instance = None):
            if instance:
                instance.userId = attrs['userId']
                instance.userName = attrs['userName']
                instance.userNickName = attrs['userNickName']
                instance.userSex = attrs['userSex']
                return  instance
            return UserTable(**attrs)
