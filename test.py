
import numpy as np
import nrrd



def read_image(path):
    img, options = nrrd.read(path)
    return img


def roi(image_data, mask_data):
    data = image_data[mask_data > 0]
    return data


def calculate_mean_suv(data):
    mean_suv = np.mean(data)
    return mean_suv


import streamlit as st
import pandas as pd

uploaded_pet = st.file_uploader("Choose a PET nrrd file")
uploaded_mask = st.file_uploader("Choose a MASk nrrd file")

if uploaded_pet and uploaded_mask is not None:
    nii_data = read_image(uploaded_pet)
    roi_mask_data = read_image(uploaded_mask)
    roi_data = roi(nii_data, roi_mask_data)
    st.write('SUVmean:', calculate_mean_suv(roi_data))
