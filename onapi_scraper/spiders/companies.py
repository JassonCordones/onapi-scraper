from onapi_scraper.items import OnapiScraperItem
import string
import scrapy
import urllib.parse
import logging
logger = logging.getLogger('mycustomlogger')
class CompaniesSpider(scrapy.Spider):
    name = 'companies'
    base_url = f'https://www.onapi.gob.do/busquedas/api/signos/'
    chars = string.printable
    i = 0
    page = 1
    ids = []
    params = {
        'tipoBusqueda': 0,
        'texto': chars[i],
        'tipo': 'NO/NO',
        'clase': 0,
        'pgSize': 10,
        'pgIndex': page
    }
    params2 = {
        'id':''
    }
    def start_requests(self): 
        url = f'{self.base_url}paged?{urllib.parse.urlencode(self.params)}'
        request = scrapy.Request(url=url, callback=self.parse)
        yield request

    def parse(self, response):
        logger.info('Parse function called on % s', response.url)
        jsonresponse = response.json()
        if len(jsonresponse['data']) != 0:
            for i in range(len(jsonresponse['data'])):
                q = self.params2
                q['id'] = jsonresponse['data'][i]['Id']
                url = f'{self.base_url}detalle?{urllib.parse.urlencode(q)}'
                request = scrapy.Request(url, callback=self.parse_details)
                yield request
            self.page += 1 
            p = self.params
            p['pgIndex'] = self.page
            url = f'{self.base_url}paged?{urllib.parse.urlencode(p)}'
            request = scrapy.Request(url, callback=self.parse, dont_filter=True)
            yield request
        else:
            self.i += 1
            self.page = 1
            p = self.params
            p['texto'] = self.chars[self.i]
            p['pgIndex'] = self.page
            url = f'{self.base_url}paged?{urllib.parse.urlencode(p)}'
            request = scrapy.Request(url, callback=self.parse, dont_filter=True)
            yield request
        

    def parse_details(self, response):
        item = OnapiScraperItem()
        jsonresponse = response.json()
        item['Certificado']     = jsonresponse['data']['Certificado']
        item['Tipo']            = jsonresponse['data']['Tipo']
        item['Texto']           = jsonresponse['data']['Texto']
        item['Clases']          = jsonresponse['data']['Clases']
        item['Actividad']       = jsonresponse['data']['Actividad']
        item['Expedicion']      = jsonresponse['data']['Expedicion']
        item['Id']              = jsonresponse['data']['Id']
        item['Estado']          = jsonresponse['data']['Estado']
        item['EnTramite']       = jsonresponse['data']['EnTramite']
        item['Domicilio']       = jsonresponse['data']['Domicilio']
        item['Titular']         = jsonresponse['data']['Titular']
        item['Gestor']          = jsonresponse['data']['Gestor']
        item['Vencimiento']     = jsonresponse['data']['Vencimiento']
        item['Serie']           = jsonresponse['data']['Serie']
        item['Numero']          = jsonresponse['data']['Numero']
        item['Secuencia']       = jsonresponse['data']['Secuencia']
        item['TipoExpediente']  = jsonresponse['data']['TipoExpediente']
        item['Expediente']      = jsonresponse['data']['Expediente']
        item['ListaClases']     = jsonresponse['data']['ListaClases']

        return item 
        #           {'id':response.meta['id'],
        #         'texto': response.meta['texto'],
        #         'pagina': response.meta['page'],
        #         'details':jsonresponse['data']
        #         }
