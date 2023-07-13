from rest_framework import serializers
from .models import Posts, BooksModel, VideoModel, CertificateModel

class CertificateSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField()
    file = serializers.FileField(required=False)
    class Meta:
        model = CertificateModel
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Posts.MY_CHOICES)
    picture = serializers.ImageField()
    picture2 = serializers.ImageField(required=False)
    picture3 = serializers.ImageField(required=False)
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

class VideosSerializer(serializers.ModelSerializer):
    video = serializers.URLField(max_length=200)
    class Meta:
        model = VideoModel
        fields = ['id', 'title', 'video', 'text']