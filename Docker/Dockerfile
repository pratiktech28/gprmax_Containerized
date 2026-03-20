# Step 1: Base image (Python slim version for efficiency)
FROM python:3.11-slim

# Step 2: OS level dependencies (Compilers, OpenMP support aur Tools)
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    gcc \
    g++ \
    libgomp1 \
    libfreetype6-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Working Directory set kar
WORKDIR /app

# Step 4: Environment Variables (OpenMP aur Parallel processing ke liye)
ENV OMP_NUM_THREADS=4
ENV PYTHONPATH="/gprMax:${PYTHONPATH}"

# Step 5: Python ki core libraries aur gprMax ki zarurat
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy cython matplotlib scipy h5py pytest

# Step 6: gprMax Setup (Clone and Build with OpenMP)
RUN git clone https://github.com/gprMax/gprMax.git /gprMax
WORKDIR /gprMax

# Install requirements agar kuch miss ho gaya ho
RUN pip install --no-cache-dir -r requirements.txt || true

# Final Building steps (Cython code ko compile karke machine level speed dena)
RUN python setup.py build
RUN python setup.py install

# Step 7: Tera project code container mein copy kar
COPY . /app
WORKDIR /app

# Step 8: Simulation run karne ka default command
CMD ["python", "scripts/integration_test.py"]