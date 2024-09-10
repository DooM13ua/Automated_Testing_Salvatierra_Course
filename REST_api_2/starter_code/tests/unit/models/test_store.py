from Automated_Testing.REST_api_2.starter_code.models.store import StoreModel
from Automated_Testing.REST_api_2.starter_code.tests.unit.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         "The name the store after creation does not equal the constructor argument.")
        