# bandai-scraper
Web Scraper for Bandai TCG. Currently works for only "One Piece Card Game".
Enter ID of card found at [Bandai TCG](https://api.bandai-tcg-plus.com/api/user/card/list?game_title_id=4&limit=20&offset=0).

Card will return json object and download image.


# Example
```py
from scraper import scrape_card
card = scrape_card(36534)
print(card)
```

```
{
  'card_name': 'Monkey.D.Luffy',
  'card_number': 'ST01-001',
  'card_text': '[Activate: Main] [Once Per Turn] Give this Leader or 1 of your Characters up to 1 rested DON!! card.',
  'image_url': 'https://s3.amazonaws.com/prod.bandaitcgplus.files.api/card_image/OP-EN/ST01/ST01-001_D.png',
  'card_set': 'STARTER DECK -Straw Hat Crew- [ST-01]',
  'bandai_id': 36534,
  'card_regulations': 'Official Rule',
  'card_color': ['Red'],
  'card_card type': 'Leader',
  'card_rarity': 'L',
  'card_cost/life': '5',
  'card_power': '5000',
  'card_type': 'Supernovas/Straw Hat Crew',
  'card_counter+': None,
  'card_attribute': 'Strike'
}
```
