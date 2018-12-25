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


class ConnectivitySerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        self.routers_name = []
        super(ConnectivitySerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Router
        fields = ('id', 'router_name', 'card', 'neighbour_data',)

    def prepare_connectivity_data(self, data):
        pass

    card = CardSerializer(many=True, read_only=True)

    def to_representation(self, value):
        routers = super(ConnectivitySerializer, self).to_representation(value)

        nodes = []
        connections = []
        for router in [routers] if not isinstance(routers, list) else routers:
            if routers['router_name'] not in self.routers_name:
                nodes.append({'id': router['router_name'], 'name': router['router_name']})
                self.routers_name.append(router['router_name'])

            for card in router['card']:
                for interface in card['interface']:
                    if interface['connected_router']:
                        connections.append({'sid': router['router_name'],
                                            'tid': interface['connected_router']
                                            }
                                           )
                        if interface['connected_router'] not in self.routers_name:
                            nodes.append({'id': interface['connected_router'], 'name': interface['connected_router']})
                            self.routers_name.append(interface['connected_router'])

        routers.pop('card', None)
        routers.update({'nodes': nodes, 'links': connections})
        return routers
