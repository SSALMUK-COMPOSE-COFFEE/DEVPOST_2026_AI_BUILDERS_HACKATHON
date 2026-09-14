FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends git libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libffi8 fonts-dejavu-core && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml ./
COPY killscore ./killscore
RUN pip install --no-cache-dir .
COPY tests ./tests
EXPOSE 8000
CMD ["uvicorn", "killscore.main:app", "--host", "0.0.0.0", "--port", "8000"]
