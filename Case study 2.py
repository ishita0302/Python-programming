'''1.	Cate Hospital wants to know the medical specialty visited by the maximum number of patients. Assume that the Patient id of the patient along with the medical specialty visited by the patient is stored in a list. The details of the medical specialties are stored in a dictionary as follows:
{
“P”:”Pediatrics”,
“O”:”Orthopedics”,
“E”:”ENT”
}
Write a function to find the medical specialty visited by the maximum number of patients and return the name of the specialty.'''
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
 
    p=o=e=0 
    for i in range(1,len(patient_medical_speciality_list),2):
        if patient_medical_speciality_list[i]=='P':
            p=p+1 
        elif patient_medical_speciality_list[i]=='O':
            o=o+1 
        elif patient_medical_speciality_list[i]=='E':
            e=e+1 
    if p>e and p>o:
        max=p 
    elif e>p and e>o:
        max=e 
    else:
        max=o 
    if max==p:
        speciality="Pediatrics"
    elif max==e:
        speciality="ENT"
    else:
        speciality="Orthopedics"

    return speciality

patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
