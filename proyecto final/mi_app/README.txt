# 📌 Proyecto Django – Gestión de Personas

Este proyecto es una aplicación web desarrollada con Django que permite registrar y listar personas junto con su país de origen y trabajo.

## 🚀 Funcionalidades

- Agregar nuevas personas mediante un formulario.
- Crear automáticamente países y trabajos si no existen.
- Listar todas las personas registradas.
- Visualizar datos desde el panel de administración de Django.

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

2. Crear entorno virtual e instalar dependencias:

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
```

3. Aplicar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Ejecutar el servidor:

```bash
python manage.py runserver
```

5. Abrir en el navegador:

```
http://127.0.0.1:8000/
```

---

## 👤 Panel de Administración

Para acceder al panel admin:

```bash
python manage.py createsuperuser
```

Luego ingresar en:

```
http://127.0.0.1:8000/admin/
```

---

## 🛠️ Tecnologías utilizadas

- Python
- Django
- SQLite
