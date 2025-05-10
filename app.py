import streamlit as st

# Title
st.title("🧭 SkillConnectance - AI-Powered Learning Path")

# Input: skills from user
skills_input = st.text_input("Enter skills you'd like to learn (comma-separated):", "Python, Soft Skills")

# Processing
desired_skills = [skill.strip().lower() for skill in skills_input.split(",")]

# Mock learning path generator
def generate_learning_path(skill):
    return [
        f"1. Introduction to {skill.title()}",
        f"2. Foundational Concepts in {skill.title()}",
        f"3. Practice Projects in {skill.title()}",
        f"4. Intermediate to Advanced Applications",
        f"5. Join a community or mentorship program",
        f"6. Apply {skill.title()} in real-world case studies",
    ]

# Output: Learning Paths
st.subheader("📘 Suggested Learning Paths")

if desired_skills:
    for skill in desired_skills:
        st.markdown(f"### {skill.title()}")
        for step in generate_learning_path(skill):
            st.markdown(f"- {step}")
        st.markdown("---")
else:
    st.info("Please enter at least one skill to see a learning path.")
