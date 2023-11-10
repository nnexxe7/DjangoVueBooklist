from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.db.models import Q


def search(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
    results = []
    for book in books:
        results.append(
            {
                "name": book.name,
                "author": book.author,
                "image": book.image.url,
                 # Tu sie potem doda wiecej informacji
            }
        )
    return JsonResponse({"results": results})

def get_book_details(request, book_name, book_author):
    try:
        book = Book.objects.get(name=book_name, author=book_author)
        book_details = {
            "name": book.name,
            "author": book.author,
            "image": book.image.url,
            # Tu sie potem doda wiecej informacji
        }
        return JsonResponse(book_details)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)