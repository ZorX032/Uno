import os

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_web_app():
    return send_from_directory('.', 'index.html')  # Передаёт ваш HTML-файл

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))  # Получаем порт из переменной окружения
    app.run(host="0.0.0.0", port=port)  # Запускаем сервер с правильными параметрами
