
from rest_framework import serializers 
from .models import Rating 
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User 
 
 
class RatingSerializer (serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField( 
    queryset=User.objects.all(), 
    default=serializers.CurrentUserDefault() 
    ) 
    class Meta():
        model = Rating
        fields = ['user','menuitem_id', 'rating']
        # validators below was explained differently in the instructions than it ended up being in the examplar.  
        # 'a fields variable that contains three list elements that are strings like: user, menuitem_id and rating  '
        # the instructions said to add user, menuitem_id and rating the fields list, but that did not work as shown.  
        # The examplar showed the below code.
        validators = [UniqueTogetherValidator(queryset = Rating.objects.all(),fields = ['user', 'menuitem_id'])]
        extra_kwargs = {'rating':{'max_value':5,'min_value':0}}
