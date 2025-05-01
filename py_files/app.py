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
        pd.read_parquet("../data_frames/diabetes_data.parquet"),
        pd.read_parquet("../data_frames/obesity_data.parquet"),
        pd.read_parquet("../data_frames/poverty_data.parquet"),
        pd.read_parquet("../data_frames/food_security_data.parquet"),
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
        with open("../README.md", "r") as file:
            readme_contents = file.read()
        st.markdown(readme_contents)


def display_map():
    # Apply custom CSS to change the expander's size
    st.markdown("""
        <style>
            .st-expanderHeader {
                font-size: 20px;  /* Adjust the font size of the expander header */
                padding: 10px;  /* Adjust padding for the header */
            }
            .st-expanderContent {
                max-height: 1000px;  /* Adjust the content's height */
                overflow-y: scroll;  /* Enable scrolling if content exceeds height */
            }
        </style>
    """, unsafe_allow_html=True)

    with st.expander("🗺️ Interactive Map"):
        with open("state_map.html", "r", encoding="utf-8") as f:
            folium_html = f.read()
        st.components.v1.html(folium_html, height=1000, scrolling=True)


def display_linear_regression_graph():
    with st.expander("Linear Regression Relationship between Poverty and Diabetes Percentage"):
        st.image("../trained_data_graphs/diabetes_poverty_relationship.png", use_container_width=True)


def display_lasso_regression_graph():
    with st.expander("Lasso Regression between Poverty and Diabetes Percentage"):
        st.image("../trained_data_graphs/lasso_regression_obesity_vs_diabetes.png", use_container_width=True)


def display_random_forest_pred():
    with st.expander("Random Forest Obesity Prediction"):
        st.image("../trained_data_graphs/random_forest_obesity_prediction.png", use_container_width=True)


def display_random_forest_res():
    with st.expander("Random Forest Obesity Residual"):
        st.image("../trained_data_graphs/random_forest_obesity_residual.png", use_container_width=True)


def display_poverty_obesity_growth():
    with st.expander("Obesity/Diabetes Growth with Linear Regression"):
        st.image("../trained_data_graphs/diabetes_growth_vs_obesity_growth.png", use_container_width=True)


if __name__ == "__main__":
    config_page_and_title()
    notebook = get_notebook()
    diabetes_data, obesity_data, poverty_data, food_security_data = get_data_frames(notebook)
    readme_expander()
    display_map()
    display_linear_regression_graph()
    display_lasso_regression_graph()
    display_random_forest_pred()
    display_random_forest_res()
    display_poverty_obesity_growth()

