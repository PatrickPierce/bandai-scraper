from pathlib import Path
import requests

class Scraper:
    def __init__(self, id):
        self.baseurl = 'https://api.bandai-tcg-plus.com/api/user/card/'
        self.id = str(id)
        self.card = self.scrape_card(self.id)
        self.serialize_card(self.card)
    
    def scrape_card(self, id):
        """
        GET request to API using card ID
        :param id (int): Bandai's API ID representing card
        :return (dict): Card details return in json format
        """
        res = requests.get(self.baseurl + self.id)
        data = res.json()
        card = data['success']['card']
        return card

    # Need to seralize for text keywords (blocker, trigger, counter)
    def serialize_card(self, card):
        """
        Serailize data from Bandai's API
        :param card (dict): Card details in json format

        """
        # Move card configurations to root dictionary
        for config in self.card['card_config']:
            if len(config) < 2:
                config['value'] = None
        
            key = 'card_' + config['config_name'].lower()
            value = config['value']
            self.card[key] = value

        # Create card text configuration if missing
        if self.card.get('card_text') is None:
            self.card['card_text'] = None
    
        # List of colors for dual color cards.
        # May break in the future once dual color's are released to API
        self.card['card_color'] = self.card['card_color'].split('/')
        self.card['card_regulations'] = "Official Rule"
        self.card['bandai_id'] = self.id
        self.card['card_crew'] = self.card['card_type']

        del self.card['card_config']
        del self.card['card_notes']
        del self.card['regulations']
        del self.card['card_type']

    
    def download_image(self):
        """
        Download card image from Bandai's Amazon S3 bucket
        :param card (dict): Card

        """
        Path('images').mkdir(parents=True, exist_ok=True)
        response = requests.get(self.card['image_url'], stream=True)
        imagePath = f"images/{self.card['card_number']}.png"
        with open(imagePath, 'wb') as f:
            f.write(response.content)

        self.card['image_path'] = imagePath
        del self.card['image_url']
    
    def name(self):
        return self.card['card_name']

    def number(self):
        return self.card['card_number']
    
    def text(self):
        return self.card['card_text']
    
    def image(self):
        if self.card.get('image_url'):
            return self.card['image_url']
        return self.card['image_path']

    def set(self):
        return self.card['card_set']

    def color(self):
        return self.card['card_color']

    def type(self):
        return self.card['card_card type']

    def rarity(self):
        return self.card['card_rarity']

    def cost_life(self):
        return self.card['card_cost/life']

    def power(self):
        return self.card['card_power']

    def crew(self):
        return self.card['card_crew']

    def counter(self):
        return self.card['card_counter+']

    def attribute(self):
        return self.card['card_attribute']

    def regulations(self):
        return self.card['card_regulations']

    def bandai_id(self):
        return self.card['bandai_id']

if __name__ == "__main__":
    luffy = Scraper(36534)
    usopp = Scraper(36535)
    karoo = Scraper(36536)

    # luffy.download_image()
    print(luffy.name())
    print(luffy.number())
    print(luffy.text())
    print(luffy.image())
    print(luffy.set())
    print(luffy.color())
    print(luffy.type())
    print(luffy.rarity())
    print(luffy.cost_life())
    print(luffy.power())
    print(luffy.crew())
    print(luffy.counter())
    print(luffy.attribute())
    print(luffy.regulations())
    print(luffy.bandai_id())

    print(len(luffy.card))
    print(luffy.card)
    print('\n')
    print(len(usopp.card))
    print(usopp.card)
    print('\n')
    print(karoo.card)
    print(len(karoo.card))