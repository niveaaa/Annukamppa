document.getElementById('student-signin-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Replace these with the correct email and password for students
    const studentEmail = 'student@example.com';
    const studentPassword = 'student123';

    if (email === studentEmail && password === studentPassword) {
        window.location.href = 'student-display.html';
    } else {
        alert('Invalid email or password');
    }
});
