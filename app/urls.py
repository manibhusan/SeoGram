from django.conf.urls import url
from django.urls import path, re_path
from . import views
from .views import Detail

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about-us/', views.AboutUsView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    # path('blog/', views.BlogView.as_view(), name='blog_pagination'),
    path('contact/', views.ContactUs.as_view(), name='contact'),
    path('blog-detail/', views.BlogDetailsView.as_view(), name='blog_details'),
    path('contact-us/', views.ContactusView.as_view(), name="contact_us"),
    path('leave-comment/', views.CommentView.as_view(), name='leave_comment'),
    path('news-letter/', views.NewsletterView.as_view(), name='news_letter'),
    # path('search/', views.search, name="search"),
    re_path('detail/(?P<pk>\d+)/', views.Detail.as_view(), name='detail'),
    re_path('category/(?P<pk>\d+)/', views.CategoryView.as_view(), name='catogory'),
    path('blog-list/', views.BlogListView.as_view(), name='blog'),
    path('results/', views.SearchView.as_view(), name='search'),


    # url(r'^blog-detail/', Detail.as_view()),
    # url(r'^details/(?P<pk>\d+)/(?P<title>\d+)/$', Detail.as_view()),
    # url(r'^(?P<title>\d+)|/$', Detail.as_view()),

]
