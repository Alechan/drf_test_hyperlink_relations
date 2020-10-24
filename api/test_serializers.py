from django.test import TestCase, override_settings
from django.urls import path

from api.models import APITestModel
from api.serializers import APITestModelSerializer

urlpatterns = [
    path('whateveryouwant/<int:pk>/', lambda request: None, name='apitestmodel-detail'),
]


@override_settings(ROOT_URLCONF=__name__)
class HyperlinkedRelatedFieldTestCase(TestCase):

    def setUp(self):
        # Populate db with APITestModel instances
        _ = APITestModel.objects.create(year=1960)
        _ = APITestModel.objects.create(year=1961)
        _ = APITestModel.objects.create(year=1962)

    def test_to_internal_value_correct_error_message(self):
        queryset = APITestModel.objects.all()
        serializer = APITestModelSerializer(queryset, many=True, context={'request': None})
        expected = [
            {'url': '/whateveryouwant/1/', 'year': 1960},
            {'url': '/whateveryouwant/2/', 'year': 1961},
            {'url': '/whateveryouwant/3/', 'year': 1962},
        ]
        self.assertEqual(serializer.data, expected)
