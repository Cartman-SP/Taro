import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from horoscopes.models import Horoscope

# Ссылки на гороскопы для каждого знака
urls = {
    'aries': 'https://1001goroskop.ru/?znak=aries',
    'taurus': 'https://1001goroskop.ru/?znak=taurus',
    'gemini': 'https://1001goroskop.ru/?znak=gemini',
    'cancer': 'https://1001goroskop.ru/?znak=cancer',
    'leo': 'https://1001goroskop.ru/?znak=leo',
    'virgo': 'https://1001goroskop.ru/?znak=virgo',
    'libra': 'https://1001goroskop.ru/?znak=libra',
    'scorpio': 'https://1001goroskop.ru/?znak=scorpio',
    'sagittarius': 'https://1001goroskop.ru/?znak=sagittarius',
    'capricorn': 'https://1001goroskop.ru/?znak=capricorn',
    'aquarius': 'https://1001goroskop.ru/?znak=aquarius',
    'pisces': 'https://1001goroskop.ru/?znak=pisces'
}

# Функция для получения текста прогноза по указанной ссылке
def get_horoscope_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    description_div = soup.find('div', itemprop='description')
    if description_div:
        return description_div.get_text().strip()
    return None

class Command(BaseCommand):
    help = 'Fetch horoscopes and save them to the database'

    def handle(self, *args, **kwargs):
        for sign, url in urls.items():
            horoscope_text = get_horoscope_text(url)
            if horoscope_text:
                Horoscope.objects.update_or_create(sign=sign, defaults={'text': horoscope_text})
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved horoscopes'))
