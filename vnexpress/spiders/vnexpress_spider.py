import scrapy
import os.path
from vnexpress.spiders.crawl_vnexpress import parseXML


class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"

    def start_requests(self):
        urls = parseXML('thethao.xml')
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        content = response.url.split("/")[-1]
        filename = f'{content}'
        savepath = './vnexpress/data/thethao'
        complete_name = os.path.join(savepath, filename)
        with open(complete_name, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {complete_name}')