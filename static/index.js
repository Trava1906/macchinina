let port;
let writer;
const encoder = new TextEncoder();
const activeButtons = {};

const keyMap = {
  ArrowUp: { command: 'A', buttonId: 'btn-up' },
  ArrowDown: { command: 'I', buttonId: 'btn-down' },
  ArrowLeft: { command: 'S', buttonId: 'btn-left' },
  ArrowRight: { command: 'D', buttonId: 'btn-right' },
  ' ': { command: 'S', buttonId: 'btn-stop' },
  w: { command: 'F', buttonId: 'btn-up' },
  s: { command: 'B', buttonId: 'btn-down' },
  a: { command: 'L', buttonId: 'btn-left' },
  d: { command: 'R', buttonId: 'btn-right' },
};

function sendCommand(char) {
  console.log("Sto per inviare:", char);
  fetch('/invia_comando', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ comando: char })
  })
  .then(response => {
    if (!response.ok) throw new Error('Errore dal server Flask');
    return response.json();
  })
  .then(data => {
    console.log('Risposta Flask:', data);
  })
  .catch(error => {
    console.error('Errore invio al server:', error);
  });
}


function updateSpeed(val) {
  document.getElementById("speedValue").innerText = val;
  sendCommand(val + '\n');
}

document.addEventListener('keydown', (e) => {
  const key = e.key.toLowerCase();
  const mapEntry = keyMap[key];

  if (mapEntry && !activeButtons[key]) {
    sendCommand(mapEntry.command);
    const btn = document.getElementById(mapEntry.buttonId);
    if (btn) {
      btn.classList.add('active');
      activeButtons[key] = btn;
    }
  }
});

document.addEventListener('keyup', (e) => {
  const key = e.key.toLowerCase();
  const btn = activeButtons[key];
  if (btn) {
    btn.classList.remove('active');
    delete activeButtons[key];
  }
});
