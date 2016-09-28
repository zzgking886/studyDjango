__author__ = 'zzg'
from zzgSystemServer.models import *
from rest_framework import serializers


class UserTableSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTable
        fields = ('userId', 'userName', 'userNickName', 'userSex')

        def restore_object(self, attrs, instance=None):
            if instance:
                instance.userId = attrs['userId']
                instance.userName = attrs['userName']
                instance.userNickName = attrs['userNickName']
                instance.userSex = attrs['userSex']
                return instance
            return UserTable(**attrs)


class VRVideoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VRVideoTable
        fields = ('videoImage', 'videoTitle', 'videoUrl')

        def restore_object(self, attrs, instance=None):
            if instance:
                instance.videoImage = attrs['videoImage']
                instance.videoTitle = attrs['videoTitle']
                instance.videoUrl = attrs['videoUrl']
                return instance
            return VRVideoTable(**attrs)