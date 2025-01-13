# Show Overview data like total users, total units..
import streamlit as st
import os


def drawUsersDashboard():
    current_dir=os.getcwd()
    user_permissions = st.session_state.user_permissions
    Units_pages = []
    for i in range(1, 11):
        unit = f"Unit-{i}"
        if unit in user_permissions:
            page = st.Page(f"{current_dir}/units/pod_{i}.py", title=f"POD {i}", icon="🛜", default=(i == 1))
            Units_pages.append(page)

    pages = {
        "Units": Units_pages
    }
    pg = st.navigation(pages)
    st.logo(f"{current_dir}/images/logo.png",size="large")
    st.sidebar.subheader("Urban Nap ")
    st.sidebar.markdown("Offers innovative nap pods that enhance productivity and well-being.")
    pg.run()
    
    
