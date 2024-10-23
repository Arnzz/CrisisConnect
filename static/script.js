function simulateDisaster() {
    fetch('/simulate_disaster')
        .then(response => response.json())
        .then(data => {
            alert(`Disaster Alert: ${data.disaster}!`);
            setTimeout(simulateDisaster, 10000);  // Call the function again after 10 seconds
        });
}

window.onload = function() {
    simulateDisaster();
};
