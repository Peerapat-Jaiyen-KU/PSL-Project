import os
import pulp
import streamlit as st
import numpy as np
import pandas as pd

def load_data(file_path):
    return

def calculate_transportation_cost():
    return

def main():
    with st.form("Optimization Tool"):
        col1, col2, col3 = st.columns(3)

        col1.write("**Biomass Price**")
        biomass_price = {
            "Biomass Type": [
                "Cassava rhizome", "Coconut coir", "Coconut shell", "Corn stalk", "Corncob",
                "Palm empty fruit bunch", "Palm frond", "Palm kernel shell", "Palm trunk", "Rice husk",
                "Rice straw", "Rubber wood sawdust", "Sugarcane bagasse", "Sugarcane leaf"
            ],
            "Price (THB/ton)": [
                1800.00, 5000.00, 1000.00, 1500.00, 500.00, 50.00, 500.00,
                3200.00, 500.00, 1500.00, 2000.00, 600.00, 500.00, 800.00
            ]
        }

        biomass_price = pd.DataFrame(biomass_price)
        biomass_price = col1.data_editor(biomass_price, disabled=["Biomass Type"], hide_index=True)

        col2.write("**Truck Operational Parameters**")
        col3.write("**‎‎ **")
        truck_params = {
            "Fuel price": col2.number_input("Fuel price (THB/liter)", value=31.94, min_value=0.00, key="Fuel price"),
            "Fuel consumption rate": col3.number_input("Fuel consumption rate (km/liter)", value=5.00, min_value=0.00, key="Fuel consumption rate"),
            "Maintenance cost": col2.number_input("Average maintenance cost (THB/km)", value=0.60, min_value=0.00, key="Maintenance cost"),
            "Tire price": col3.number_input("Tire price (THB/tire)", value=8000.00, min_value=0.00, key="Tire price"),
            "Tire lifespan": col2.number_input("Tire lifespan (km)", value=70000.00, min_value=0.00, key="Tire lifespan"),
            "Number of tires": col3.number_input("Number of tires", value=10, min_value=0, key="Number of tires"),
            "Cargo width": col2.number_input("Cargo width (m)", value=2.30, min_value=0.00, key="Cargo width"),
            "Cargo length": col3.number_input("Cargo length (m)", value=2.30, min_value=0.00, key="Cargo length"),
            "Cargo height": col2.number_input("Cargo height (m)", value=2.30, min_value=0.00, key="Cargo height"),
            "Cargo capacity": col3.number_input("Cargo capacity (ton)", value=2.30, min_value=0.00, key="Cargo capacity"),
        }

        submit_button, _, reset_button = st.columns([1.2, 4.9, 1])

        if submit_button.form_submit_button("**Submit**", type="primary"):
            st.write("Yes!")

if __name__ == "__main__":
    main()
