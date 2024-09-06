from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

stations = pd.read_csv('data_small/stations.txt', skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):

    fname = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(fname, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def allData(station):
    fname = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(fname, skiprows=20, parse_dates=["    DATE"])
    res = df.to_dict(orient="records")
    return res

@app.route("/api/v1/annual/<station>/<year>")
def yearData(station, year):
    fname = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(fname, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    res = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return res
if __name__ == "__main__":
    app.run(debug=True)
