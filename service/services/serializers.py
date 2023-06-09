from rest_framework import serializers

from .models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.company_name")
    email = serializers.CharField(source="client.user.email")

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email')
