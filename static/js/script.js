document.addEventListener('DOMContentLoaded', function() {
    const hamburgerButton = document.getElementById('hamburgerButton');
    const menu = document.getElementById('menu');

    hamburgerButton.addEventListener('click', function() {
        menu.classList.toggle('active');
    });
});
