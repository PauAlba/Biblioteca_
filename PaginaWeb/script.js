const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(drop => {
  const toggle = drop.querySelector('.dropdown-toggle');
  const content = drop.querySelector('.dropdown-content');

  toggle.addEventListener('click', () => {
    content.style.display = content.style.display === 'flex' ? 'none' : 'flex';
  });
});
