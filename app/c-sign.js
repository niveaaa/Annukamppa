document.getElementById('counsellor-signin-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Replace these with the correct email and password for counsellors
    const counsellorEmail = 'counsellor@example.com';
    const counsellorPassword = 'counsellor123';

    if (email === counsellorEmail && password === counsellorPassword) {
        window.location.href = 'counsellor-display.html';
    } else {
        alert('Invalid email or password');
    }
});
