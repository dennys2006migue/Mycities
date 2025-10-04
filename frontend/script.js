let map = L.map('map').setView([0, 0], 2);  // Centro inicial
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

const API_BASE = 'http://127.0.0.1:8000';  // Backend local

function fetchData(endpoint) {
    fetch(`${API_BASE}${endpoint}`)
        .then(response => response.json())
        .then(data => document.getElementById('content').innerHTML = JSON.stringify(data))
        .catch(error => console.error('Error:', error));
}