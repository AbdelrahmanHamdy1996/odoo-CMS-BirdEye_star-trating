var request = new XMLHttpRequest();

request.open('GET', 'https://api.birdeye.com/resources/v1/review/businessid/158170949468469/summary?api_key=bJQGlIUGx2ZZ9YlnuVPPYMVR3yhrmWAU');

request.onreadystatechange = function() {
    if (this.readyState === 4) {
        console.log('Status:', this.status);
        console.log('Headers:', this.getAllResponseHeaders());
        console.log('Body:', this.responseText);
    }
};

request.send();