from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import openai


@api_view(['GET'])
def get_answer(request):
    cards_names = [
    "The Devil",
    "Ten of Pentacles",
    "King of Swords",
    "Knight of Pentacles",
    "Knight of Swords",
    "Page of Swords",
    "Queen of Swords",
    "The Magician",
    "The High Priestess",
    "Two of Wands",
    "Two of Cups",
    "Two of Swords",
    "Two of Pentacles",
    "Three of Wands",
    "Three of Cups",
    "Three of Swords",
    "Four of Wands",
    "The Emperor",
    "Four of Cups",
    "Four of Swords",
    "Five of Cups",
    "Five of Wands",
    "Five of Swords",
    "The Lovers",
    "Six of Wands",
    "Six of Cups",
    "Six of Pentacles",
    "Six of Swords",
    "The Chariot",
    "Seven of Wands",
    "Seven of Cups",
    "Seven of Swords",
    "Seven of Pentacles",
    "Strength",
    "Eight of Cups",
    "Eight of Swords",
    "Eight of Pentacles",
    "Nine of Wands",
    "Nine of Cups",
    "Nine of Swords",
    "Nine of Pentacles",
    "Ten of Wands",
    "Ten of Cups",
    "Ten of Swords",
    "Justice",
    "Page of Cups",
    "Page of Wands",
    "The Hanged Man",
    "Death",
    "Queen of Wands",
    "Queen of Pentacles",
    "Temperance",
    "The Sun",
    "The Tower",
    "The World",
    "Judgement",
    "King of Cups",
    "King of Pentacles",
    "The Hierophant",
    "King of Wands",
    "Ace of Pentacles",
    "Ace of Swords",
    "The Moon",
    "Ace of Cups",
    "Eight of Wands",
    "Ace of Wands",
    "Three of Pentacles",
    "Four of Pentacles",
    "The Star",
    "The Empress",
    "Five of Pentacles",
    "Queen of Cups",
    "Knight of Cups",
    "Knight of Wands",
    "The Hermit",
    "Page of Pentacles",
    "The Fool",
    "Wheel of Fortune"
]
    cards =  request.query_params.get('cards[]')
    chosen_cards=''
    question = request.query_params.get('question')
    for i in cards:
        chosen_cards += cards_names[int(i)] +', '
    chosen_cards = chosen_cards[:-2]
    openai.api_key = 'sk-proj-VQD7HlpwM4gsQqVgseGhT3BlbkFJi3ReSkWvTjhMGYB6ypSj'
    quest = 'сделай рассклад, вопрос на который хочу узнать ответ:' +question +'карты которые мне выпали:'+chosen_cards
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # или используйте "gpt-3.5-turbo" в зависимости от доступной модели
            messages=[
                {"role": "system", "content": "Ты телеграмм бот таролог, делающий рассклады на натальных картах"},
                {"role": "user", "content": quest},
            ]
        )

        print(response.choices[0].message['content'])
    except Exception as e:
        print(e)

    return Response({'answer':chosen_cards}, status=status.HTTP_200_OK)
