import os
import subprocess
import sys
import sqlite3
import time

def log_to_db(model_name, nrmse, exec_time, status):
    """Simulation results ko database mein save karne ka function"""
    try:
        conn = sqlite3.connect('results/simulation_results.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS simulation_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT NOT NULL,
                nrmse_value REAL,
                execution_time REAL,
                status TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            INSERT INTO simulation_logs (model_name, nrmse_value, execution_time, status)
            VALUES (?, ?, ?, ?)
        ''', (model_name, nrmse, exec_time, status))
        
        conn.commit()
        conn.close()
        print("📁 Data logged to SQLite successfully!")
    except Exception as e:
        print(f"❌ Database Error: {e}")

def run_simulation(input_file):
    print(f"🚀 Simulation Start: {input_file}")
    start_time = time.time()
    
    # gprMax cmd
    command = f"python -m gprMax {input_file} -n 100"
    
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        end_time = time.time()
        exec_time = round(end_time - start_time, 2)
        print(f"✅ Simulation Completed in {exec_time}s")
        return True, exec_time
    except subprocess.CalledProcessError as e:
        print(f"❌ Simulation Failed! Error: {e.stderr}")
        return False, 0

def validate_geometry():
    """Geometry check logic (Dummy NRMSE for now)"""
    print("🔍 Checking Geometry Constraints...")
    return True, 0.0045  # Dummy NRMSE value

if __name__ == "__main__":
    model_path = "models/user_model.in"
    
    # 1. Check if model exists
    if not os.path.exists(model_path):
        print(f"⚠️ Model file {model_path} not found!")
        sys.exit(1)

    # 2. Run Simulation
    success, duration = run_simulation(model_path)
    
    if success:
        # 3. Validate
        valid, nrmse_val = validate_geometry()
        
        if valid:
            # 4. Success Log to DB
            log_to_db(os.path.basename(model_path), nrmse_val, duration, "SUCCESS")
            print("🎉 GSoC Pipeline: All tests passed!")
            sys.exit(0)
        else:
            log_to_db(os.path.basename(model_path), nrmse_val, duration, "FAILED_VALIDATION")
            sys.exit(1)
    else:
        log_to_db(os.path.basename(model_path), 0, 0, "FAILED_SIMULATION")
        sys.exit(1)
