import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Job Market Analysis Dashboard",
    layout="wide"
)

df = pd.read_csv("data/cleaned_postings.csv")

# Experience Level Filter

experience_options = ["All"] + sorted(
    df["formatted_experience_level"].dropna().unique().tolist()
)

selected_experience = st.sidebar.selectbox(
    "Select Experience Level",
    experience_options
)

if selected_experience != "All":
    df = df[
        df["formatted_experience_level"]
        == selected_experience
    ]


# Location Filter

location_options = ["All"] + sorted(
    df["location"].dropna().unique().tolist()
)

selected_location = st.sidebar.selectbox(
    "Select Location",
    location_options
)

if selected_location != "All":
    df = df[
        df["location"]
        == selected_location
    ]


# Work Type Filter

work_type_options = ["All"] + sorted(
    df["formatted_work_type"].dropna().unique().tolist()
)

selected_work_type = st.sidebar.selectbox(
    "Select Work Type",
    work_type_options
)

if selected_work_type != "All":
    df = df[
        df["formatted_work_type"]
        == selected_work_type
    ]
st.title("📊 Job Market Analysis Dashboard")
#*******************
st.sidebar.markdown("---")
st.sidebar.write(f"Filtered Jobs: {len(df):,}")
# KPI Metrics

total_jobs = df.shape[0]
total_companies = df["company_name"].nunique()
total_locations = df["location"].nunique()
median_salary = int(df["normalized_salary"].dropna().median())

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", f"{total_jobs:,}")
col2.metric("Total Companies", f"{total_companies:,}")
col3.metric("Total Locations", f"{total_locations:,}")
col4.metric("Median Salary", f"${median_salary:,}")


st.subheader("Experience Level Distribution")

experience_counts = (
    df["formatted_experience_level"]
    .value_counts()
    .reset_index()
)

experience_counts.columns = ["Experience Level", "Count"]

fig = px.bar(
    experience_counts,
    x="Experience Level",
    y="Count",
    title="Jobs by Experience Level"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Hiring Locations")

location_counts = (
    df["location"]
    .value_counts()
    .head(10)
    .reset_index()
)

location_counts.columns = ["Location", "Count"]

fig_locations = px.bar(
    location_counts,
    x="Location",
    y="Count",
    title="Top 10 Locations by Job Postings"
)

st.plotly_chart(fig_locations, use_container_width=True)

st.subheader("Top 10 Hiring Companies")

company_counts = (
    df[df["company_name"] != "Unknown"]["company_name"]
    .value_counts()
    .head(10)
    .reset_index()
)

company_counts.columns = ["Company", "Count"]

fig_companies = px.bar(
    company_counts,
    x="Company",
    y="Count",
    title="Top 10 Companies by Job Postings"
)

st.plotly_chart(fig_companies, use_container_width=True)

st.subheader("Salary Distribution")

salary_df = df[
    (df["normalized_salary"].notna()) &
    (df["normalized_salary"] <= 300000)
]

fig_salary = px.histogram(
    salary_df,
    x="normalized_salary",
    nbins=30,
    title="Salary Distribution"
)

st.plotly_chart(fig_salary, use_container_width=True)

st.markdown("---")
st.markdown(
    """
    **Built by Vinay**  
    Dataset: LinkedIn Job Postings  
    Tools: Python, Pandas, Streamlit, Plotly
    """
)
