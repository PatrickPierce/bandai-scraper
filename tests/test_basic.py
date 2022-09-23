import pytest
import requests
from src.bandai_scraper.scraper import Scraper


def test_valid_api():
    res = requests.get(
        "https://api.bandai-tcg-plus.com/api/user/card/list?game_title_id=4&limit=10&offset=0"
    )
    assert res.status_code == 200


base = "https://s3.amazonaws.com/prod.bandaitcgplus.files.api/card_image/OP-EN/"


@pytest.mark.parametrize(
    "id,name,image_url",
    [
        ("36534", "Monkey.D.Luffy", f"{base}ST01/ST01-001_D.png"),
        ("36536", "Karoo", f"{base}ST01/ST01-003_D.png"),
        ("36535", "Usopp", f"{base}ST01/ST01-002_D.png"),
    ],
)
def test_scrape_card(id, name, image_url):
    card = Scraper(id)
    assert card.name() == name
    assert card.image() == image_url
    assert len(card.card) == 15


# Test for color and other card details
