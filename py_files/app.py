import streamlit as st
import json
import pandas as pd  # noqa: F401
import numpy as np  # noqa: F401


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
        st.caption("""The Linear Equation:
            Simple Linear Regression (one independent variable):
            y = β₀ + β₁x + ε

            where:

            y is the dependent variable.
            x is the independent variable.
            β₀ is the y-intercept (the value of y when x is 0).
            β₁ is the slope (the change in y for a one-unit change in x).
            ε is the error term (the difference between the actual y and the predicted y).""")
        st.image("../trained_data_graphs/diabetes_poverty_relationship.png", use_container_width=True)
        st.caption("A scatter plot relating poverty % to diabetes %")
        st.caption("The red line represents the linear regression model's predictions")
        st.caption("\nR² = 0.58\n")
        st.caption("""
            Correlation Coefficient (R): Measures the strength and direction of a linear relationship 
            between two variables. It ranges from -1 to +1.\n

            R-squared: Is the square of the correlation coefficient. It measures the proportion of 
            the variance in the dependent variable that is explained by the independent variable(s) 
            in a regression model.
            """)


def display_lasso_regression_graph():
    with st.expander("Lasso Regression between Poverty and Diabetes Percentage"):
        st.caption("""
        This graph visualizes the results of a Lasso Regression, a technique that not only models 
        the linear relationship between variables but also performs automatic feature selection 
        by shrinking the coefficients of less influential predictors towards zero.
        
        Lasso Cost Function:

        Cost Function = Σᵢ=₁ⁿ (yᵢ - (β₀ + Σⱼ=₁ᵖ βⱼ xᵢⱼ))² + λ Σⱼ=₁ᵖ |βⱼ|
        
        where:\n
        \tyᵢ = actual value of the dependent variable for the i-th observation\n
        \tβ₀ = y-intercept\n
        \tβⱼ = coefficient for the j-th independent variable\n
        \txᵢⱼ = value of the j-th independent variable for the i-th observation\n
        \tn = number of observations\n
        \tp = number of independent variables\n
        \tλ = regularization parameter (lambda)\n
        \t|βⱼ| = absolute value of the j-th coefficient\n
        
        """)
        st.image("../trained_data_graphs/lasso_regression_obesity_vs_diabetes.png",
                 use_container_width=True)
        st.caption("""
            A scatter plot relating obesity % to diabetes %\n
            
            Blue line: The blue line represents the Lasso Regression model's prediction of
            the relationship between Obesity_Percentage and Diabetes_Percentage.""")


def display_random_forest_pred():
    with st.expander("Random Forest Obesity Prediction"):
        st.caption("""
            Random Forest is a powerful and widely used machine learning algorithm, particularly 
            effective for both classification (predicting categories) and regression (predicting 
            continuous values). It operates by constructing a multitude of decision trees during the 
            training phase and then outputs the prediction based on the collective decision 
            of these trees.
            """)
        st.image("../trained_data_graphs/random_forest_obesity_prediction.png",
                 use_container_width=True)
        st.caption("""
            This plot compares the predicted values to the actual values.
            Interpretation:
            Each point represents a predicted value (y_pred) against its corresponding actual 
            value (y_test).
            The red dashed line represents a perfect prediction where the predicted value equals 
            the actual value. The closer the blue points are to this red line, the better your model 
            is at predicting.
            If the points are spread out far from the line, it means the predictions are not accurate.
            Ideally, you'd want most points to be clustered around the red line, showing that the 
            model’s predictions are close to the actual values.
        """)

def display_random_forest_res():
    with st.expander("Random Forest Obesity Residual"):
        st.caption("""
                Purpose: This plot shows the residuals (errors) between your predicted values and 
                actual values. It's used to evaluate whether a model is underfitting or overfitting.
                \n\nInterpretation:
                \tThe x-axis represents the predicted values, and the y-axis shows the residuals 
                (y_test - y_pred).
                \tThe red line is a smoothed line through the residuals. If a model is correctly 
                capturing the patterns in the data, the residuals should be scattered randomly around 
                this line with no clear pattern.
                \tIf the residuals are randomly scattered and do not follow a specific pattern 
                (i.e., there is no clear trend or curve), this indicates that the model is well-fitting.
                \tIf a pattern emerges (e.g., a U-shape or a trend), it could mean the model is 
                underfitting or not capturing certain patterns in the data.
                """)
        st.image("../trained_data_graphs/random_forest_obesity_residual.png", use_container_width=True)


def display_poverty_obesity_growth():
    with st.expander("Obesity/Diabetes Growth with Linear Regression"):
        st.caption("""
        To examine the relationship between the rate of growth for obesity percentage and the rate 
        of growth for diabetes percentage over a given period. We specifically focus on understanding 
        whether there is a correlation between the two variables and how their growth rates relate 
        to each other.

        Rate of Growth Calculation: The rate of growth is calculated using the formula:
        (current_value - previous_value) / previous_value
        for both obesity percentage and diabetes percentage.
        """)
        st.image("../trained_data_graphs/diabetes_growth_vs_obesity_growth.png",
                 use_container_width=True)


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

