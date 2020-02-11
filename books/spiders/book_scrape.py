# -*- coding: utf-8 -*-
import scrapy


class BookScrapeSpider(scrapy.Spider):
    name = 'book_scrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):

        #Create a selector for each book on current webpage
        books = response.xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']") 

        #Iterate through each selector to find both star rating and link
        for book in books:
            star_class = book.xpath(".//article/p/@class").get()
            star = star_class.split()[1] #Star rating
            link = book.xpath(".//article/div/a/@href").get() #Book indepth webpage link

            #For each book, follow the indepth link and callback to parse_book function, while passing on the rating
            yield response.follow(url=link, callback=self.parse_book, meta={'Star Rating' : star})

        #Link to the next page of books
        next_page = response.xpath("//li[@class='next']/a/@href").get()

        #Check if there is a next page, and if TRUE, callback parse function
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)

    def parse_book(self, response):
        #Retrieve meta data
        star = response.request.meta['Star Rating']

        #Extract book data from
        title = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        price = response.xpath("//table[@class='table table-striped']/tr[3]/td/text()").get()
        upc = response.xpath("//table[@class='table table-striped']/tr[1]/td/text()").get()
        availability = response.xpath("//table[@class='table table-striped']/tr[6]/td/text()").get()
        reviews = response.xpath("//table[@class='table table-striped']/tr[7]/td/text()").get()

        #Output book data
        yield{
            'Title' : title,
            'Price' : price,
            'UPC' : upc,
            'Availability' : availability,
            'Star Rating' : star,
            'Total Reviews' : reviews
        }
