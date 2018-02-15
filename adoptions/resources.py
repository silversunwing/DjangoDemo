from tastypie.resources import ModelResource
from adoptions.models import Pet
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = Pet.objects.all()
        resource_name = 'pet'
        authorization = Authorization()
        fields = ['id','name','sex','species','age','breed','description','submission_date','submitter']