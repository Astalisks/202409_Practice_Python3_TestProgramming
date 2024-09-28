FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY ./tests /tests

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
# 4つのワーカー（プロセス）を使用してリクエストを並列に処理
# main.pyのappオブジェクトをFastAPIアプリケーションとして指定、Gunicornでそのアプリケーションを動かす
# サーバーは全てのネットワークインターフェース（0.0.0.0）でポート8000をリッスン、リクエスト受け付け