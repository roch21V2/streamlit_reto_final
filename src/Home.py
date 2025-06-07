import streamlit as st

st.set_page_config(
    page_title="BookML Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    # Set the title of the dashboard
    st.title("📚 BookML Main Menu 🤖")

    st.markdown("""
    Welcome to the **Hotel Occupancy Dashboard**! This app provides an interactive overview of hotel usage over time and offers powerful forecasting tools.

    ---
    
    ### 📊 **Dashboard Overview**
    - View multiple **timeseries metrics and graphs** from the hotel database.
    - Analyze **occupancy rates** and **number of guests** over different periods.
    - Apply dynamic **date filters** to focus on specific time ranges.
    
    ---
    
    ### 🤖 **Prediction Models**
    - Access machine learning models to **predict future occupancy**.
    - Forecast both:
        - 📈 **Occupancy Rate**
        - 🧍‍♂️ **Number of Guests**
    - Useful for **trend analysis**, **resource planning**, and **decision-making**.
    
    ---
    
    ### 🔎 **Filters**
    - Filter by **date range** to explore historical data or test predictions.
    
    ---
    
    ### 📂 **Source Code**
    
    * **Models** 
      [*(View the project on GitHub)*](https://github.com/Azahramirez/claseMreporeto)

    * **Backend** 
      [*(View the project on GitHub)*](https://github.com/roch21V2/api)

    * **Frontend** 
      [*(View the project on GitHub)*](https://github.com/roch21V2/streamlit_reto_final)
    """)


if __name__ == "__main__":
    main()
