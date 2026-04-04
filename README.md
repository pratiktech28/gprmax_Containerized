[![gprMax CI/CD Trident Pipeline](https://github.com/pratiktech28/gprmax_Containerized/actions/workflows/main.yml/badge.svg)](https://github.com/pratiktech28/gprmax_Containerized/actions/workflows/main.yml)


<img width="400" height="200" alt="logo_gprMax" src="https://github.com/user-attachments/assets/b2430b3e-9ccb-4f07-84a2-0a991d01d254" />


<img width="600" height="73" alt="download" src="https://github.com/user-attachments/assets/679dc592-7b1a-4084-9f32-53e42108b810" />

<img width="318" height="159" alt="download" src="https://github.com/user-attachments/assets/166fcd52-342f-463b-bd1f-145c62c736b5" />


<img width="300" height="168" alt="download" src="https://github.com/user-attachments/assets/7f766db7-394f-4ee0-adcd-815712d9cb59" />


<img width="332" height="152" alt="download" src="https://github.com/user-attachments/assets/c51d1710-fa1e-4622-97e0-b930751e1648" />


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
  <img src="https://img.shields.io/badge/Mysql-003B57?style=for-the-badge&logo=Mysql&logoColor=white" alt="Mysql">
</p>

---

## 📖 Overview
This project aims to revolutionize the development workflow of gprMax by implementing a **Containerized CI/CD Pipeline (The Trident Pipeline).** By leveraging Docker and GitHub Actions, we ensure that every physics simulation is automatically validated across isolated environments, preventing regression errors and streamlining the contribution process for researchers worldwide.


---
<div align="center">
  <h1>🏗️ gprmax_Containerized: The Trident Pipeline</h1>
  <p><strong>Automated CI/CD & Physics-Based Regression Testing for gprMax (GSoC 2026)</strong></p>
  <div style="display:none;">
    Keywords: gprMax CI/CD, Trident Pipeline Architecture, 
    Physics-Aware Automation, NRMSE Validation Gate, 
    Kubernetes Simulation Clusters, Automated A-scan Extraction, 
    Dockerized gprMax v3.1.7, GPR Data Integrity, 
    Prateek Sharma GSoC Proposal, Dr. Craig Warren gprMax.
  </div>

  <div>
    <p align="center">
    <img src="https://github.com/user-attachments/assets/66b97491-1502-4369-9c5d-7f56b8e51e65" alt="GSoC 2026">
    <img src="https://github.com/user-attachments/assets/e167672d-72a2-48b6-97e9-339a4e9436f2" alt="gprMax">
    <img src="https://github.com/user-attachments/assets/735b33f5-d04b-415f-af1f-fd1b267fd8fc" alt="Physics validation">
  </p>
</div>


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

**🚀 Database & Automation Setup**
<br>
To ensure data persistence for physics simulations (gprMax), the project uses a Dockerized MySQL instance. This allows for automated logging of NRMSE values and simulation status.
**Simulation Logs Schema**
We track each simulation run with high precision to monitor convergence and physics accuracy.

<img width="698" height="199" alt="image" src="https://github.com/user-attachments/assets/d204f5fe-3ef6-4a63-b929-c4056de42129" />


---

**Resilient Infrastructure & Orchestration**

The project is designed to handle high-performance GPR simulations that can be resource-intensive. To ensure zero downtime and handle potential container failures, we leverage orchestration principles.
<br>
**Self-Healing & Auto-Scaling (The K8s Strategy)**
**Self-Healing**: If a Docker container crashes due to a resource-intensive simulation (OOM or Segfault), the ReplicaSet immediately detects the failure and spins up a healthy pod to maintain the desired state.
<br>
**Dynamic Scaling**: To optimize the "100 Parallel Pads" Roadmap, the system can use a Horizontal Pod Autoscaler (HPA). When the CPU/Memory load increases during massive physics computations, it can automatically scale the cluster from 10 replicas to 100 replicas in real-time.
<br>
<img width="1335" height="154" alt="image" src="https://github.com/user-attachments/assets/9e4ebe60-5aad-4570-ba02-eb04b4522b0f" />

---



**Infrastructure & Scalability**
<br>
**🚀 Automated Milestone Tracking**
<br>
The project integrates a Dockerized MySQL backend to maintain a persistent and transparent record of the development lifecycle. Unlike static documentation, this live database ensures that every stage of the "100 Parallel Pads" implementation is tracked with precision.
<br>
**Data Persistence**: Using a dedicated container ensures that roadmap data and simulation results remain intact, even across system reboots.
<br>
**Operational Transparency**: By querying the gsoc_roadmap table, mentors can verify real-time progress against the proposed timeline.
<br>
**Structured Planning**: Each task is categorized by week and status, providing a clear path from the initial infrastructure setup to final cloud deployment.
<br>
<img width="752" height="211" alt="image" src="https://github.com/user-attachments/assets/1ca61b9c-7551-44e4-bb34-5a09768f786a" />
<br>



---



**Physics Validation & High-Performance Scaling**
<br>
A core focus of this gprMax project is maintaining physics integrity while scaling computational resources. To achieve this, the system is designed to handle massive parallelization across multiple environments.
<br>
**Automated NRMSE Logging**: Every simulation run automatically pushes its NRMSE (Normalized Root Mean Square Error) value to the database. This allows for immediate detection of physics deviations during kernel optimization.
<br>
**Self-Healing Clusters**: By leveraging Kubernetes orchestration principles, the infrastructure is built to be fault-tolerant. If a simulation pod crashes under heavy load, the system automatically respawns it to maintain the desired state.
<br>
**Elastic Cloud Scaling**: The architecture supports dynamic scaling from 10 to 100 replicas on cloud platforms like GCP or AWS. This ensures that the "100 Parallel Pads" roadmap can be executed smoothly without resource stalling or local hardware limitations.
<br>

<img width="601" height="196" alt="image" src="https://github.com/user-attachments/assets/fa8a7a94-4b5d-4399-9bcf-e0d5a067a9e3" />


---



## 🛠️ Tech Stack & Requirements

| Category | Technology Used | Purpose |
| :--- | :--- | :--- |
| **Simulation Engine** | gprMax (Latest) | Electromagnetic wave simulation. |
| **Virtualization** | Docker | Environment consistency and isolation. |
| **Acceleration** | OpenMP / Cython | Parallel processing and code optimization. |
| **Data Logging** | Mysql | Persistent storage for simulation metadata. |
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
<br>

## 🌍 Global Scaling & Multi-Region Orchestration
The final phase focuses on a **Global Simulation Network** for the international GPR research community:

1.  **Federated K8s Clusters:** Distributing simulation loads across global regions (AWS/GCP/Azure) to reduce researcher latency.
2.  **Massive Parallelism:** Scaling to **100+ concurrent worker pods** for rapid AI/ML synthetic data generation.
3.  **Edge Integration:** Deploying lightweight containers for real-time, on-site structural health monitoring.
4.  **Distributed RWX Storage:** Aggregating global outputs into a unified "Global Golden Dataset".
---



