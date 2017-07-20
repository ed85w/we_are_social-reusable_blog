from django.contrib import admin
from .models import Subject, Thread, Post

#   adds models to admin page of django

admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)
