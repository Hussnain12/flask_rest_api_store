FROM python:3.11.9
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r  requirements.txt
COPY . .
CMD [ "guicorn","--bind","0.0.0.0:80","app:create_app()" ]