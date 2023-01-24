### CoinDahsApp
#### Install with Docker
    git clone https://github.com/stdinstdout/CoinAppDashboard.git
    cd CoinAppDashboard/
    docker compose up --build -d

#### Install with python venv
    git clone https://github.com/stdinstdout/CoinAppDashboard.git
    cd CoinAppDashboard
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    cd CoinDashApp
    gunicorn app:server -b 0.0.0.0:80


