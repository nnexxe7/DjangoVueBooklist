from django.contrib import admin
from django.urls import path
from books import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", views.search, name="search"),
    path('book/<str:book_name>/<str:book_author>/', views.get_book_details, name='get_book_details'),
    path('api/login/', users_views.login_view, name='login'),
    path('api/register/', users_views.register_view, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
