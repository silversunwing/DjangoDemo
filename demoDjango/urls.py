
from django.conf.urls import url, include
from django.contrib import admin

from adoptions import views
from adoptions.resources import NoteResource

note_resource = NoteResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home, name='home'),
    url(r'^adoptions/(\d+)/',views.pet_detail,name='pet_detail'),
    url(r'^adoptions/', include(note_resource.urls)),
]
