from typing import Any, Text, Dict, List, Union
import requests
import smtplib
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ServiceRequest(FormAction):
    def name(self) -> Text:
        return "service"

    @staticmethod
    def required_slots(tracker):
        return ["cid","time"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "cid": [
                self.from_entity(entity="cid", intent="inform")
            ],
            "time": [
                self.from_entity(entity="time")
            ]
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        customerid = int(tracker.get_slot('cid'))
        cidd = str(tracker.get_slot('cid'))
        times = str(tracker.get_slot('time'))
        api_address = "http://127.0.0.1:8000/customers"
        url = api_address + "/" + cidd + "/"
        r = requests.get(url)
        js = r.json()
        name = js['name']
        model = js['model']
        fueltype = js['fueltype']
        emailslot = js['emailid']
        FROM = <Email Id>
        user = <Email Id>
        pwd = <Password>
        TO = emailslot
        SUBJECT = "Your service is confirmed!"
        TEXT = "Name:" + name + "\n" + "Model:" + model + "\n" + "Time:" + times
        message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        res = requests.put(url, json={'name': name,'model': model, 'fueltype': fueltype, 'timeslot': times})
        response = "Your service will be booked. Confirmation Mail is sent to your email id."
        dispatcher.utter_message(response)
        return []

class SubmitService(FormAction):
    def name(self) -> Text:
        return "submission"

    @staticmethod
    def required_slots(tracker):
        return ["cname", "carname", "phone", "fueltype", "time", "email", "number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "cname": [
                self.from_entity(entity="cname", not_intent=["out_of_scope", "deny", "confirm"])
            ],
            "carname": [
                self.from_entity(entity="carname", intent="vehiclename")
            ],
            "phone": [
                self.from_entity(entity="phone", intent="cphone")
            ],
            "fueltype": [
                self.from_entity(entity="fueltype", intent="fuel")
            ],
            "time": [
                self.from_entity(entity="time")
            ],
            "email": [
                self.from_entity(entity="email")
            ]

        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        customername = str(tracker.get_slot('cname'))
        print(customername)
        carname1 = str(tracker.get_slot('carname'))
        fueltype1 = str(tracker.get_slot('fueltype'))
        emailslot = str(tracker.get_slot('email'))
        timez = str(tracker.get_slot('time'))
        cnumber = int(tracker.get_slot('phone'))
        FROM = 
        user = 
        pwd = 
        TO = emailslot
        SUBJECT = "Your service is confirmed"
        TEXT = "Name:" + customername + "\n" + "Model:" + carname1 + "\n" + "Time:" + timez
        message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        response = requests.post("http://127.0.0.1:8000/customers/",json={'name': customername,'customernumber': cnumber, 'emailid' : emailslot,'model': carname1, 'fueltype': fueltype1,'timeslot': timez})
        dispatcher.utter_message("Your service will be booked!")
        return []


class TestDriveCarInfo(Action):
    def name(self) -> Text:
        return "testdrive"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_address = "http://127.0.0.1:8000/carinfos"
        carname = str(tracker.get_slot('testcar'))
        url = api_address + "/" + carname
        r = requests.get(url)
        js = r.json()
        response = "Price:" + js['price'] + "\n" + "Type:" + js['type'] + "\n" + "Mileage:" + js['mileage'] + "\n" + "Fuel type:" + js['fueltype'] + "\n" + "Transmission:" + js['transmission']
        dispatcher.utter_message(response)
        return []


class TestDriveService(FormAction):
    def name(self) -> Text:
        return "testbook"

    @staticmethod
    def required_slots(tracker):
        return ["cname", "testdrivecar", "phone", "time", "email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "cname": [
                self.from_entity(entity="cname", not_intent=["out_of_scope", "deny", "confirm"])
            ],
            "testdrivecar": [
                self.from_entity(entity="testdrivecar", intent="choosecar")
            ],
            "phone": [
                self.from_entity(entity="phone", intent="cphone")
            ],
            "time": [
                self.from_entity(entity="time")
            ],
            "email": [
                self.from_entity(entity="email")
            ]

        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        customername = str(tracker.get_slot('cname'))
        modelselect = str(tracker.get_slot('testdrivecar'))
        contactnumber = int(tracker.get_slot('phone'))
        timeselect = str(tracker.get_slot('time'))
        emailid = str(tracker.get_slot('email'))
        FROM = 
        user = 
        pwd = 
        TO = emailid
        SUBJECT = "Test Drive Registered :)"
        TEXT = "Name:" + customername + "\n" + "Model for Test Drive Selected:" + modelselect + "\n" + "Date and Time:" + timeselect
        message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        response = requests.post("http://127.0.0.1:8000/customerinfo/",
                                 json={'name': customername, 'model_selected': modelselect,
                                       'contactnumber': contactnumber,
                                       'emailid': emailid, 'booktime': timeselect})
        dispatcher.utter_message("Your Test Drive will be booked!")
        return []
