# Usa Python como base
FROM python:3.11

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu proyecto
COPY . .

# Ejecuta la app con uvicorn (ajusta si tu archivo no se llama main.py)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
