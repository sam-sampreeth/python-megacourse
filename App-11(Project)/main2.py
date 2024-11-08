import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv('hotels.csv', dtype={'id': str})

class Hotel:
    watermark = "THE REAL ESTATE CO."
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    @classmethod
    def get_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass

class Spa(Hotel):
    def book_spa(self):
        pass

class Reservation(Ticket):
    def __init__(self, cust_name, hotel_ob):
        self.cust_name = cust_name
        self.hotel = hotel_ob

    def generate(self):
        content = f"""
        Thank you for booking our hotel!
        Here are your reservation details:
        Name: {self.cust_name}
        Hotel: {self.hotel.name}
        """
        return content

    @property
    def cleaned_name(self):
        name = self.cust_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2

class DugTicket(Ticket):
    def generate(self):
        return "This is your ticket"

    def download(self):
        pass

class SpaTicket:
    def __init__(self, cust_name, hotel_ob):
        self.cust_name = cust_name
        self.hotel = hotel_ob

    def generate(self):
        content = f"""
        Thank you for your Spa reservation!
        Here are your reservation details:
        Name: {self.cust_name}
        Hotel: {self.hotel.name}
        """
        return content

