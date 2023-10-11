
        
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('signup-form');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); 

        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('conf-password').value;

        const userData = {
            username: username,
            email: email,
            password: password,
            confirmPassword: confirmPassword
        };

        fetch('/auth/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(response => {

            if (response.redirected){
                window.location.href = '/auth/login/'
                history.replaceState(null, '', '/auth/login/');
            }
            else {
                return response.json()
            }
            
        })
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
