from flask import Flask, render_template, request, abort, jsonify
from datetime import datetime, timedelta
import bluetooth

app = Flask(__name__)

# Configura il MAC e la porta
MAC_ADDRESS = "98:D3:71:F7:05:08"  # <-- Cambialo con quello giusto
PORT = 1

# Socket globale
bt_socket = None

def connetti_bluetooth():
    global bt_socket
    try:
        bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        bt_socket.connect((MAC_ADDRESS, PORT))
        print("[INFO] Connessione Bluetooth riuscita")
    except bluetooth.btcommon.BluetoothError as e:
        print(f"[ERRORE] Connessione Bluetooth fallita: {e}")
        bt_socket = None

# Lock per IP
dispositivo_autorizzato = None
ultima_attivita = None
TIMEOUT_MINUTI = 5

def controlla_lock():
    global dispositivo_autorizzato, ultima_attivita

    ip_cliente = request.remote_addr
    ora_corrente = datetime.now()

    if ultima_attivita and (ora_corrente - ultima_attivita > timedelta(minutes=TIMEOUT_MINUTI)):
        print("Timeout scaduto. Lock rilasciato.")
        dispositivo_autorizzato = None
        ultima_attivita = None

    if dispositivo_autorizzato is None:
        dispositivo_autorizzato = ip_cliente
        ultima_attivita = ora_corrente
        print(f"Accesso concesso a: {ip_cliente}")
    elif ip_cliente != dispositivo_autorizzato:
        print(f"Accesso negato a: {ip_cliente}. Già registrato: {dispositivo_autorizzato}")
        abort(403)
    else:
        ultima_attivita = ora_corrente

@app.before_request
def before_request():
    controlla_lock()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/invia_comando', methods=['POST'])
def invia_comando():
    global bt_socket
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"status": "errore", "dettaglio": f"JSON non valido: {e}"}), 400

    comando = data.get("comando")
    print("[DEBUG] Comando ricevuto:", comando)

    if comando and bt_socket:
        try:
            bt_socket.send(comando.encode())
            return jsonify({"status": "ok"})
        except bluetooth.btcommon.BluetoothError as e:
            print(f"[ERRORE] Errore Bluetooth: {e}")
            return jsonify({"status": "errore", "dettaglio": str(e)}), 500

    return jsonify({"status": "errore", "dettaglio": "Comando mancante o socket non connessa"}), 400


if __name__ == '__main__':
    connetti_bluetooth()
    app.run(host='0.0.0.0', port=8000, debug=True)
