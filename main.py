from flask import Flask, render_template, request
import serial

#bluetooth = serial.Serial('COM5', 9600)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


@app.route('/invia_comando', methods=['POST'])
def invia_comando():
    comando = request.json.get("comando")
    if comando:
        #bluetooth.write(comando.encode())  # Manda il comando ad Arduino
        return {"status": "ok"}
    return {"status": "errore"}, 400