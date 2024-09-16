# serializers.py
from rest_framework import serializers
from .models import Complaint, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Complaint
        fields = '__all__'
