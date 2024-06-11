from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("basic.html")


@app.route("/clothes/")
def get_clothes():
    catalog_clothes = [
                        {"title": "Штаны", "description": "description"},
                        {"title": "Майки", "description": "description"},
                        {"title": "Рубашки", "description": "description"}
                      ]
    return render_template("clothes.html", context=catalog_clothes)


@app.route("/shoes/")
def get_shoes():
    catalog_shoes = [
                        {"title": "Весенне-Осенняя обувь", "description": "description"},
                        {"title": "Летняя обувь", "description": "description"},
                        {"title": "Зимняя обувь", "description": "description"}
                    ]
    return render_template("shoes.html", context=catalog_shoes)


@app.route("/jackets/")
def get_jackets():
    catalog_jackets = [
                        {"title": "Весенне-Осенние куртки", "description": "description"},
                        {"title": "Летние куртки ", "description": "description"},
                        {"title": "Зимние куртки", "description": "description"}
                    ]
    return render_template("jackets.html", context=catalog_jackets)



if __name__ == "__main__":
    app.run(debug=True)




