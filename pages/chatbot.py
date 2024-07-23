import streamlit as st
from chatbots.agent import agent
from chatbots.finsage import finsage
from chatbots.careersage import careersage
from chatbots.scholarsage import scholarsage
from streamlit_option_menu import option_menu

def chatbot():
    
    styles = {
        "container": {"background-color": "#007d40", "border-radius": "10px", "--hover-color": "#007d40"},
        "icon": {"color": "black"},
        "nav-link": {"color": "black", "backgroung-color": "#007d40", "--hover-color": "#007d40", "border-radius": "5px"},
        "nav-link-selected": {"color": "black", "backgroung-color": "#007d40", "border-radius": "5px"},
        "active": {"color": "black" ,"background-color": "#007d40", "--hover-color": "#007"},
        "position": "fixed",
    }
 
    menu_dict = {
        "Engineering and Physics" : {"fn": agent},
        "Computing and Mathematics" : {"fn": finsage},
        "Petroleum Engineering & Geosciences" : {"fn": careersage},
        "Chemicals and Materials" : {"fn": scholarsage}
    }

    selected = option_menu(None, 
        ["Engineering and Physics", "Computing and Mathematics", "Petroleum Engineering & Geosciences", "Chemicals and Materials"], 
        icons=["gear-fill", "pc-display-horizontal", "fuel-pump-fill", "paint-bucket"],
        default_index=0,
        styles = styles,
        orientation="horizontal")
    if selected in menu_dict.keys():
        menu_dict[selected]["fn"]()
    