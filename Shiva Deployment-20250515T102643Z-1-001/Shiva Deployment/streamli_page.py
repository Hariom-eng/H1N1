import streamlit as st

# Title of the app
st.title("H1N1 Prediction")

# Text inputs for h1n1_concern and h1n1_knowledge
h1n1_worry = st.selectbox(f"Select for H1N1 Worry : ", ['Select','0', '1', '2','3'])
h1n1_awareness = st.selectbox(f"Select for H1N1 Awareness : ", ['Select','0', '1', '2'])


checkbox_values = {} 
label_01 = ["antiviral_medication","contact_avoidance","bought_face_mask",
          "wash_hands_frequently","avoid_large_gatherings",
          "reduced_outside_home_cont","avoid_touch_face","dr_recc_h1n_vacc",
          "dr_recc_seasonal_vacc","chronic_medic_condition","cont_child_undr_6_mnths",
          "is_health_worker","has_health_insur"]
# Loop to create checkboxes and store values in dictionary
for label1 in label_01:
    checkbox_values[label1] = 1 if st.checkbox(f"{label1}") else 0

# Initialize a list for text inputs for other behavioral factors
inputsvar = []
label_val = ["is_h1n1_vacc_effective", "is_h1n1_risk", "sick_from_h1n1_vacc",
          "is_seas_vacc_effective", "is_seas_risk", "sick_from_seas_vacc"]
# Loop to create text inputs and store their values in list
for label2 in label_val:
    user_input = st.selectbox(f"Select for {label2} : ", ['Select','2', '3', '4','5'])
    inputsvar.append(user_input)

age_group = st.selectbox(f"Select the Age_group : ", ['Select','18 - 34 Years','35 - 44 Years','45 - 54 Years','55 - 64 Years', '65+ Years'])

qualification = st.selectbox(f"Select the Qualification : ", ['Select','< 12th Standard','12th Standard','Some College','College Graduate'])

race = st.selectbox(f"Select the Race : ", ['Select','White','Black','Hispanic','Other or Multiple'])

sex = st.selectbox(f"Select Sex : ", ['Select','Male','Female'])

income_level = st.selectbox(f"Select Income Level : ", ['Select','Below Poverty', '<= $75,000, Above Poverty', '> $75,000'])

marital_status = st.selectbox(f"Select Marital Status : ", ['Select','Married','Not Married'])

employment = st.selectbox(f"Select Employement Status : ", ['Select','Employed','Not in Labor Force'])

census_msa = st.selectbox(f"Select Census MSA : ", ['Select','Non-MSA','MSA, Not Principle  City'])

no_of_adults = st.selectbox(f"Select No of Adults : ", ['Select','0','1','2'])

no_of_children = st.selectbox(f"Select No of Children : ", ['Select','0','1','2','3'])



# Display the captured input data (
# this step is for debugging purposes)
# st.write("Checkbox Values:")
# st.write(checkbox_values)

# st.write("Text Input Values:")
# for i, value in enumerate(inputsvar, 1):
#     st.write(f"Input {i}: {value}")
