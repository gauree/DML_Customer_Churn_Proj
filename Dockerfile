FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Set work directory inside container
WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement file(s) first for better Docker layer caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

# Expose the Flask port
EXPOSE 5000

# Default command:
# - run the training script if model.pkl is missing
# - then start the Flask API
CMD ["bash", "-lc", "if [ ! -f src/model/model.pkl ]; then python src/model/train.py; fi && python src/app.py"]
