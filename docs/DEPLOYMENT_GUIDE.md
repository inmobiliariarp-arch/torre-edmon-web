# 🚀 Guía de Despliegue y Publicación en GitHub y Vercel

## 🌐 1. Publicación Automatizada en GitHub Pages

El repositorio cuenta con un flujo de integración continua en `.github/workflows/deploy.yml`.

### Pasos para Activar:
1. Sube el código al repositorio de GitHub:
   ```bash
   git remote add origin https://github.com/<TU_USUARIO>/<TU_REPOSITORIO>.git
   git branch -M main
   git push -u origin main
   ```
2. En GitHub, ve a **Settings** > **Pages**.
3. En el apartado **Build and deployment > Source**, elige **GitHub Actions**.
4. Cada vez que hagas un `git push` a `main`, GitHub Pages desplegará automáticamente la versión más reciente en:
   `https://<TU_USUARIO>.github.io/<TU_REPOSITORIO>/`

---

## ⚡ 2. Despliegue en Vercel (Recomendado para Repositorios Privados)

Si tu repositorio en GitHub es privado y tu cuenta de GitHub es del plan gratuito, **Vercel** permite desplegar repositorios privados de manera 100% gratuita, con CDN global ultrarrápido y certificados SSL automáticos.

### Pasos:
1. Crea una cuenta o inicia sesión en [Vercel](https://vercel.com).
2. Haz clic en **Add New...** > **Project**.
3. Conecta tu cuenta de GitHub y selecciona el repositorio privado de Torre Edmond.
4. En **Framework Preset**, déjalo en **Other** (sitio estático).
5. Haz clic en **Deploy**.
6. En pocos segundos tendrás una URL lista para compartir, por ejemplo:
   `https://torre-edmond.vercel.app`

---

## 💻 3. Ejecución Local

Para probar el sitio localmente en tu computadora:

### Con Python:
```bash
python -m http.server 8000
```
Luego abre tu navegador en `http://localhost:8000`.

### Con Node.js / npx:
```bash
npx serve .
```
