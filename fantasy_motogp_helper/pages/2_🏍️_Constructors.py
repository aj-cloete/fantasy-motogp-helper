import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer

from fantasy import FantasyStats

st.markdown("# Constructors 🏍️")
# st.sidebar.markdown("# Constructors 🏍️")

basic, stats, history, all_data = st.tabs(["Basic Info", "Point Stats", "History", "All Data"])

data = FantasyStats().constructors


with basic:
    st.table(
        dataframe_explorer(
            data.info.sort_values("cost", ascending=False)
        )
    )

with stats:
    st.table(
        dataframe_explorer(
            data.stats#.sort_values(["avg_points", "last_event"], ascending=False)
        )
    )

with history:
    st.table(
        dataframe_explorer(
            data.history
        )
    )

with all_data:
    st.table(dataframe_explorer(data.all_data))
