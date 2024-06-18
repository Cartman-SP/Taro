from rest_framework import serializers
from .models import TelegramUser

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('user_id', 'username', 'usertag', 'sub_date')

    def create(self, validated_data):
        return TelegramUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.username = validated_data.get('username', instance.username)
        instance.usertag = validated_data.get('usertag', instance.usertag)
        instance.sub_date = validated_data.get('sub_date', instance.sub_date)
        instance.save()
        return
