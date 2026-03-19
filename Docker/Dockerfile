# Step 1: Base image ko update kar (3.9 se 3.11 ya 3.12 kar de)
FROM python:3.11-slim

# Step 2: OS level dependencies (Compilers aur Tools)
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    gcc \
    g++ \
    libfreetype6-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Working Directory
WORKDIR /app

# Step 4: Python ki core libraries aur gprMax ki zarurat
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy cython matplotlib scipy h5py

# Step 5: gprMax Install (Ensure correctly cloning and installing)
RUN git clone https://github.com/gprMax/gprMax.git /gprMax
WORKDIR /gprMax
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py build
RUN python setup.py install
# Step 6: Tera project code container mein copy
COPY . .

# Step 7: Simulation run karne ka default command
CMD ["python", "scripts/integration_test.py"]