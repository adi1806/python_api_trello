import configparser
import os

class ConfigParser:
    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.file_path = os.path.join(os.path.dirname(__file__),
                                        '../data/testdata.ini')
        self.parser.read(self.file_path)

    def fetch_trello_data(self):
        return {
            'api_key': self.parser.get('Configproperties', 'api_key'),
            'token': self.parser.get('Configproperties', 'token'),
            'base_url': self.parser.get('Configproperties', 'base_url'),
            'card_id': self.parser.get('Configproperties', 'card_id'),
            'invalid_card_id': self.parser.get('Configproperties', 'invalid_card_id'),
            'id_list': self.parser.get('Configproperties', 'id_list'),
            'invalid_id_list': self.parser.get('Configproperties', 'invalid_id_list'),
            'id_board': self.parser.get('Configproperties', 'id_board'),
        }

    def set_trello_data(self, key, value):
        # Check if the section 'trello' exists, if not, add it
        if not self.parser.has_section('Configproperties'):
            self.parser.add_section('Configproperties')

        # Set the key and value
        self.parser.set('Configproperties', key, value)

        # Write the changes back to the config.ini file
        with open(self.file_path, 'w') as configfile:
            self.parser.write(configfile)
        print(f"Updated {key} in 'trello' section with value {value}")