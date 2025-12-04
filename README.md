# Wind-Turbine-Fault-Detection
"Data Analytics project analyzing Nordex Wind Turbine sensor data using Python, SQL, and Power BI."
# 🌬️ Wind Turbine Fault Detection Project

## 📌 Project Overview
This project simulates and analyzes sensor data from a **Nordex Main Converter** system. The goal is to detect overheating faults in specific turbines using Data Analytics techniques.

## 🛠️ Tech Stack Used
* **Python:** For simulating SCADA sensor data (Wind Speed, Power, IGBT Temp) and ETL processes.
* **SQL (PostgreSQL):** For data warehousing and structured querying.
* **Power BI:** For building an interactive dashboard to visualize faults.

## 🔍 Key Insights
* Simulated **22,000+ sensor logs** for 5 turbines.
* Identified **Turbine 003** as the faulty unit due to abnormal IGBT temperature spikes (>90°C) inconsistent with power output.
* The dashboard allows real-time monitoring of fault counts and efficiency metrics.

## 📂 File Structure
* `data_generation.py`: Script to generate the dummy sensor dataset.
* `load_data.py`: Automation script to load CSV data into PostgreSQL.
* `schema.sql: SQL script to define the database table structure.
* `Dashboard.png`: Preview of the final Power BI dashboard.
