
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

pet_path = st.text_input("Choose a PET nrrd file")
mask_path = st.text_input("Choose a MASk nrrd file")

if pet_path and mask_path is not None:
    nii_data = read_image(pet_path)
    roi_mask_data = read_image(mask_path)
    roi_data = roi(nii_data, roi_mask_data)
    st.write('SUVmean:', calculate_mean_suv(roi_data))
