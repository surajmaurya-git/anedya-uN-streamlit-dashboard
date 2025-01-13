import streamlit as st
from components.ui.unit_ui_components import unit_header
from components.ui.unit_ui_components import unit_details
from components.ui.unit_ui_components import cards_section
from components.ui.unit_ui_components import gauge_section
from components.ui.unit_ui_components import controllers_section
from components.ui.unit_ui_components import graph_section
from components.ui.unit_ui_components import map_section
from cloud.anedya_cloud import Anedya

import json

UNIT_NUMBER = 5


def draw_unit_1_dashboard():
    NUMBER_OF_NODES= len(st.session_state.nodesId)
    if NUMBER_OF_NODES< UNIT_NUMBER:
        st.error("Node ID not found")
        st.stop()

    anedya = Anedya()
    NODE_ID = st.session_state.nodesId[f"node_{UNIT_NUMBER}"]
    VARIABLES = st.session_state.variablesIdentifier

    node = None
    node = anedya.new_node(st.session_state.anedya_client, nodeId=NODE_ID)
    device_status_res = node.get_deviceStatus()
    unit_header(
        f"POD {UNIT_NUMBER}",
        node_client=node,
        device_status_res=device_status_res,
    )


    vitals_value = {
        "booking": None,
        "timeLeft": None,
        "endEpoch": None,
        "napTime": None,
        "macId": "ND",
        "firmware": "ND",
        "wifiSignal": None,
        "rfidGain": None,
        "rfid": "ND",
        "can": None,
        "seatSensor": [None, None],
    }
    res = node.get_valueStore("vitals")
    if res.get("isSuccess"):
        value=res.get("value")
        vitals_value = json.loads(value)
        # st.write(vitals_value)
    unit_details(vitals_value)
    cards_section(vitals_value)

    # gauge_data_list=[0,0,0,0,0]
    # gauge_section(gauge_data_list)

    controllers_section(node)

    # graph_section(node)
    map_section(node)


draw_unit_1_dashboard()
