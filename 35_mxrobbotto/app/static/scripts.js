document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelector('.messages');
    if (messages) {
        setTimeout(() => {
            messages.style.display = 'none';
        }, 5000);
    }
});