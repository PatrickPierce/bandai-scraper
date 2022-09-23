import json
import requests
from scraper import scrape_card, download_image


def get_total() -> int:
    """
    Return total number of cards found in Bandai's master API
    :return int: Interger for total cards
    """
    link = 'https://api.bandai-tcg-plus.com/api/user/card/list?game_title_id=4&limit=10&offset=0'
    res = requests.get(link)
    jsonRes = res.json()
    return int(jsonRes['success']['total'])


cardList = []
offset = 0
limit = 20
total = get_total()

while offset < total:
    link = f'https://api.bandai-tcg-plus.com/api/user/card/list?game_title_id=4&limit={limit}&offset={offset}'
    res = requests.get(link)
    data = res.json()
    cards = data['success']['cards']
    for card in cards:
        cardDetail = scrape_card(card['id'])
        download_image(cardDetail)
        cardList.append(cardDetail)    
    offset += limit

if __name__ == "__main__":
    print(cardList)
    print('\n###########\n')

    print(f"Total Cards from API: {total}")
    print(f"Scraped Cards: {len(cardList)}")
    print(f"First card: {cardList[0]}")
    print(f"Last card: {cardList[total-1]}")

    with open("card_list.json", "w", encoding='utf-8') as f:
        json.dump(cardList, f, ensure_ascii=False, indent=4)