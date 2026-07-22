import streamlit as st
from components.profiler import show_boxplot
from services.profiler import numeric_columns
from components.profiler import show_distribution
from services.profiler import correlation_matrix
from components.profiler import show_correlation_heatmap
from components.profiler import show_categorical_summary
from services.profiler import categorical_summary
from components.profiler import show_descriptive_statistics
from services.profiler import descriptive_statistics
from components.profiler import show_data_type_chart
from components.profiler import show_data_types
from services.profiler import data_type_summary
from services.profiler import profile_data
from components.profiler import show_profile
from services.profiler import missing_values_summary
from components.profiler import show_missing_values
from components.header import show_header
from components.sidebar import show_sidebar
from components.uploader import upload_file
from services.data_loader import load_data

def main():
    st.set_page_config(
        page_title="AI Business Analyst Assistant",
        page_icon="🤖",
        layout="wide"
    )

    show_sidebar()
    show_header()

    uploaded_file = upload_file()

    if uploaded_file is not None:
        try:
            df = load_data(uploaded_file)
            profile = profile_data(df)
            missing_summary = missing_values_summary(df)
            st.success("✅ File uploaded successfully!")

            st.write("### Dataset Preview")
            st.dataframe(df.head())

            show_profile(profile)
            show_missing_values(missing_summary)
            dtype_summary = data_type_summary(df)
            stats = descriptive_statistics(df)
            categorical = categorical_summary(df)
            correlation = correlation_matrix(df)
            numeric_cols = numeric_columns(df)
            show_data_types(dtype_summary)
            show_data_type_chart(dtype_summary)
            show_descriptive_statistics(stats)
            show_categorical_summary(categorical)
            show_correlation_heatmap(correlation)
            show_distribution(df, numeric_cols)
            show_boxplot(df, numeric_cols)
        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()