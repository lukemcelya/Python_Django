from django.contrib import admin
from post_app.models import BlogPost
from registration.models import Registration

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Registration)