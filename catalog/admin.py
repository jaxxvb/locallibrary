from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class AuthorInLine(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [AuthorInLine,
               ]
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    inlines = [BookInstanceInLine]
    list_filter = ('author', 'language', 'genre')


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('id', 'book', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
