// app.js
document.getElementById('riskForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Collect the form data
    const formData = new FormData(document.getElementById('riskForm'));
    const data = {};
    formData.forEach((value, key) => {
        if (key === "symptoms") {
            if (!data[key]) {
                data[key] = [];
            }
            data[key].push(value);
        } else {
            data[key] = value;
        }
    });

    // Send the data to the backend
    const response = await fetch('http://127.0.0.1:5000/predict3', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    // Get the result and display it
    const result = await response.json();
    document.getElementById('result').innerText = `Risk Level: ${result.prediction}`;
});
