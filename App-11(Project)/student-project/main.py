import fpdf
import pandas as pd

df = pd.read_csv('articles.csv', dtype={'id': str})

class Article:
    def __init__(self, art_id):
        self.id = art_id
        self.name = df.loc[df['id'] == self.id]['name'].squeeze()
        self.price = df.loc[df['id'] == self.id]['price'].squeeze()

    def available(self):
        if self.id in list(df["id"]):
            availability = df.loc[df["id"] == self.id, "in stock"].squeeze()
            if not availability <= 0:
                return True
            else:
                return False

class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        pdf.set_font('Arial', 'B', size=16)
        pdf.cell(w=50, h=8, txt = f"Receipt #{self.article.id}", ln=1)

        pdf.set_font('Arial', 'B', size=16)
        pdf.cell(w=50, h=8, txt = f"Article: {self.article.name}", ln=1)

        pdf.set_font('Arial', 'B', size=16)
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output('receipt.pdf')

print(df)
arti_ID = input('Enter Article ID to buy: ')
article = Article(art_id=arti_ID)
if article.available():
    receipt = Receipt(article)
    receipt.generate()
else:
    print('Article not available')
