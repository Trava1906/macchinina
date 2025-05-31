from flask import Flask, render_template, request, abort, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Variabili globali per il lock
dispositivo_autorizzato = None
ultima_attivita = None
TIMEOUT_MINUTI = 5  # Timeout di inattività per liberare il lock

def controlla_lock():
    global dispositivo_autorizzato, ultima_attivita

    ip_cliente = request.remote_addr
    ora_corrente = datetime.now()

    # Libera il lock se il timeout è scaduto
    if ultima_attivita and (ora_corrente - ultima_attivita > timedelta(minutes=TIMEOUT_MINUTI)):
        print("Timeout scaduto. Lock rilasciato.")
        dispositivo_autorizzato = None
        ultima_attivita = None

    if dispositivo_autorizzato is None:
        # Primo client: lo autorizzo
        dispositivo_autorizzato = ip_cliente
        ultima_attivita = ora_corrente
        print(f"Accesso concesso a: {ip_cliente}")
    elif ip_cliente != dispositivo_autorizzato:
        print(f"Accesso negato a: {ip_cliente}. Già registrato: {dispositivo_autorizzato}")
        abort(403)  # Accesso negato
    else:
        # IP già autorizzato, aggiorno attività
        ultima_attivita = ora_corrente

@app.before_request
def before_request():
    controlla_lock()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/invia_comando', methods=['POST'])
def invia_comando():
    comando = request.json.get("comando")
    if comando:
        # bluetooth.write(comando.encode())  # Manda il comando ad Arduino
        return jsonify({"status": "ok"})
    return jsonify({"status": "errore"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
