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
            }
        )
    return JsonResponse({"results": results})
