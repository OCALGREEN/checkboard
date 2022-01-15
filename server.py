from flask import Flask, render_template # importing Flask

app = Flask(__name__) # creating a Flask object

@app.route('/') # creating default route will output the function immediately after this
def render_8X8(): # will render an 8X8 checker board
    return render_template("index.html") 

@app.route('/4')
def render_8X4(): # will render an 8X4 checker board
    return render_template("index4.html") 

@app.route('/<int:x>/<int:y>')
def render_XY(x, y): # will render a checker board according to the inputs
    return render_template("indexYX.html", x = x, y = y)

if __name__ == "__main__": # end and debug
    app.run(debug=True)

