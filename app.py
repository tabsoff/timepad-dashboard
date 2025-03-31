from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

app = Flask(__name__)

# Формируем строку подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Отключаем отслеживание изменений в базе данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализируем SQLAlchemy
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Flask подключился к PostgreSQL!"

if __name__ == "__main__":
    # Создаем таблицы, если они еще не существуют (при наличии моделей)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
