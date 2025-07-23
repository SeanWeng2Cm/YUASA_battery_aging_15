import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set up the page
st.set_page_config(page_title="Battery Internal Resistance Estimation", layout="centered")

st.title("Battery Internal Resistance Estimation using Arrhenius Equation")

# Data at 25°C (Years, Resistance)
time = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
R_25 = np.array([1.0, 1.05, 1.1, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 3.75, 4.5])

# User-selectable temperature
T_ref = 298  # 25°C in Kelvin
T_celsius = st.slider("Select Target Temperature (°C)", min_value=0, max_value=30, value=15)
T = T_celsius + 273.15  # Convert to Kelvin

# Constants
Ea = 0.5 * 1.60218e-19 * 6.022e23  # eV to J/mol
Rg = 8.314  # J/mol·K

# Calculate Arrhenius temperature correction factor
factor = np.exp((Ea / Rg) * (1 / T - 1 / T_ref))

# Estimate resistance at selected temperature
R_estimated = R_25 * factor

# Plotting
fig, ax = plt.subplots()
ax.plot(time, R_25, label='25°C Original Resistance', marker='o')
ax.plot(time, R_estimated, label=f'{T_celsius}°C Estimated Resistance', marker='x')
ax.set_xlabel('Time (Years)')
ax.set_ylabel('Internal Resistance (Ω)')
ax.set_title('Internal Resistance over Time')
ax.legend()
ax.grid(True)

# Show plot in Streamlit
st.pyplot(fig)

# Show factor value
st.write(f"Arrhenius Correction Factor: **{factor:.3f}**")
