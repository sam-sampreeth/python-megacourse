from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api/v1/<word>')
def api(word):
    df = pd.read_csv("dictionary.csv")
    defn = df.loc[df['word'] == word]['definition'].squeeze()
    return {"word": word, "mean": defn}

if __name__ == '__main__':
    app.run(debug=True)