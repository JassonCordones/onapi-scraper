# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OnapiScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Certificado     = scrapy.Field()
    Tipo            = scrapy.Field()
    Texto           = scrapy.Field()
    Clases          = scrapy.Field()
    Actividad       = scrapy.Field()
    Expedicion      = scrapy.Field()
    Id              = scrapy.Field()
    Estado          = scrapy.Field()
    EnTramite       = scrapy.Field()
    Domicilio       = scrapy.Field()
    Titular         = scrapy.Field()
    Gestor          = scrapy.Field()
    Vencimiento     = scrapy.Field()
    Serie           = scrapy.Field()
    Numero          = scrapy.Field()
    TipoExpediente  = scrapy.Field()
    Secuencia       = scrapy.Field()
    Expediente      = scrapy.Field()
    ListaClases     = scrapy.Field()
