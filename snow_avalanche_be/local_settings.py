import json
import os
from django.core.exceptions import ImproperlyConfigured


class SettingUtils:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(BASE_DIR, 'config/cnf.json')) as secrets_file:
            self.secrets = json.load(secrets_file)

    def get_data(self, setting_key):
        """Get secret setting or fail with ImproperlyConfigured"""
        try:
            return self.secrets[setting_key]
        except KeyError:
            raise ImproperlyConfigured("Set the {} setting".format(setting_key))


CONNECTION_KEY_TESTS = {
    'PUCIT_CAMPUS': {
        'DB_KEY': 'pucit_campus',
        'APPS': ['db_campus_migration'],
        'MODELS': [],
        'TABLES': []
    },

    'DEFAULT': {
        'DB_KEY': 'default',
        'APPS': [],
        'MODELS': [],
        'TABLES': []
    }
}

MODEL_FIELD_TYPES = {
    "spatial": ['GeometryField', 'PointField', 'LineStringField', 'PolygonField',
                'MultiPointField', 'MultiLineStringField', 'MultiPolygonField',
                'GeometryCollectionField', 'RasterField'],
    "number": ['AutoField', 'BigAutoField', 'BigIntegerField', 'DecimalField', 'DurationField', 'FloatField',
               'IntegerField', 'PositiveIntegerField', 'PositiveSmallIntegerField', 'SmallIntegerField'],
    "date": ['DateField', 'DateTimeField', 'TimeField'],
    "string": ['CharField', 'EmailField', 'FilePathField', 'TextField'],
    "others": ['BinaryField', 'BooleanField', 'FileField', 'FileField and FieldFile',
               'ImageField', 'GenericIPAddressField', 'NullBooleanField', 'SlugField', 'URLField', 'UUIDField'],
    "relational": ['ForeignKey']
}
