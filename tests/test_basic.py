import pytest
import requests
from src.bandai_scraper.scraper import scrape_card


def test_valid_api():
    res = requests.get('https://api.bandai-tcg-plus.com/api/user/card/list?game_title_id=4&limit=10&offset=0')
    assert res.status_code == 200
    
base = 'https://s3.amazonaws.com/prod.bandaitcgplus.files.api/card_image/OP-EN/'
@pytest.mark.parametrize(
    "id,expected,image_url",
    [
        ("36534", "Monkey.D.Luffy", f'{base}ST01/ST01-001_D.png'),
        ("36536", "Karoo", f'{base}ST01/ST01-003_D.png'),
        ("36535", "Usopp", f'{base}ST01/ST01-002_D.png')
    ]
)
def test_scrape_card(id, expected, image_url):
    card = scrape_card(id)
    print(base)
    print(image_url)
    assert card['card_name'] == expected
    assert card['image_url'] == image_url
    assert len(card) == 15

# Test for color and other card details