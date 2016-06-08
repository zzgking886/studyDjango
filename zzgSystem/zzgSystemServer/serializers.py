__author__ = 'zzg'
from zzgSystemServer.models import UserTable
from rest_framework import serializers

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