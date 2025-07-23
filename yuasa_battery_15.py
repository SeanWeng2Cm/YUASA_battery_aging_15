import streamlit as st
import numpy as np
import plotly.graph_objs as go

# Title
st.title("Battery Internal Resistance Estimation (25°C vs 15°C)")

# Data: Time (years) and Resistance at 25°C
time = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
R_25 = np.array([1.0, 1.05, 1.1, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 3.75, 4.5])

# Constants for Arrhenius equation
Ea = 0.5 * 1.60218e-19 * 6.022e23
