# Portfolio Website

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

A personal portfolio built with Django.

## Deployment Options

### Deploying to Render.com

1. Create a Render account at [render.com](https://render.com)

2. Connect your GitHub repository

3. Click "New Web Service" and select your portfolio repository

4. Configure your service:
   - **Name**: portfolio-vedhanth (or your preferred name)
   - **Runtime**: Python
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn portfolio_site.wsgi:application`
   - **Plan**: Free

5. Add the following environment variables:
   - `DEBUG`: False
   - `SECRET_KEY`: (generate a secure key)
   - `ALLOWED_HOSTS`: .onrender.com,localhost,127.0.0.1
   - `RENDER`: true

6. Click "Create Web Service"

Your portfolio will be deployed and accessible at the provided Render URL!

### Deploying to fly.io

See the fly.toml file for configuration details.
