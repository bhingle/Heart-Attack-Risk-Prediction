from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route("/check",methods=["GET","POST"])
def check():
    try:
        age = request.form["a"]
        gender = request.form["g"]
        chestpainType = request.form["cp"]
        restingBP = request.form["trtbps"]
        cholestoral = request.form["chol"]
        fastingSugar = request.form["fs"]
        rest_ecg = request.form["rest_ecg"]
        thalach = request.form["thalach"]
        exang = request.form["exang"]
        ca= request.form["ca"]
    except Exception:
        m = "Please fill all the details"
        return render_template("error.html" , msg = m)
    d = [[age,gender,chestpainType,restingBP,cholestoral,fastingSugar,rest_ecg,thalach,exang,ca]]
    with open("db.model","rb") as f:
        model=pickle.load(f)
    res = model.predict(d)
    res = int(res)
    if res == 0:
        m = " Less Chance of Heart Attack"
    else:
        m = " More Chance of Heart Attack"
    return render_template("result.html" , msg = m)

if __name__=="__main__":
    app.run(debug=True)


