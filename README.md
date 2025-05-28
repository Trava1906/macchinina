#  Progetto: Macchinina Telecomandata con Arduino + PWA

##  Autori
Agliardi C., Bertoletti M., Travascio L., Pandini F., Donida Labati A., Bergomi F.

---

##  1. Obiettivi del Progetto

L’obiettivo è costruire un veicolo controllabile da remoto tramite una Progressive Web App (PWA), con Arduino per la parte hardware.

- Realizzare un veicolo telecomandato
- Utilizzare Arduino per il controllo dei componenti elettronici
- Sviluppare una PWA per inviare comandi via Wi-Fi
- Rendere il progetto open source, modulare e replicabile

---

##  2. Architettura Generale

- **Hardware:** Macchinina fisica con motori, servocomandi e controlli via Arduino
- **Software:** PWA che invia comandi all'Arduino tramite HTTP o WebSocket

---

##  3. Componenti Hardware

| Componente         | Descrizione                         |
|--------------------|-------------------------------------|
| Arduino Uno / ESP32| Microcontrollore principale         |
| HC-05 / ESP8266    | Modulo di comunicazione             |
| Ponte H L298N      | Driver per controllo motori         |
| Motori DC / Servo  | Movimento e sterzata                |
| Servomotore        | Sterzata anteriore                  |
| Telaio LEGO        | Struttura della macchina            |
| Batteria / Powerbank| Alimentazione                      |
| LED                | Feedback visivo                     |

---

##  4. Componenti Software

### Lato Arduino
- C++ con Arduino IDE
- Server Web/Socket per ricezione comandi
- Comandi supportati: `FORWARD`, `BACKWARD`, `LEFT`, `RIGHT`, `STOP`

### Lato Web (PWA)
- HTML, CSS, JavaScript (Vanilla o framework)
- UI responsive con pulsanti/joystick touch
- Comandi inviati via `fetch()` o WebSocket
- Offline-ready con Service Worker
- Installabile su smartphone

---

##  5. Funzionamento

1. L'Arduino si connette alla rete Wi-Fi
2. La PWA individua l'IP e si connette
3. L’utente interagisce con i controlli touch
4. Arduino riceve ed esegue i comandi motori

---

##  6. Funzionalità

-  Movimento: Avanti, Indietro, Destra, Sinistra, Stop
-  UI mobile-friendly
-  LED per feedback
-  Supporto modalità offline

###  Estensioni Future

- Streaming video (ESP32-CAM)
- Sensori ostacolo (ultrasuoni)
- Controllo vocale

---

##  7. Sicurezza & Limiti

- **Arduino:** Autenticazione con token, evitare IP pubblici non protetti
- **Web:** Utilizzare HTTPS, rate limiting per evitare spam

---


---

##  8. Requisiti Minimi

- Arduino Uno + HC-05 o ESP32
- 2 motori DC + Ponte H
- Batteria ricaricabile
- Telaio base (LEGO o stampa 3D)
- Smartphone moderno con browser

---

##  9. Scenario del Progetto

Una macchinina controllabile via smartphone, capace di:

- Muoversi in avanti e indietro
- Sterzare
- Fermarsi
- Mostrare lo stato della batteria

---

##  10. Use Case: Controllo Movimento

| Elemento       | Contenuto                       |
|----------------|---------------------------------|
| Nome           | Controllo Movimento             |
| Attori         | Utente                          |
| Precondizioni  | App connessa alla macchinina    |
| Postcondizioni | Esecuzione del comando          |

### Flusso principale:
1. L’utente apre la PWA
2. Tocca “Avanti”
3. La macchinina si muove

### Estensioni:
-  Connessione persa: messaggio d’errore
-  Batteria scarica: movimento bloccato

---

##  11. Conclusione

Un progetto didattico che fonde elettronica e sviluppo web. Ideale per studenti o maker, permette di imparare:

- Il funzionamento di un microcontrollore
- La comunicazione client-server
- Lo sviluppo moderno con PWA

---



