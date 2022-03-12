from flask import Flask,render_template,url_for,request
import qrcode
import support

app = Flask(__name__)


def creating_qrcode(input_):
    if str(input_) == "":
        return False
    else:
        img = qrcode.make(input_)
        global filename
        filename = support.deEmojify(str(input_))
        filename = support.duplicate_name_check(str(filename))
        img.save(f"static/images/{filename}.png")


@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        support.deletion()
        original_entry = request.form["entry"]
        if creating_qrcode(original_entry) == False:
            qr_code_img = url_for('static', filename='images/dna.png')
            return render_template('index.html',output_img=qr_code_img)
        else:
            qr_code_img = url_for('static', filename=f'images/{filename}.png')
            return render_template('index.html',output_img=qr_code_img)

    else:
        support.deletion()
        dna_img = url_for('static', filename='images/dna.png')
        return render_template('index.html',output_img=dna_img)


if __name__ == "__main__":
    app.run(debug=False)


# debug is set to false which was true and also not hosting port was specified....all these are done just for hosting purposes so change it with change in needs.
