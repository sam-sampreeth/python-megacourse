import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})


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


print(df)
hotel_ID = input('Enter hotel id: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation = Reservation(cust_name=name, hotel_ob=hotel)
    print(reservation.generate())

else:
    print('No hotels available')