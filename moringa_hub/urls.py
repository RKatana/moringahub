
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import(
    login,
    logout,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login, name='login'),
    url(r'^main/', include ('projects.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url('^logout/',logout,{'next_page':'/main/sign_out'})
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
