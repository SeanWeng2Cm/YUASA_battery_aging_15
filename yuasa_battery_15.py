import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Test Plot: Internal Resistance")

# Sample data
time = np.linspace(0, 5, 11)
R_25 = np.array([1.0, 1.05, 1.1, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 3.75, 4.5])

# Arrhenius factor calculation
Ea = 0.5 * 1.60218e-19 * 6.022e23
Rg = 8.314
T_ref = 298
T = 288
factor = np.exp((Ea / Rg) * (1 / T - 1 / T_ref))
R_15 = R_25 * factor

# Plotly plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=R_25, mode='lines+markers', name='25°C'))
fig.add_trace(go.Scatter(x=time, y=R_15, mode='lines+markers', name='15°C'))

fig.update_layout(
    title="Battery Internal Resistance (25°C vs 15°C)",
    xaxis_title="Time (Years)",
    yaxis_title="Internal Resistance",
    template="plotly_white"
)

# Display the plot
st.plotly_chart(fig)
