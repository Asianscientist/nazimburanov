from rest_framework import serializers
from .models import Posts, BooksModel, SuggestionModel



class PostSerializer(serializers.ModelSerializer):
    MY_CHOICES = (
        ("NEWS", 'News'),
        ("ARTICLES", 'Articles'),
        ("COUNTRYIMAGE", 'Image of the Country'),
        ("SCIENTIFIC_ARTICLES", "Scientific Articles"),
        ("BOOKS", "Books"),
        ("INTERNATIONAL_PROJECTS", "International Projects"),
    )
    picture = serializers.ImageField()
    class Meta:
        model = Posts
        fields = "__all__"
        # fields = ["title", "text", "picture", "category"]

    # title = serializers.CharField(max_length=50)
    # text = serializers.CharField()
    # category = serializers.ChoiceField(choices=MY_CHOICES)
    # picture = serializers.ImageField()

    # def create(self, validated_data):
    #     title = validated_data.pop("title")
    #     text = validated_data.pop("text")
    #     category = validated_data.pop("category")
    #     picture = validated_data.pop("picture")
    #     return Posts.objects.create(picture=picture, title=title, text=text, category=category)


class BookSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        max_length=10000000,
        allow_empty_file=False,
        use_url=False,)
    class Meta:
        model = BooksModel
        fields = ["title", "text", "file"]

    def create(self, validated_data):
        file = validated_data.pop("file")
        title = validated_data.pop("title")
        text = validated_data.pop("text")
        return BooksModel.objects.create(title=title, text=text, file=file)
    
class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionModel
        fields = "__all__"