from django.contrib import admin
from .models import Category, Thread, Reply, ThreadVotes, ReplyVotes

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Reply)
admin.site.register(ThreadVotes)
admin.site.register(ReplyVotes)