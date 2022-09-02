from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Add this to the end of the address bar: /play OR: /play/(any integer) OR: /play/(any integer)/(any color)"

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<user_num>')
def play_with_num(user_num):
    return render_template("index1.html", num = int(user_num))

@app.route('/play/<user_num>/<user_color>')
def play_with_num_and_color(user_num, user_color):
    return render_template("index2.html", num = int(user_num), box_color = user_color)

if __name__=="__main__":
    app.run(debug=True)
