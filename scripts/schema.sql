-- gprMax Simulation Results Table
CREATE TABLE IF NOT EXISTS simulation_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT NOT NULL,          
    nrmse_value REAL,                  
    execution_time REAL,              
    status TEXT,                       
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Geometry Configuration Table
CREATE TABLE IF NOT EXISTS geometry_configs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sim_id INTEGER,
    grid_size TEXT,                
    iterations INTEGER,
    FOREIGN KEY (sim_id) REFERENCES simulation_logs(id)
);
