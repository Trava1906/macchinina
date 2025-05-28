let port;
    let writer;
    const encoder = new TextEncoder();

   

    function sendCommand(char) {
      if (!writer) {
        alert("Connetti prima l'Arduino!");
        return;
      }
      writer.write(encoder.encode(char));
      console.log("Comando inviato:", char);
    }

    function updateSpeed(val) {
      document.getElementById("speedValue").innerText = val;
      sendCommand(val + '\n'); // Arduino deve leggere la riga come intero
    }

    // Tasti freccia da tastiera
    document.addEventListener('keydown', (e) => {
      const map = {
        ArrowUp: 'A',
        ArrowDown: 'I',
        ArrowLeft: 'S',
        ArrowRight: 'D',
        ' ': 'P'
      };
      if (map[e.key]) sendCommand(map[e.key]);
    });

    

    function inviaComando(comando) {
      fetch("/invia_comando", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ comando: comando })
      });
    }