from flask import Flask, request, render_template
app = Flask(__name__)

#1 Open both methods, GET, POST. (using "methods=" )
@app.route('/add_food', methods=["GET", "POST"])
def add_food():
  if request.method == "GET":
      return render_template("food_form.html")
  elif request.method == "POST":
        form = request.form   # form la kieu dictionary   # form hay user trong register la ten dict, request.form thi form la form o trong file html
        # print(form)
        t = form["title"]
        l = form["link"]
        # print(t, l)
        return "POST"

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        user = request.form
        u = user["username"]
        p = user["password"]
        print(u, p)
        return "Registered"

if __name__ == '__main__':
  app.run(debug=True)