
from rest_framework import serializers

from .models import Advocate

class AdvocateSerializer(serializers.ModelSerializer):
    
    profile_pic = serializers.SerializerMethodField()
    class Meta:
        model = Advocate
        fields = ['username', 'name', 'bio', 'profile_pic', 'twitter']
        
    def get_profile_pic(self, obj):
        if obj.profile_pic:
            return obj.profile_pic.url
        return None
        