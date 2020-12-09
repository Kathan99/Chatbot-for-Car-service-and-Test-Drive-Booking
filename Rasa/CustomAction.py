from typing import Any, Text, Dict, List, Union
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class PostService(Action):
    def name(self) -> Text:
        return "service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """api_address = "http://127.0.0.1:8000/customers" """

        print("inside action")
        print(name)
        print("\n")
        print(car)
        print(ctype)

        return []