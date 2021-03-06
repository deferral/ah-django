from rest_framework import serializers

from .models import Favorite


class FavoriteInputSerializer(serializers.ModelSerializer):
    """
    Input serializer for favorite article
    """

    class Meta:
        model = Favorite
        fields = ('article', 'user')


class FavoriteInfoSerializer(serializers.BaseSerializer):
    """
    Serializer for displaying article slug
    """

    def to_representation(self, obj):
        return {
            'article': obj.article.slug,
        }
