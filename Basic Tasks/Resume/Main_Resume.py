import streamlit as st
from Resume_Data import data

def main():
    # Set page title and header
    st.set_page_config(page_title="Muhammad Harris Rashid's Resume", layout="wide")
    st.title("Muhammad Harris Rashid")
    st.subheader(data["Profile Headline"])

    # Contact Information
    st.header("Contact Information")
    st.write(f"Mobile: {data['Contact']['Mobile']}")
    st.write(f"Email: {data['Contact']['Email']}")
    st.write(f"LinkedIn: {data['Contact']['LinkedIn']}")
    st.write(f"GitHub: {data['Contact']['GitHub']}")

    # Education
    st.header("Education")
    for edu in data["Education"]:
        st.subheader(edu["Institution"])
        st.write(f"Degree: {edu['Degree']}")
        st.write(f"Duration: {edu['Duration']}")
        st.write("")

    # Experience
    st.header("Experience")
    for exp in data["Experience"]:
        st.subheader(exp["Company"])
        st.write(f"Position: {exp['Position']}")
        st.write(f"Duration: {exp['Duration']}")
        st.write(f"Location: {exp['Location']}")
        st.write(f"Description: {exp['Description']}")
        st.write("")

    # Skills (Customized based on LinkedIn data)
    st.header("Skills")
    skills = ["Python", "Biotechnology", "Data Analysis", "Research", "Web Development", "Content Writing", "SEO"]
    for skill in skills:
        st.checkbox(skill)

    # Projects (Customized based on LinkedIn data)
    st.header("Projects")
    project_names = ["YoungDev Interns Project", "CodSoft Project", "SOFTEC Project", "Freelance Projects", "PCSIR Project"]
    for project in project_names:
        st.checkbox(project)

    # Certifications (Customized based on LinkedIn data)
    st.header("Certifications")
    certifications = ["Certification 1", "Certification 2", "Certification 3"]
    for cert in certifications:
        st.checkbox(cert)

    # Awards and Achievements (Customized based on LinkedIn data)
    st.header("Awards and Achievements")
    awards = ["Award 1", "Award 2", "Award 3"]

    
    for award in awards:
        st.checkbox(award)

if __name__ == '__main__':
    main()
