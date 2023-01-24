### CoinDahsApp
#### Установка при помощи Docker
    git clone ...
    docker compose up --build -d

#### Установка с python venv
    git clone ...
    cd ...
    python3 -m venv env
    pip install -r requirements.txt
    gunicorn app:server -b 0.0.0.0:80


