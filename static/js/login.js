
document.addEventListener('DOMContentLoaded', function () {
const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const loginData = {
        username: username,
        password: password
    };

    fetch('/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', 
        },
        body: JSON.stringify(loginData)
    })
    .then(response => {
        const contentType = response.headers.get('Content-Type');
        if (contentType && contentType.includes('text/html')) {
            return response.text();
        } else {
            return response.json();
        }
    })
    .then(data => {
        if (typeof data === 'string') {
            document.open();
            document.write(data)
            document.close();
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
})

