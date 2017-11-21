# coding=utf-8
# Napisz prosty czytnik RSS. Program ma mieć możliwość zapisywania ulubionych kanałów.
# Wiadomości powinny być czytelnie sformatowane.
import urllib2
from xml.dom import minidom


class RSSReader:
    def __init__(self):
        pass

    ulubione = []

    def pokaz(self, address):
        response = urllib2.urlopen(address)
        doc = minidom.parseString(response.read())
        rsstitle = doc.getElementsByTagName("title")[0].firstChild.data
        rssdescription = doc.getElementsByTagName("description")[0].firstChild.data
        header = "################################################################################################\n" \
                 "RSS Title: %s\n" \
                 "RSS Description: %s\n" \
                 "################################################################################################\n" \
                 % (rsstitle, rssdescription)
        print header
        elements = doc.getElementsByTagName("item")
        for element in elements:
            title = element.getElementsByTagName("title")[0].firstChild.data
            description = element.getElementsByTagName("description")[0].firstChild.data
            link = element.getElementsByTagName("link")[0].firstChild.data
            date = element.getElementsByTagName("pubDate")[0].firstChild.data
            message = "Title: %s\n" \
                      "Description: %s\n" \
                      "Link: %s\n" \
                      "Publication date: %s\n" \
                      % (title, description, link, date)
            print message

    def dodajdoulubionych(self, address):
        self.ulubione.append(address)

    def pokazulubione(self):
        for ulubiony in self.ulubione:
            self.pokaz(ulubiony)


czytnik = RSSReader()
czytnik.pokaz("http://feeds.bbci.co.uk/news/rss.xml")
czytnik.dodajdoulubionych("http://feeds.bbci.co.uk/news/rss.xml")
czytnik.pokaz("https://feeds.howtogeek.com/howtogeek")
czytnik.dodajdoulubionych("https://feeds.howtogeek.com/howtogeek")
czytnik.pokazulubione()
