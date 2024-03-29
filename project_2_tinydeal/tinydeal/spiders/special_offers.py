import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["web.archive.org"]
    start_urls = ["https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html"]
    
    def parse(self, response):
        all_products = response.xpath("//ul[@class='productlisting-ul']/div/li")
        for product in all_products:
            yield{
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': product.xpath(".//a[@class='p_box_title']/@href").get(),
                'discounted_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get()
            }
        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)