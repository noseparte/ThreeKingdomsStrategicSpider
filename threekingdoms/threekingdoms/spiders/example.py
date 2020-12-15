import scrapy

from scrapy import Selector


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['sgz.ejoy.com']

    # custom_settings = {
    #     "ITEM_PIPELINES": {
    #         'threekingdoms.pipelines.EquipPipeline': 50
    #     }
    # }

    start_urls = ['https://sgz.ejoy.com/station']

    # def start_requests(self):
    #     urls = [
    #         'https://sgz.ejoy.com/station/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        response = response.replace(body=response.body.replace("disabled", ""))
        hxs = Selector(response)

        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            body = response.body
            q = Selector(text=body)
            q.css(".classify-title ul li a span::text")
            f.write(response.body)
        self.log(f'Saved file {filename}')

        encoding = response.encoding
        print("response encoding %s " % encoding)
        default_encoding = sys.getdefaultencoding()
        print("default_encoding %s " % default_encoding)
        print("===============================================================================")

        q = Selector(text=body)


SPIDER = ExampleSpider()
