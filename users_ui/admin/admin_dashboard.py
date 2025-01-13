# Show Overview data like total users, total units..
import streamlit as st
import os


def drawAdminDashboard():
    
    current_dir=os.getcwd()
    pages = {
        "Admin": [
            st.Page(f"{current_dir}/users_ui/admin/sections/admin_dashboard.py", title="Admin Dashboard"),
            st.Page(f"{current_dir}/users_ui/admin/sections/create_users.py", title="Create Users",default=True),
            st.Page(f"{current_dir}/users_ui/admin/sections/users_managements.py", title="Users Managements"),
        ],
        "Units": [
            st.Page(f"{current_dir}/units/pod_1.py", title="POD 1", icon="🛜"),
            st.Page(f"{current_dir}/units/pod_2.py", title="POD 2",icon="🛜"),
            st.Page(f"{current_dir}/units/pod_3.py", title="POD 3",icon="🛜"),
            st.Page(f"{current_dir}/units/pod_4.py", title="POD 4",icon="🛜"),
            st.Page(f"{current_dir}/units/pod_5.py", title="POD 5",icon="🛜"),
  
        ]
    }
    pg = st.navigation(pages)
    st.logo(f"{current_dir}/images/logo.png",size="large")
    st.sidebar.subheader("Urban Nap ")
    st.sidebar.markdown("Offers innovative nap pods that enhance productivity and well-being.")
    pg.run()
    
    
