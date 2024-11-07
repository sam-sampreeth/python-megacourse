import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
cards_df = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
cardsecurity_df = pd.read_csv('card_security.csv', dtype=str)


class Hotel:
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

class Reservation:
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

class Creditcard:
    def __init__(self, num):
        self.num = num

    def validate(self, expi, namee, cvc):
        card_data = {"number": self.num, "expiration": expi, "holder": namee, "cvc": cvc}
        if card_data in cards_df:
            return True
        else:
            return False

class SecureCC(Creditcard):
    def authenticate(self, given_pass):
        password = cardsecurity_df.loc[cardsecurity_df["number"] == self.num, "password"].squeeze()
        if password == given_pass:
            return True
        else:
            return False

print(df)
hotel_ID = input('Enter hotel id: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    card_number = input('Enter card number: ')

    credit_card = SecureCC(num="1234567890123456")
    if credit_card.validate(expi="01/24", namee="sam", cvc="000"):
        if credit_card.authenticate(given_pass="mypas"):
            hotel.book()
            name = input('Enter your name: ')
            reservation = Reservation(cust_name=name, hotel_ob=hotel)
            print(reservation.generate())
        else:
            print("Incorrect password")

    else:
        print("Payment failed")

else:
    print('No hotels available')