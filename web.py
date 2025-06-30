# uber_clone_app.py

import streamlit as st
from geopy.geocoders import Nominatim
import openrouteservice
from openrouteservice import convert
import folium
from streamlit_folium import folium_static
import random

# Initialize geocoder and ORS client
geolocator = Nominatim(user_agent="uber_clone_app")
client = openrouteservice.Client(key='5b3ce3597851110001cf62489a11fb47f8e040ce851c66a0a0da975a')  # Replace with your API key

# Streamlit UI
st.title("🚗 Uber-like Ride Planner")

pickup = st.text_input("📍 Enter Pickup Address")
drop = st.text_input("📍 Enter Destination Address")

if st.button("Show Route"):
    if pickup and drop:
        try:
            # Geocode
            pickup_loc = geolocator.geocode(pickup)
            drop_loc = geolocator.geocode(drop)

            if not pickup_loc or not drop_loc:
                st.error("Couldn't locate one of the addresses.")
            else:
                coords = ((pickup_loc.longitude, pickup_loc.latitude),
                          (drop_loc.longitude, drop_loc.latitude))

                # Route
                route = client.directions(coords)
                geometry = route['routes'][0]['geometry']
                decoded = convert.decode_polyline(geometry)

                distance = route['routes'][0]['summary']['distance'] / 1000  # in km
                duration = route['routes'][0]['summary']['duration'] / 60    # in mins

                # Traffic Simulation
                traffic_level = random.choice(["Light", "Moderate", "Heavy"])

                # Map
                m = folium.Map(location=[pickup_loc.latitude, pickup_loc.longitude], zoom_start=13)
                folium.Marker([pickup_loc.latitude, pickup_loc.longitude], tooltip='Pickup', icon=folium.Icon(color='green')).add_to(m)
                folium.Marker([drop_loc.latitude, drop_loc.longitude], tooltip='Dropoff', icon=folium.Icon(color='red')).add_to(m)
                folium.PolyLine(locations=[(coord[1], coord[0]) for coord in decoded['coordinates']],
                                tooltip='Route', color='blue').add_to(m)

                # Output
                st.subheader("🗺 Route Summary")
                st.write(f"**Distance:** {distance:.2f} km")
                st.write(f"**Estimated Time:** {duration:.1f} minutes")
                st.write(f"**Traffic Level:** {traffic_level}")

                st.subheader("📌 Route on Map")
                folium_static(m)

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter both pickup and destination addresses.")
