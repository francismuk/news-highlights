export NEWS_API_KEY= '29cfe31df9fb475ebd6767b6b8ef74b4'
export SECRET_KEY=<Your secret key>

python3.6 manage.py server
from app import app

if __name__ == '__main__':
    app.run()