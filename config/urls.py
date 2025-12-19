from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "XIU Admin"
admin.site.site_header = "Xalqaro Innovatsion Universitet"
admin.site.index_title = "Boshqaruv paneli"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),

    # Apps
    path('', include('apps.core.urls', namespace='core')),
    path('about/', include('apps.about.urls', namespace='about')),
    path('faculties/', include('apps.faculties.urls', namespace='faculties')),
    path('education/', include('apps.education.urls', namespace='education')),
    path('admission/', include('apps.admission.urls', namespace='admission')),
    path('students/', include('apps.students.urls', namespace='students')),
    path('science/', include('apps.science.urls', namespace='science')),
    path('international/', include('apps.international.urls', namespace='international')),
    path('news/', include('apps.news.urls', namespace='news')),
    path('gallery/', include('apps.gallery.urls', namespace='gallery')),
    path('contact/', include('apps.contact.urls', namespace='contact')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)