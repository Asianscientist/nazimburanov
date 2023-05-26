from rest_framework import serializers
from .models import Posts, BooksModel, VideoModel



class PostSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Posts.MY_CHOICES)
    picture = serializers.ImageField()
    class Meta:
        model = Posts
        fields = ['title', 'title_en', 'title_uz', 'text', 'text_en', 'text_uz', 'picture', 'category', 'category_en', 'category_uz']
        extra_kwargs = {'title_en':{'required':True}, 'title_uz':{'required':True}, 'text_en':{'required':True}, 'text_uz':{'required':True}, \
                        'category_en':{'required':True}, 'category_uz':{'required':True}, }

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