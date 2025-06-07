import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st

from config.constants import BACKEND_BASE_URL

st.title("Welcome to the BookML Predictions Page! 📚🤖")

model_name = st.selectbox(
    "Select a model to make predictions",
    # Names that are with the mlflow registry
    options=[
        "TR_ocupacion",
        "TOcupacion_Tocu",
        "TOcupacion_NumAdu253",
        "TOcupacion_NumAdu173",
        "TOcupacion_NumAdu48",
        "TOcupacion_NumAdu5",
        "IngHab",
    ],
)

url_fastapi = f"{BACKEND_BASE_URL}/predict/{model_name}"


st.markdown("## Model Prophet_model")
st.markdown("### Model Description")
st.markdown("""
This model is designed to forecast employing the Prophet algorithm, which is particularly effective for time series forecasting, especially when dealing with seasonal effects and holidays.
""")

st.markdown("### Model Features")
start_date = st.date_input(
    "Select the start date for predictions",
    value=st.session_state.get("start_date", None),
)
end_date = st.date_input(
    "Select the end date for predictions", value=st.session_state.get("end_date", None)
)

if model_name in ["TR_ocupacion", "TOcupacion_Tocu"]:
    prediction = requests.post(
        url_fastapi, json={"start_date": str(start_date), "end_date": str(end_date)}
    )
else:
    prediction = requests.post(
        url_fastapi,
        json={
            "start_date": str(start_date),
            "end_date": str(end_date),
            "cap": 10000000000,  # Optional, default to 1.0
            "floor": 0.0,  # Optional, default to 0.0
        },
    )


if prediction.status_code == 200:
    prediction_data = prediction.json()

    if model_name in ["TR_ocupacion", "TOcupacion_Tocu"]:
        st.write("Predicted Occupancy Rates and Number of Guests:")
    else:
        st.write("Predicted Revenue:")

elif prediction.status_code == 400:
    st.error("Invalid input data. Please check the date range and try again.")


### Plot the predictions
if prediction.status_code == 200:
    df = pd.DataFrame(prediction_data)
    df["ds"] = pd.to_datetime(df["ds"])

    fig = go.Figure()

    # Add the lower bound first
    fig.add_trace(
        go.Scatter(
            x=df["ds"],
            y=df["yhat_lower"],
            mode="lines",
            line=dict(width=0),
            name="Lower Bound",
            showlegend=False,
        )
    )

    # Add the upper bound and fill to the previous trace
    fig.add_trace(
        go.Scatter(
            x=df["ds"],
            y=df["yhat_upper"],
            mode="lines",
            fill="tonexty",
            fillcolor="rgba(176,224,230,0.2)",  # adjust color and opacity
            line=dict(width=0),
            name="Confidence Interval",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["ds"],
            y=df["yhat"],
            mode="lines",
            name="Prediction",
            line=dict(color="red"),
        )
    )

    # Customize layout
    fig.update_layout(
        title="Predicted Values",
        xaxis_title="Date",
        yaxis_title="Ocupcación"
        if model_name in ["TR_ocupacion", "TOcupacion_Tocu"]
        else "Revenue",
        template="plotly_white",
    )

    # Show plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)
