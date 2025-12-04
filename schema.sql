CREATE TABLE IF NOT EXISTS wind_turbine_data (
    "Timestamp" TIMESTAMP WITHOUT TIME ZONE,
    "Turbine_ID" VARCHAR(50),
    "Wind_Speed_m_s" DOUBLE PRECISION,
    "Power_Output_kW" DOUBLE PRECISION,
    "Grid_Voltage_V" DOUBLE PRECISION,
    "Rotor_Current_A" DOUBLE PRECISION,
    "Ambient_Temp_C" DOUBLE PRECISION,
    "IGBT_Phase_Temp_C" DOUBLE PRECISION,
    "Status" VARCHAR(20),
    "Error_Code" INTEGER
);
