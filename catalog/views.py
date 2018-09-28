from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    yoba_books = Book.objects.filter(title__contains='yoba')
    number_yoba_books = Book.objects.filter(title__contains='yoba').count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'yoba_books': yoba_books, 'number_yoba_books': number_yoba_books, 'num_visits': num_visits},
        # num_visits appended,
    )


class BookListView(generic.ListView):
    model = Book
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is dome data'
        return context


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is dome data'
        return context


class AuthorDetailedView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailedView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is dome data'
        return context
