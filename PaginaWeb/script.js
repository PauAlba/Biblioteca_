const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(drop => {
  const toggle = drop.querySelector('.dropdown-toggle');
  const content = drop.querySelector('.dropdown-content');

  toggle.addEventListener('click', () => {
    content.style.display = content.style.display === 'flex' ? 'none' : 'flex';
  });
});



document.addEventListener('DOMContentLoaded', () => {
  const listaLibros = document.querySelectorAll('.dropdown-content')[0];

  fetch('http://localhost:8000/books', {
    headers: {
      Authorization: 'Bearer eltoken' //cambiar por el token
    }
  })
    .then(res => res.json())
    .then(data => {
      listaLibros.innerHTML = '';
      data.forEach(libro => {
        const item = document.createElement('p');
        item.textContent = `${libro.title} - ${libro.autor}`;
        listaLibros.appendChild(item);
      });
    })
    .catch(error => console.error('Error cargando libros:', error));
});


function buscarLibro() {
  const id = document.getElementById('buscarLibro').value;

  fetch(`http://localhost:8000/books/${id}`, {
    headers: {
      Authorization: 'Bearer eltoken'
    }
  })
    .then(res => {
      if (!res.ok) throw new Error("Libro no encontrado");
      return res.json();
    })
    .then(data => alert(`Título: ${data.title}\nAutor: ${data.autor}`))
    .catch(err => alert(err.message));
}

function publicarLibro() {
  const titulo = document.getElementById('titulo').value;
  const autor = document.getElementById('autor').value;
  const year = document.getElementById('anio').value;
  const categoria = document.getElementById('categoria').value;
  const paginas = document.getElementById('paginas').value;

  const libro = {
    title: titulo,
    autor: autor,
    year: parseInt(year),
    categoria: categoria,
    paginas: parseInt(paginas)
  };

  fetch('http://localhost:8000/books', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: 'Bearer TU_TOKEN_AQUÍ'
    },
    body: JSON.stringify(nuevoLibro)
  })
    .then(res => res.json())
    .then(data => alert(data.message))
    .catch(err => alert("Error al registrar el libro"));

}