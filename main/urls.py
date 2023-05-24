from django.urls import path

from main.apps import MainConfig
from main.views import IndexView, ContactView, BlogListView, BlogDetail, CommentCreateView, BlogCreateView, \
    BlogUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='article'),
]
