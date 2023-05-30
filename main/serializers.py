from rest_framework import serializers
from .models import Posts, BooksModel, VideoModel



class PostSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Posts.MY_CHOICES)
    picture = serializers.ImageField()
    class Meta:
        model = Posts
        fields = "__all__"
class BookSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        max_length=10000000,
        allow_empty_file=False,
        use_url=False,)
    class Meta:
        model = BooksModel
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    video = serializers.FileField()
    class Meta:
        model = VideoModel
        fields = ['title', 'video', 'text']