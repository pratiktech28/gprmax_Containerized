-- gprMax Simulation Results Table
CREATE TABLE IF NOT EXISTS simulation_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT NOT NULL,          -- Model file ka naam (e.g., user_model.in)
    nrmse_value REAL,                  -- Accuracy check (0.0 to 1.0)
    execution_time REAL,               -- Kitni der chala simulation
    status TEXT,                       -- 'SUCCESS' ya 'FAILED'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Geometry Configuration Table
CREATE TABLE IF NOT EXISTS geometry_configs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sim_id INTEGER,
    grid_size TEXT,                    -- e.g., "0.002, 0.002, 0.002"
    iterations INTEGER,
    FOREIGN KEY (sim_id) REFERENCES simulation_logs(id)
);