import scrapy

class GdpDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        rows = response.xpath('//table/tbody/tr')
        for row in rows:
            name = row.xpath(".//th/a/text()").get(),
            gdp = row.xpath(".//td[2]/text()").get()
            yield{
                'country_name':name,
                'GDP':gdp
            }
        
        

