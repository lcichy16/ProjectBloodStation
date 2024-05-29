const hamburgerButton = document.getElementById('hamburgerButton');
const menu = document.querySelector('.menu');

hamburgerButton.addEventListener('click', () => {
    menu.classList.toggle('show');
});