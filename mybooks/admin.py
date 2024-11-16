from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'isbn', 'pages', 'languages', 'genre')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('languages', 'genre')
    
admin.site.register(Book, BookAdmin)
