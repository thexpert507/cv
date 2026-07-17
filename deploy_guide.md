# Guía de Despliegue en GitHub Pages 🚀

Tu CV interactivo y bilingüe ya está listo para ser publicado en internet de forma **gratuita** a través de **GitHub Pages**. Dado que ya tienes una cuenta de GitHub (`thexpert507`), el proceso es sumamente sencillo.

Sigue estos pasos para subirlo a tu cuenta:

---

## Paso 1: Crear el repositorio en GitHub
1. Inicia sesión en [github.com](https://github.com).
2. Haz clic en el botón **New** (Nuevo repositorio) en la esquina superior izquierda o ve a [github.com/new](https://github.com/new).
3. Configura lo siguiente:
   - **Repository name:** `cv` (o el nombre que prefieras, por ejemplo, `mi-cv`).
   - **Public/Private:** Debe ser **Public** (Público) para que GitHub Pages sea gratuito.
   - **NO** marques las opciones de agregar un README, .gitignore o licencia (ya que usaremos este proyecto local).
4. Haz clic en **Create repository**.

---

## Paso 2: Vincular y subir tu código local
Abre la terminal de tu computadora en esta misma carpeta y ejecuta los siguientes comandos para subir el CV a GitHub:

1. **Añadir los archivos locales al área de preparación:**
   ```bash
   git add .
   ```

2. **Realizar el primer commit:**
   ```bash
   git commit -m "feat: agregar CV interactivo bilingue"
   ```

3. **Asegurar que la rama principal se llame `main`:**
   ```bash
   git branch -M main
   ```

4. **Vincular con tu nuevo repositorio de GitHub** *(Reemplaza `TU_REPOSITORIO` por el nombre que le pusiste en el Paso 1, por ejemplo: `cv`)*:
   ```bash
   git remote add origin https://github.com/thexpert507/TU_REPOSITORIO.git
   ```

5. **Subir el código a GitHub:**
   ```bash
   git push -u origin main
   ```

---

## Paso 3: Activar GitHub Pages
Una vez subido el código, haz que esté visible para todo el mundo:

1. Entra a tu repositorio en la página de GitHub.
2. Ve a la pestaña **Settings** (Configuración) arriba a la derecha.
3. En el menú lateral izquierdo, haz clic en **Pages**.
4. En la sección **Build and deployment**:
   - **Source:** Déjalo en `Deploy from a branch`.
   - **Branch:** Selecciona la rama `main` y en la carpeta selecciona `/ (root)`.
5. Haz clic en **Save** (Guardar).

---

## ¡Listo! 🎉
En aproximadamente 1 o 2 minutos, GitHub construirá tu sitio. Podrás ver el enlace público en la misma sección de **Pages** (usualmente tendrá el formato `https://thexpert507.github.io/TU_REPOSITORIO/`).

Podrás compartir este enlace con reclutadores para que vean tu CV interactivo, cambien de idioma y lo impriman a PDF directamente desde el navegador.
