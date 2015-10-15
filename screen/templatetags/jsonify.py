from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library

register = Library()

def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return simplejson.dumps(object, cls=DjangoJSONEncoder)

register.filter('jsonify', jsonify)
