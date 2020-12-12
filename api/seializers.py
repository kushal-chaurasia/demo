from rest_framework import serializers

class CardSerializeer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    card_no = serializers.IntegerField()
    expiry = serializers.DateField()
    cvv = serializers.IntegerField()
