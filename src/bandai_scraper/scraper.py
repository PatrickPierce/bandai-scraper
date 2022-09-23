from pathlib import Path
import requests


def scrape_card(id: int) -> dict:
    """
    GET request to API using card ID
    :param id (int): Bandai's API ID representing card
    :return (dict): Card details return in json format
    """
    res = requests.get(f'https://api.bandai-tcg-plus.com/api/user/card/{id}')
    data = res.json()
    card = data['success']['card']
    card['bandai_id'] = id
    serialize_card(card)
    return card


# Seralize for dual colors and text keyboards (blocker, trigger, counter)
def serialize_card(card):
    """
    Serailize data from Bandai's API
    :param card (dict): Card details in json format

    """
    card['regulations'] = "Official Rule"
    card['card_regulations'] = card['regulations']
    
    if card.get('card_text') is None:
        card['card_text'] = None

    for config in card['card_config']:
        if len(config) < 2:
            config['value'] = None
        
        key = 'card_' + config['config_name'].lower()
        value = config['value']
        card[key] = value
    
    card['card_color'] = card['card_color'].split('/')
    del card['card_config']
    del card['card_notes']
    del card['regulations']


def download_image(card):
    """
    Download card image from Bandai's Amazon S3 bucket
    :param card (dict): Card

    """
    Path('images').mkdir(parents=True, exist_ok=True)
    response = requests.get(card['image_url'], stream=True)
    imagePath = f"images/{card['card_number']}.png"
    with open(imagePath, 'wb') as f:
        f.write(response.content)

    card['image_path'] = imagePath
    del card['image_url']


if __name__ == "__main__":
    luffy = scrape_card(36534)
    karoo = scrape_card(36536)
    usopp = scrape_card(36535)

    # download_image(usopp)
    # download_image(karoo)

    print(f'{luffy}\n')
    print(len(luffy))
    print(usopp)
    print('\n')
    print(len(usopp))

    print(karoo)
    print('\n')
    print(len(karoo))