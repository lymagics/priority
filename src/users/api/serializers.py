from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent User model.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'about_me', 'avatar_url']
        read_only_fields = ['id', 'avatar_url']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True}
        }

    def validate_email(self, value):
        """
        Check that email value is unique.
        """
        if User.objects.filter(email=value).first() is not None:
            error = 'A user with that email already exists.'
            raise serializers.ValidationError(error)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data: dict):
        password = validated_data.pop('password', None)

        instance = super().update(instance, validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
