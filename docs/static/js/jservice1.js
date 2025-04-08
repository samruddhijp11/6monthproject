// app.js
document.getElementById('diabetesForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const data = {
        gender: document.getElementById('gender').value,
        age: document.getElementById('age').value,
        fbs: document.getElementById('fbs').value,
        ppbs: document.getElementById('ppbs').value,
        hba1c: document.getElementById('hba1c').value,
        bmi: document.getElementById('bmi').value,
        weight: document.getElementById('weight').value,
        bps: document.getElementById('bps').value,
        bpd: document.getElementById('bpd').value
    };
//http://127.0.0.1:5555/predict1
    const response = await fetch('https://diabetes-project-ewvn.onrender.com/diabetes/predict1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });

    const result1 = await response.json();
    document.getElementById('result1').innerText = result1.prediction;
});
