import streamlit as st
import leafmap.foliumap as leafmap
import random


def app():
    st.title("Countries")

    m = leafmap.Map(center=[0, 0], zoom=2)

    url = "https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/countries.geojson"

    def random_color(feature):
        return {
            "color": "black",
            "fillColor": random.choice(["red", "yellow", "green", "orange"]),
        }

    m.add_geojson(url, layer_name="Countries", style_callback=random_color)

    m.to_streamlit(height=700)
