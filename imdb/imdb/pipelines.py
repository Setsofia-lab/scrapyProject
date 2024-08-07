# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import sqlite3


class MongodbPipeline:
    collection_name = "best_moviez"
        
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://user1:Wk8DOsZb2anQezek@webscrapingproject.pnmj9lc.mongodb.net/")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item

class SQLitePipeline:
        
    def open_spider(self, spider):
        self.connection = sqlite3.connect("imdb.db")
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE best_moviez(
                title TEXT, 
                year TEXT,
                duration TEXT,
                genre TEXT,
                rating TEXT,
                movie_url TEXT
            ) 
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute('''
             INSERT INTO best_moviez (title,year,duration,genre,rating,movie_url) VALUES(?,?,?,?,?,?)
        ''',(
            item.get('title'),
            item.get('year'),
            item.get('duration'),
            item.get('genre'),
            item.get('rating'),
            item.get('movie_url'),
        ))
        self.connection.commit()
        return item
    

# class ImdbPipeline(object):

#     @classmethod
#     def from_crawler(cls, crawler):
#         logging.warning(crawler.settings.get("MONGO_URI"))
        
#     def open_spider(self, spider):
#         logging.warning("SPIDER OPENED FROM PIPELINE")

#     def close_spider(self, spider):
#         logging.warning("SPIDER CLOSED FROM PIPELINE")


#     def process_item(self, item, spider):
#         return item
