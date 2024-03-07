import scrapy


class BestMoviesSpider(scrapy.Spider):
    name = "best_movies"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        all_movies = response.xpath("//*[@id='__next']/main/div/div[3]/section/div/div[2]/div/ul")
        print("<_kjhgbhjhjgbhgkhkjhkjhkjhkjhkjhkjhkjlhkjkjhkjhjk_>",all_movies)
        for movies in all_movies:
        


         
            
             yield{
            'title': movies.xpath(".//li[@class='ipc-metadata-list-summary-item']/a/h3[@class='ipc-title__text']").get(),
            'year': movies.xpath(".//li/div[2]/div/div/div[2]/span[1]/text()").get(),
            'duration': movies.xpath(".//li/div[2]/div/div/div[2]/span[2]/text()").get(),
            'rating': movies.xpath(".//li/div[2]/div/div/span/div/span/text()").get(),
            'movie_url': movies.xpath("//li/div[2]/div/div/div[1]/a/@href").get()
            }

            # yield{
            # 'title': movies.xpath(".//li/div[2]/div/div/div[1]/a/h3/text()").get(),
            # 'year': movies.xpath(".//li/div[2]/div/div/div[2]/span[1]/text()").get(),
            # 'duration': movies.xpath(".//li/div[2]/div/div/div[2]/span[2]/text()").get(),
            # 'rating': movies.xpath(".//li/div[2]/div/div/span/div/span/text()").get(),
            # 'movie_url': movies.xpath("//li/div[2]/div/div/div[1]/a/@href").get()
            # }
        