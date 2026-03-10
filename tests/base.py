"""
Base test case for rubber.
"""
from django.test import TransactionTestCase

from rubber import get_rubber_config

rubber_config = get_rubber_config()


class BaseTestCase(TransactionTestCase):

    def setUp(self):
        super().setUp()
        self.rubber_config = rubber_config

    def refresh(self):
        rubber_config.es.indices.refresh('_all')

    def docExists(self, obj, indexer_index, doc_id=None):
        doc = obj.get_es_doc(indexer_index)
        if doc is not None:
            return True
        else:
            return False

    def aliasExists(self, index, name):
        return rubber_config.es.indices.exists_alias(
            index=index, name=name)

    def indexExists(self, index):
        return rubber_config.es.indices.exists(index=index)

    def assertAliasExists(self, index, name):
        self.assertTrue(self.aliasExists(index, name))

    def assertAliasDoesntExist(self, index, name):
        self.assertFalse(self.aliasExists(index, name))

    def assertIndexExists(self, index):
        self.assertTrue(self.indexExists(index))

    def assertIndexDoesntExist(self, index):
        self.assertFalse(self.indexExists(index))

    def assertDocExists(self, obj, indexer_index):
        self.assertTrue(self.docExists(obj, indexer_index))

    def assertDocDoesntExist(self, obj, indexer_index):
        self.assertFalse(self.docExists(obj, indexer_index))

    def createIndex(self, index):
        rubber_config.es.indices.create(index=index)
        self.refresh()

    def deleteIndex(self, index):
        rubber_config.es.indices.delete(index=index, ignore=404)
        self.refresh()
