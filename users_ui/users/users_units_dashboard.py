# Show Overview data like total users, total units..
import streamlit as st
import os


def drawUsersDashboard():
    current_dir=os.getcwd()
    user_permissions = st.session_state.user_permissions
    Pods_pages = []
    for i in range(1, 11):
        pod = f"Pod-{i}"
        if pod in user_permissions:
            page = st.Page(f"{current_dir}/units/pod_{i}.py", title=f"POD {i}", icon="🛜", default=(i == 1))
            Pods_pages.append(page)

    pages = {
        "Units": Pods_pages
    }
    pg = st.navigation(pages)
    st.logo(f"{current_dir}/images/logo.png",size="large")
    st.sidebar.subheader("Demo ")
    st.sidebar.markdown("Anedya Demo Dashbaord")
    pg.run()
    
    
