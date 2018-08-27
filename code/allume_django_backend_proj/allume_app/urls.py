from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^faq/add/$', views.add_to_faq, name='add_to_faq'),
    url(r'^faq/view/$', views.faq, name='faq'),
    url(r'^testimonials/add/$', views.add_testimonial, name='add_testimonial'),
    url(r'^testimonials/view/$', views.testimonials, name='testimonials'),
    url(r'^', views.signup, name='signup'),
]