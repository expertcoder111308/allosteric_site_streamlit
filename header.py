import streamlit as st

def create_header():
  st.title("Discovery of Allosteric Sites using Ensemble Classifiers")
  st.header("By: Sriram Susarla")
  st.subheader("Enter in protein pocket descriptors found from FPocket and click classify when ready!")

def get_user_input():
  score = st.number_input("Score:")
  druggability_score = st.number_input("Druggability Score:")
  number_alpha_spheres = st.number_input("Number of Alpha Spheres:")
  total_sasa = st.number_input("Total SASA:")
  polar_sasa = st.number_input("Polar SASA:")
  apolar_sasa = st.number_input("Apolar SASA:")
  volume = st.number_input("Volume:")
  local_hydrophobic_density = st.number_input("Mean local hydrophobic density:")
  alpha_sphere_radius = st.number_input("Mean alpha sphere radius:")
  alpha_sphere_solvent_access = st.number_input("Mean alpha sphere solvent access:")
  apolar_alpha_sphere_proportion = st.number_input("Apolar alpha sphere proportion:")
  hydrophobicity_score = st.number_input("Hydrophobicity score:")
  volume_score = st.number_input("Volume score:")
  polarity_score = st.number_input("Polarity score:")
  charge_score = st.number_input("Charge score:")
  proportion_polar_atoms = st.number_input("Proportion of polar atoms:")
  alpha_sphere_density = st.number_input("Alpha sphere density:")
  CoM_Sphere_Max_Dist = st.number_input("Center of mass - Alpha Sphere max distance:")
  flexibility = st.number_input("Flexibility:")


  input_features = [[score, druggability_score, number_alpha_spheres, total_sasa, polar_sasa, apolar_sasa, volume, local_hydrophobic_density, alpha_sphere_radius, alpha_sphere_solvent_access, apolar_alpha_sphere_proportion, hydrophobicity_score, volume_score, polarity_score, charge_score, proportion_polar_atoms, alpha_sphere_density, CoM_Sphere_Max_Dist, flexibility]]
  return input_features
