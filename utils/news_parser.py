import requests
from bs4 import BeautifulSoup

from typing import List, Dict

from messages import MESSAGES
from conf import NEWS_LINK, SALES_LINK, SPARE_PARTS_LINK, EVENTS_LINK, ADDRESS_LINK, TECH_LINK


class NewsParser:
    news_link = NEWS_LINK
    sales_link = SALES_LINK
    spare_parts_link = SPARE_PARTS_LINK
    events_link = EVENTS_LINK
    address_link = ADDRESS_LINK
    tech_link = TECH_LINK

    def get_news(self) -> List[Dict[str, str]]:
        r = requests.get(self.news_link)
        soup = BeautifulSoup(r.text, 'xml')
        news = []
        for post in soup.find_all('post')[:3]:
            n = {
                'title': f"<b>{post.find('Title').text}</b>",
                'excerpt': post.find('Excerpt').text,
                'permalink': post.find('Permalink').text,
                'date': post.find('Date').text,
                'img': post.find('ImageFeatured').text
            }
            if n['excerpt'] == '':
                n.pop('excerpt')

            news.append(n)
        return news

    def get_sales(self) -> List[Dict[str, str]]:
        r = requests.get(self.sales_link)
        soup = BeautifulSoup(r.text, 'xml')
        sales = []
        for sale in soup.find_all('post'):
            s = {
                'title': f"<b>{sale.find('Title').text}</b>",
                'excerpt': sale.find('Excerpt').text,
                'permalink': sale.find('Permalink').text,
                'img': sale.find('ImageFeatured').text
            }
            if s['excerpt'] == '':
                s.pop('excerpt')
            sales.append(s)
        return sales

    def get_spare_part(self, part_mark: str) -> (Dict[str, str], str):
        r = requests.get(self.spare_parts_link)
        soup = BeautifulSoup(r.text, 'xml')
        parts = soup.find_all('post')
        parts_skus = [p.text for p in soup.find_all('Sku')]
        parts_names = [p.text.lower() for p in soup.find_all('Title')]
        if part_mark in parts_skus:
            detail_ind = parts_skus.index(part_mark)
            post = parts[detail_ind]
        elif part_mark.lower() in parts_names:
            detail_ind = parts_names.index(part_mark.lower())
            post = parts[detail_ind]
        else:
            return MESSAGES['part_not_found']
        detail = {
            'title': f"✅Запчасть в наличии. Можете оформить заказ на сайте\n\n<b>{post.find('Title').text}</b>",
            'sku': f'Артикул: {post.find("Sku").text}',
            'price': f'Цена: {post.find("Price").text[:-3]} ₽',
            'permalink': post.find('Permalink').text,
            'img': '-'
        }
        return detail

    def get_events(self) -> List[Dict[str, str]]:
        r = requests.get(self.events_link)
        soup = BeautifulSoup(r.text, 'xml')
        events = []
        for event in soup.find_all('post'):
            s = {
                'title': f"<b>{event.find('Title').text}</b>",
                'excerpt': event.find('Excerpt').text,
                'permalink': event.find('Permalink').text,
                'img': event.find('ImageFeatured').text
            }
            if s['excerpt'] == '':
                s.pop('excerpt')
            events.append(s)
        return events

    def get_address(self) -> Dict[str, dict]:
        r = requests.get(self.address_link)
        soup = BeautifulSoup(r.text, 'xml')
        address = {}
        for event in soup.find_all('post'):
            a = {
                'title': f"<b>{event.find('Title').text}</b>",
                'address': event.find('Address').text,
                'phone': event.find('Phone').text,
                'time': event.find('Time').text,
                'yandex_link': event.find('YandexLink').text
            }
            address[event.find('ID').text] = a
        return address

    def get_tech(self) -> Dict[str, dict]:
        r = requests.get(self.tech_link)
        soup = BeautifulSoup(r.text, 'xml')
        tech = {}
        for event in soup.find_all('post'):
            a = {
                'content': event.find('Content').text,
                'img': event.find('ImageFeatured').text,
            }
            tech[event.find('ID').text] = a
        return tech
