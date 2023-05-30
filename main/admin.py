from django.contrib import admin
from .models import Posts, VideoModel, BooksModel, CertificateModel

admin.site.register(Posts)
admin.site.register(VideoModel)
admin.site.register(BooksModel)
admin.site.register(CertificateModel)

