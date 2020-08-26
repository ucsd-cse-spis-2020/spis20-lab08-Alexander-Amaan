from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
   return "Hello Alex and Amaan!"

def ftoc(ftemp):
    return (ftemp - 32.0) * (5.0 / 9.0)

def ctof(ctemp):
    return (ctemp * (9.0/5.0) + 32.0)

def miles_to_km(miles):
    return miles * 1.60934

@app.route('/mtokm/<miles_str>')
def mtokm(miles_str):
    miles = 0.0
    try:
        miles = float(miles_str)
        km = miles_to_km(miles)
        return "Miles: " + miles_str + " In Kilometers " + str(km)
    except:
        return "Couldn't convert " + miles_str + " To Kilometers"


@app.route('/ftoc/<ftemp_str>')
def convert_ftoc(ftemp_str):
    ftemp = 0.0
    try:
        ftemp = float(ftemp_str)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftemp_str + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftemp_str + " to a number"


@app.route('/ctof/<ctemp_str>')
def convert_ctof(ctemp_str):
    ftemp = 0.0
    try:
        ftemp = float(ctemp_str)
        ftemp = ctof(ftemp)
        return 'In Celsius ' + ctemp_str + ' In Fahrenheight ' + str(ftemp)
    except ValueError:
        return "Sorry, Could Not Convert " + ctemp_str + " to a number"        


if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)