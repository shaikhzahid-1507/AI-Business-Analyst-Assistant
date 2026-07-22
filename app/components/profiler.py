import streamlit as st
import plotly.express as px


# ==========================================================
# DATASET OVERVIEW
# ==========================================================

def show_profile(profile):
    """
    Display dataset profiling KPIs.
    """

    st.divider()
    st.subheader("📊 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", profile["rows"])

    with col2:
        st.metric("Columns", profile["columns"])

    with col3:
        st.metric("Missing Values", profile["missing_values"])

    with col4:
        st.metric("Duplicate Rows", profile["duplicate_rows"])

    st.write("")

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric("Memory (MB)", profile["memory_usage_mb"])

    with col6:
        st.metric("Numeric Columns", profile["numeric_columns"])

    with col7:
        st.metric("Categorical Columns", profile["categorical_columns"])


# ==========================================================
# MISSING VALUES
# ==========================================================

def show_missing_values(summary):
    """
    Display missing values summary.
    """

    st.divider()
    st.subheader("📋 Missing Values Analysis")

    if summary.empty:
        st.success("🎉 No missing values found in the dataset!")
    else:
        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True,
        )


# ==========================================================
# DATA TYPES TABLE
# ==========================================================

def show_data_types(summary):
    """
    Display data types summary.
    """

    st.divider()
    st.subheader("🧬 Data Types Summary")

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True,
    )


# ==========================================================
# DATA TYPE CHART
# ==========================================================

def show_data_type_chart(summary):
    """
    Display data type distribution using Plotly.
    """

    st.divider()
    st.subheader("📊 Data Type Distribution")

    fig = px.bar(
        summary,
        x="Count",
        y="Data Type",
        orientation="h",
        text="Count",
        color="Data Type",
    )

    fig.update_layout(
        xaxis_title="Number of Columns",
        yaxis_title="Data Type",
        height=400,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
def show_descriptive_statistics(stats):
    """
    Display descriptive statistics.
    """

    st.divider()
    st.subheader("📈 Descriptive Statistics")

    st.dataframe(
        stats,
        use_container_width=True,
        hide_index=True,
    )


def show_categorical_summary(summary):
    """
    Display categorical column summary.
    """

    st.divider()
    st.subheader("📝 Categorical Columns Summary")

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True,
    )


def show_correlation_heatmap(correlation):
    """
    Display correlation heatmap.
    """

    st.divider()
    st.subheader("🔥 Correlation Heatmap")

    fig = px.imshow(
        correlation,
        text_auto=True,
        color_continuous_scale="RdBu",
        aspect="auto",
        zmin=-1,
        zmax=1,
    )

    fig.update_layout(
        height=600,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def show_distribution(df, numeric_cols):
    """
    Display histogram for selected column.
    """

    st.divider()
    st.subheader("📈 Distribution Analysis")

    selected = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    fig = px.histogram(
        df,
        x=selected,
        nbins=30,
        title=f"Distribution of {selected}",
    )

    fig.update_layout(
        height=500,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
def show_boxplot(df, numeric_cols):
    """
    Display box plot for outlier analysis.
    """

    st.divider()
    st.subheader("📦 Outlier Analysis")

    selected = st.selectbox(
        "Select Column for Box Plot",
        numeric_cols,
        key="boxplot"
    )

    fig = px.box(
        df,
        y=selected,
        title=f"Box Plot of {selected}",
        points="outliers"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )