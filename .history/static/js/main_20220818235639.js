const burger = document.getElementById('burger');
const navLinks = document.querySelector('.custom-header');

burger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});
