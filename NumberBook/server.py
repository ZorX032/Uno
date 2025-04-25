from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_web_app():
    return send_from_directory('.', 'index.html')  # Передаёт ваш HTML-файл

if __name__ == '__main__':
    app.run()  # Запуск сервера f