import streamlit as st
import json
import io
import pandas as pd  # noqa: F401
import numpy as np  # noqa: F401
import matplotlib.pyplot as plt
from contextlib import redirect_stdout


def get_notebook():
    with open("Diabetes_Mining.ipynb", "r", encoding="utf-8") as file:
        return json.load(file)


def get_data_frames(ntbk):
    diabetes_data, obesity_data, poverty_data, food_security_data = [
        pd.read_parquet("data_frames/diabetes_data.parquet"),
        pd.read_parquet("data_frames/obesity_data.parquet"),
        pd.read_parquet("data_frames/poverty_data.parquet"),
        pd.read_parquet("data_frames/food_security_data.parquet"),
    ]
    return diabetes_data, obesity_data, poverty_data, food_security_data


def config_page_and_title():
    st.set_page_config(page_title="⚕️ Health in Numbers ⚕️", layout="centered")

    st.markdown(  # Title
        "<h1 style='text-align: center;'>⚕️ Health in Numbers ⚕️</h1>",
        unsafe_allow_html=True
    )

    st.markdown(  # Subtitle
        "<h3 style='text-align: center;'>Mapping the Metrics of Food and Health</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h5 style='text-align: center;'>🚧 Website Under Construction 🚧</h5>",
        unsafe_allow_html=True
    )


def readme_expander():
    with st.expander("README"):
        with open("README.md", "r") as file:
            readme_contents = file.read()
        st.markdown(readme_contents)


def exploratory_expander(ntbk):
    for cell in ntbk["cells"]:
        if cell["cell_type"] == "code":
            source = cell["source"]
            if source and source[0].strip() == "# INCLUDE":
                title = source[1].strip("# ")
                code_to_run = "".join(source[2:])

                # Execute code and capture output
                fig = None
                buffer = io.StringIO()

                with redirect_stdout(buffer):
                    try:
                        exec(code_to_run, globals())

                        # Try to find the matplotlib figure
                        fig = plt.gcf()
                    except Exception as e:
                        st.error(f"Error running code for '{title}': {e}")
                        continue

                with st.expander(title):
                    if fig:
                        st.pyplot(fig)
                        plt.clf()  # Clear after rendering
                    output = buffer.getvalue()
                    if output.strip():
                        st.code(output, language='text')


if __name__ == "__main__":
    notebook = get_notebook()
    diabetes_data, obesity_data, poverty_data, food_security_data = get_data_frames(notebook)

    config_page_and_title()
    readme_expander()
    exploratory_expander(notebook)

