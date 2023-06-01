
#hospital
def expert_system(symptoms,symptom1,symptom2):
    diagnosis = None
    treatment = None

    if symptoms == 'fever' and symptom1 == 'cough' and symptom2 == 'headache':
        diagnosis = 'Migraine'
        treatment = 'Ibuprofen'
        hospitals='Recommended Hospitals:\n 1. Life Care \n Facilaties: \n1. X-ray 2. Blood Test . cash payment\n2. Apollo  Hospital:\n.Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment, hospitals

    elif symptoms == 'cough' and symptom1 == 'headache' and symptom2 == 'fever':
        diagnosis = 'Flu'
        treatment = 'Acetaminophen'
        hospitals='Recommended Hospitals:\n 1. Life Care \n Facilaties: \n1. X-ray 2. Blood Test . cash payment\n2. Apollo  Hospital:\n.Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals

    elif symptoms == 'chest_pain' and symptom1 == 'fever' and symptom2 == 'shortness_of_breadth':
        diagnosis = 'pneumonia'
        treatment = 'Antibiotics and rest'
        hospitals = 'Recommended Hospitals:\n 1. Ashoka \n Facilaties: \n1. X-ray 2. Blood Test . cash payment\n2. wokart  Hospital:\n.Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals

    elif symptoms == 'shortness_of_breadth' and symptom1 == 'cough' and symptom2 == 'blue_lips':
        diagnosis = 'Asthma'
        treatment = 'Bronchodilators and inhaled corticosteroids'
        hospitals = 'Recommended Hospitals:\n 1. Six sigma \n Facilaties: \n1. X-ray 2. Blood Test . cash payment\n2. magna  Hospital:\n.Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals

    elif symptoms == 'nausia' and symptom1 == 'fever' and symptom2 == 'pains':
        diagnosis = 'Dengue'
        treatment = 'Acetaminophen and Rest'
        hospitals = 'Recommended Hospitals:\n 1. Shatabdi \n Facilaties: \n1. X-ray 2. Blood Test . cash payment\n2. magna  Hospital:\n.Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals

    elif symptoms == 'frequent_urination'  and symptom1 == 'fatigue':
        diagnosis = 'Diabetes'
        treatment = 'Insulin therapy and blood sugar monitoring'
        hospitals = 'Recommended Hospitals:\n 1. cooper \n Facilaties: \n1. X-ray 2. Blood Test . cash payment\n2. leelavati Hospital:\n.Facilities: 1.Mri 2.CT-Scan online as well as cash'
        return diagnosis, treatment,hospitals
        
    else:
        diagnosis='No diagnosis'
        treatment="No treatment"
    return diagnosis, treatment


symptoms= input("enter the symptoms")
symptom1=input("enter the symptom")
symptom2=input("enter the symptom")


diagnosis, treatment, hospitals = expert_system(symptoms,symptom1,symptom2)


print('Diagnosis:', diagnosis)
print('Treatment:', treatment)
print(hospitals)

