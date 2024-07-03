from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import openai
from .models import *
from .serializers import *
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, TelegramUser
from .serializers import OrderSerializer
import requests
from django.conf import settings
from .data import *
from horoscopes.models import *
  


def get_goroskop():
    url = "https://my-calend.ru/goroskop"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        goroskop_items = soup.find('ul', class_='goroskop-items').find_all('li')
        goroskop_dict = {}
        for item in goroskop_items:
            description_block = item.find('div', class_='goroskop-items-description')
            if description_block:
                sign_element = description_block.find('a')
                description_element = description_block.find_all('div')[-1]
                if sign_element and description_element:
                    sign = sign_element.text.strip()
                    description = description_element.text.strip()
                    goroskop_dict[sign] = description
        
        return goroskop_dict
    else:
        print(f"Ошибка при запросе страницы: {response.status_code}")
        return None
    
@api_view(['GET'])
def get_answer(request):
    cards = request.query_params.getlist('cards[]')
    print(cards)
    chosen_cards=''
    question = request.query_params.get('question')
    for i in cards:
        chosen_cards += cards_names[int(i)] +', '
    chosen_cards = chosen_cards[:-2]
    openai.api_key = 'sk-proj-gIywL2EHVCchhMVRShlPT3BlbkFJn6JZSgqWMFztSXI3XWsF'
    quest = 'сделай рассклад, вопрос на который хочу узнать ответ:' +question +' карты которые мне выпали:'+chosen_cards
    print(quest)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # или используйте "gpt-3.5-turbo" в зависимости от доступной модели
            messages=[
                {"role": "system", "content": "Ты телеграмм бот таролог, делающий рассклады на натальных картах, ты выдаёшь ответ в любом случае внезависимости от вопроса, так же называй к чему относиться каждая карта (названия карт пиши на русском)"},
                {"role": "user", "content": quest},
            ],
            

        )


        return Response({'answer':response.choices[0].message['content']}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)

    return Response({'answer':chosen_cards}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request):
    user_id = request.query_params.get('user_id')
    username = request.query_params.get('username')
    usertag = request.query_params.get('usertag')

    if not user_id or not username or not usertag:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        telegram_user = TelegramUser.objects.get(user_id=user_id)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    except TelegramUser.DoesNotExist:
        sub_date = datetime.now().date() + timedelta(days=7)
        telegram_user = TelegramUser.objects.create(user_id=user_id, username=username, usertag=usertag, sub_date=sub_date)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def get_user(request):
    user_id = request.query_params.get('user_id')
    username = request.query_params.get('username')
    usertag = request.query_params.get('usertag')

    if not user_id or not username or not usertag:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        telegram_user = TelegramUser.objects.get(user_id=user_id)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    except TelegramUser.DoesNotExist:
        sub_date = datetime.now().date() + timedelta(days=7)
        telegram_user = TelegramUser.objects.create(user_id=user_id, username=username, usertag=usertag, sub_date=sub_date)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def day_card(request):
    card = cards_names[int(request.GET.get('card'))-1]
    answer = cards_interpretations[card]
    print(answer)
    return Response({'answer':answer}, status=status.HTTP_200_OK)



@api_view(['GET'])
def yes_no(request):
    card = cards_names[int(request.GET.get('card'))-1]
    answer = cards_dict[card]
    print(answer)
    return Response({'info':answer}, status=status.HTTP_200_OK)


@api_view(['GET'])
def cards_info(request):
    card = cards_names[int(request.GET.get('card'))-1]
    name = ru_cards[int(request.GET.get('card'))-1]
    answer = tarot_cards[card]
    return Response({'info':answer,'name':name}, status=status.HTTP_200_OK)
@api_view(['GET'])

def get_goroscope_info(request):
    sign = request.GET.get('sign')
    horoscope = Horoscope.objects.get(sign=sign)
    serializer = HoroscopeSerializer(horoscope)
    return Response({'data':HoroscopeSerializer(Horoscope.objects.get(sign = sign)).data}, status=status.HTTP_200_OK)
