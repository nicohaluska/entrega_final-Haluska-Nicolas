
# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)

from django.contrib import admin
from .models import Post, Comentario

admin.site.register(Comentario)