import re
import requests
from bs4 import BeautifulSoup


def parse_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    categories = soup.findAll("div", {"class": "categories"})
    ratings = soup.findAll("div", {"class": "ratings"})
    comments = soup.findAll("span", {"class": "review_comment"})
    return {'categories': categories,
            'ratings': ratings,
            'comments': comments}


def extract_text(data):
    categories = data['categories']
    ratings = data['ratings']
    comments = data['comments']

    tags_categories = []
    if categories:
        for category in categories:
            info = category.findAll("li", {'class': 'active'}, text=True)
            tags_categories.extend([re.sub(r'\d+x ', '', i.text) for i in info])

    tags_ratings = []
    if ratings:
        for rating in ratings:
            info = rating.findAll("li", {'class': 'active'}, text=True)
            tags_ratings.extend([i.text for i in info])

    tags_comments = []
    if comments:
        for comment in comments:
            comment = comment.text
            if not comment:
                continue
            comment = comment if len(comment) < 40 else comment[:40] + '...'
            tags_comments.append(comment)
    return {'category': tags_categories[0] if tags_categories else tags_categories,
            'rating': tags_ratings[0] if tags_ratings else tags_ratings,
            'comments': list(set(tags_comments))[:7]}


def is_spam(data):
    rating = data['rating']
    is_spam = False
    if rating:
        count, status = rating.split(' ')
        if 'отрицател' in status and int(count[:-1]) > 10:
            is_spam = True
    return is_spam


def format(data):
    is_spam_ = is_spam(data)
    rating = data['rating']
    data['rating'] = rating.split(' ')[1] if rating else rating

    return {**data, 'is_spam': is_spam_}


def get_info(phone):
    response = requests.get(f'https://www.neberitrubku.ru/nomer-telefona/{phone}')
    data = parse_page(response.text)
    data = extract_text(data)
    return format(data)


phone = '+78123354000'
print(get_info(phone))
