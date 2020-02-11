# -*- coding: utf-8 -*-

# This class is not used for this example.

# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BooksPipeline(object):
    def process_item(self, item, spider):
        return item
