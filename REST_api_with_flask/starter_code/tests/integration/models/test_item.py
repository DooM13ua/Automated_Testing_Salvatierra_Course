from Automated_Testing.REST_api_with_flask.starter_code.models.item import ItemModel
from Automated_Testing.REST_api_with_flask.starter_code.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app.app_context():
            item = ItemModel('test', 19.99)

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 f"Found an item with name, but expected not to.".format(item.name))
            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))