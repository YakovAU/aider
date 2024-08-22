import os
from poe_api_wrapper import PoeApi

class PoeApiWrapper:
    def __init__(self):
        poe_p_b = os.getenv('POE_P_B')
        poe_p_lat = os.getenv('POE_P_LAT')

        if not poe_p_b or not poe_p_lat:
            raise ValueError("POE_P_B and POE_P_LAT environment variables must be set")

        tokens = {
            'p-b': poe_p_b,
            'p-lat': poe_p_lat
        }
        self.poe_client = PoeApi(tokens=tokens)

    def send_message(self, model, message):
        return self.poe_client.send_message(model, message)

poe_api = PoeApiWrapper()
