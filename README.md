[![gprMax CI/CD Trident Pipeline](https://github.com/pratiktech28/gprmax_Containerized/actions/workflows/main.yml/badge.svg)](https://github.com/pratiktech28/gprmax_Containerized/actions/workflows/main.yml)


<img width="400" height="200" alt="logo_gprMax" src="https://github.com/user-attachments/assets/b2430b3e-9ccb-4f07-84a2-0a991d01d254" />


<img width="600" height="73" alt="download" src="https://github.com/user-attachments/assets/679dc592-7b1a-4084-9f32-53e42108b810" />


<img width="250" height="164" alt="download" src="https://github.com/user-attachments/assets/5daec642-f732-4c2d-828d-5643cf0d672e" />


# 🏛️ gprMax CI/CD & HPC Automation Infrastructure 🚀

<p align="center">
  <strong>
  Architecting robust, production-ready microservices ecosystems through advanced Docker containerization 
  and enterprise-grade Kubernetes (K8s) orchestration. Expert in designing high-availability Pod 
  architectures, managing multi-node cluster lifecycles, and implementing declarative deployments via 
  Helm charts. Leveraging industry-standard CI/CD pipelines to automate the scaling of gprMax 
  simulation workloads, ensuring seamless resource allocation, efficient node management, and 
  maintaining zero-downtime infrastructure for high-performance computational physics environments 
  at a global scale.
</strong>
  <br>
  <b>Google Summer of Code (GSoC) 2026 Strategy & Implementation</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenMP-FF6B6B?style=for-the-badge&logo=cpu&logoColor=white" alt="OpenMP">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

---

## 📖 Overview
This project aims to revolutionize the development workflow of gprMax by implementing a **Containerized CI/CD Pipeline (The Trident Pipeline).** By leveraging Docker and GitHub Actions, we ensure that every physics simulation is automatically validated across isolated environments, preventing regression errors and streamlining the contribution process for researchers worldwide.


---

## 🏗️ System Architecture & Dependencies

The infrastructure is built on a "Layered Security & Performance" model:

### 1. High-Performance Docker Core
* **Base:** `python:3.11-slim` for a lightweight yet powerful footprint.
* **Compiler Stack:** `build-essential`, `gcc`, and `g++` for compiling gprMax source code.
* **Parallelization:** `libgomp1` (OpenMP) integrated to allow multi-threaded simulation execution.
* **Optimization:** Automatic `Cython` compilation during build time to convert Python bottlenecks into C-level speed.

### 2. Automated CI/CD Pipeline (GitHub Actions)
* **Trigger:** Every `push` or `pull_request` initiates a full system audit.
* **Validation:** The pipeline builds the environment from scratch, ensuring "Zero-Configuration" for new contributors.
* **Database Integration:** Uses an automated Python-SQLite bridge to log NRMSE values and execution metrics.

---

## 🛠️ Tech Stack & Requirements

| Category | Technology Used | Purpose |
| :--- | :--- | :--- |
| **Simulation Engine** | gprMax (Latest) | Electromagnetic wave simulation. |
| **Virtualization** | Docker | Environment consistency and isolation. |
| **Acceleration** | OpenMP / Cython | Parallel processing and code optimization. |
| **Data Logging** | SQLite3 | Persistent storage for simulation metadata. |
| **Automation** | GitHub Actions | Continuous Integration and automated testing. |

---

## 🚀 Getting Started (For Mentors & Contributors)

To replicate this environment or test the simulations locally, follow these commands:

### 1. Clone the Repository
```bash
git clone [https://github.com/pratiktech28/gprmax_Containerized.git](https://github.com/pratiktech28/gprmax_Containerized.git)
cd gprmax_Containerized
**2. Build the HPC Docker Image**
This command compiles the gprMax engine with OpenMP support:

```Bash
docker build -t gprmax-automation -f Dockerfile .
**3. Run the Automated Pipeline**
Execute the simulation and log results directly to the database:

```Bash
# Create results directory for database persistence
mkdir -p results

# Run the container with volume mapping
docker run -v $(pwd)/results:/app/results gprmax-automation
**4. Verify Database Logs**
You can inspect the simulation history using SQLite:

```Bash
sqlite3 results/simulation.db "SELECT * FROM simulation_logs;"
📊 Performance Benchmarks
Multithreading: Enabled via OMP_NUM_THREADS.

Accuracy Tracking: Automated NRMSE calculation integrated into the validation script.

Scalability: Designed to handle 100+ concurrent simulation configurations via relational mapping.
---
