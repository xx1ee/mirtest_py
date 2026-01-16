FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libnss3 libatk1.0-0 libx11-xcb1 libxcomposite1 \
    libxdamage1 libxrandr2 libgbm1 libasound2 \
    libpangocairo-1.0-0 libcups2 libdrm2 libxss1 \
    libgtk-3-0 libxtst6 libxcb-shm0 libxcb-xfixes0 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright browsers
RUN playwright install

COPY . .

CMD ["sh", "-c", "pytest ui/tests --alluredir=reports ; pytest api/tests --alluredir=reports"]

