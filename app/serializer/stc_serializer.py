from rest_framework import serializers

from app.models.models import (
    Router,
    Card,
    Interface
)


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ('card', 'local_interface', 'remote_interface', 'status', 'connected_router',)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('slot_number', 'card_name', 'interface',)

    interface = InterfaceSerializer(many=True, read_only=True)


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = ('id', 'router_name', 'card',)

    card = CardSerializer(many=True, read_only=True)
