FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    gcc \
    g++ \
    libgomp1 \
    libfreetype6-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV OMP_NUM_THREADS=4
ENV PYTHONPATH="/gprMax:${PYTHONPATH}"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy cython matplotlib scipy h5py pytest

RUN git clone https://github.com/gprMax/gprMax.git /gprMax
WORKDIR /gprMax

RUN pip install --no-cache-dir -r requirements.txt || true

RUN python setup.py build
RUN python setup.py install

COPY . /app
WORKDIR /app

CMD ["python", "scripts/integration_test.py"]
