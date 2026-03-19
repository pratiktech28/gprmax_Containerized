🚀 gprMax Automated CI/CD & Dockerization
📌 Project Overview
Is project ka main goal gprMax (Ground Penetrating Radar simulation) ko containerize karna aur ek fully automated CI/CD Pipeline set up karna hai. Isse physics simulations kisi bhi machine par bina installation errors ke chal sakti hain.

🛠 Tech Stack Used
Infrastructure: Docker (Containerization)

Automation: GitHub Actions (CI/CD)

Language: Python 3.11, HTML/CSS (Interface)

Physics Engine: gprMax

🚀 Workflow Architecture
Code Commit: Developer pushes code (HTML interface + Dockerfile).

Trigger: GitHub Actions identifies the push event.

Environment Setup: A virtual Ubuntu runner is allocated.

Docker Build: The system builds the image using python:3.11-slim.

Installation: gprMax and its dependencies (numpy, cython, h5py) are installed inside the container.

Verification: Automated integration tests are executed.

Push: Final verified environment is ready for deployment.

📂 Project Structure
Plaintext
├── .github/workflows/
│   └── main.yml          # GitHub Actions Configuration (The Engine)
├── Docker/
│   └── Dockerfile        # Container Blueprints (Python 3.11 + gprMax)
├── scripts/
│   └── integration_test.py # Automated Physics Tests
├── index.html            # Web Interface for results
└── README.md             # Project Documentation
🐳 How to Run Locally
Agar aapko ye environment apne local machine par chalana hai:

Clone the Repo:

Bash
git clone https://github.com/your-username/gprMax_Containerized.git
cd gprMax_Containerized
Build Docker Image:

Bash
docker build -t gprmax-automation -f Docker/Dockerfile .
Run Simulation:

Bash
docker run --rm gprmax-automation
📈 CI/CD Implementation Logs
Humne successfully complex installation hurdles ko solve kiya:

✅ Branch Mismatch Fix: master to main transition.

✅ Case Sensitivity: Corrected Docker/Dockerfile path mapping.

✅ Python Compatibility: Upgraded to 3.11-slim for latest gprMax support.

✅ Cloud Verification: Achieved Green Tick on GitHub Actions.
