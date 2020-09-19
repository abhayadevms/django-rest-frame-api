from rest_framework import serializers

from dev_api.models import Status

'''
SERILIZER ----CONVERT THE DAT INTO JSON 
               VALIDETE THE DATA
'''
class StatusSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'

        ]
    def validate_content(self, value):
        if len(value)>10000:
            raise serializers("This is very too long")
        return value

    def validate(self, data):
        content =data.get("content", None)
        if content == "":
            content=None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("content or Image is required")
        return data

