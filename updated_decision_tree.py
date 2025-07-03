import streamlit as st
import pandas as pd

st.set_page_config(page_title="Decision Tree Assistant", layout="centered")
st.title("🧠 Interactive Decision Tree")

# Tree structure
tree = {
    "node_022": ['node_018', 'node_013'],
    "node_018": ['node_026', 'node_003'],
    "node_026": ['node_025', 'node_017'],
    "node_025": ['node_009', 'node_004'],
    "node_017": ['node_025', 'leaf_no'],
    "node_004": ['node_005', 'node_009'],
    "node_005": ['node_029', 'node_023'],
    "node_009": ['node_027', 'node_033'],
    "node_027": ['node_014', 'node_015'],
    "node_014": ['node_020', 'node_016'],
    "node_016": ['node_012', 'node_034'],
    "node_015": ['node_000', 'node_021'],
    "node_003": ['node_001', 'node_030'],
    "node_001": ['node_028', 'node_007'],
    "node_028": ['node_008', 'leaf_no'],
    "node_008": ['node_019', 'node_033'],
    "node_007": ['node_028', 'node_010'],
    "node_000": ['node_024', 'node_035'],
    "node_024": ['node_002', 'node_035'],
    "node_002": ['node_035', 'node_011'],
    "node_035": ['node_011', 'node_032'],
    "node_006": ['node_031', 'node_025'],
    "node_012": ['node_012', 'leaf_no'],
    "node_023": ['node_033', 'node_009'],
    "leaf_yes": [],
    "leaf_no": [],
}

labels = {
    "node_000": """Are there issues with conflicting dependencies or complex setups?""",
    "node_001": """Are these existing webservers open or publicly accessible?""",
    "node_002": """Are you working with large datasets which you can mount as external volumes and can you provide enough compute resources on the host machine?""",
    "node_003": """Can all your software needs be met by existing webservers that have a graphical user interface?""",
    "node_004": """Can participants bring their own computers?""",
    "node_005": """Can the software run on participants own computers?""",
    "node_006": """Can you contact the vendor to arrange training licenses for the duration of the course?""",
    "node_007": """Can you ensure access to the private webservers for all participants?""",
    "node_008": """Can you make it work on Colab or other cloud systems, if Google services are not available?""",
    "node_009": """Can you provide access to computers (as in a computer lab), with a minimum specification of: 8GB RAM, Intel i5 or equivalent processor, 100GB of disk space?""",
    "node_010": """Consider retracing steps or re-planning your course design.""",
    "node_011": """Create a VM with Linux. Install the software. Run the VM on the computer labs.""",
    "node_012": """Deploy a VM with a Windows OS and install the software on it.""",
    "node_013": """Discussion-Based Course""",
    "node_014": """Do the computers in the lab have a Windows licence?""",
    "node_015": """Do the computers in the lab run Linux?""",
    "node_016": """Do you have a Windows licence?""",
    "node_017": """Do you have a licence to run the software for the number of participants and instructors expected in the course?""",
    "node_018": """Do you need software installed for the course?""",
    "node_019": """Google Colab or other cloud systems N.B: It requires access to course data via a command-line accessible internet source.""",
    "node_020": """Install the software on the Windows machines in the lab""",
    "node_021": """Install the software on the machines in the lab""",
    "node_022": """Is a computer mandatory?""",
    "node_023": """Is the course online of hybrid?""",
    "node_024": """Is the course teaching workflow reproducibility, or pipeline development, such as Snakemake or Nextflow?""",
    "node_025": """Is the software cross platform?""",
    "node_026": """Is the software free to use?""",
    "node_027": """Is the software only running on Windows?""",
    "node_028": """Must participants code and execute on data accessed in the cloud?""",
    "node_029": """Provide participants with instructions on how to install the software""",
    "node_030": """Reconsider your course design.""",
    "node_031": """Reconsider your course design. You cannot create a training on a software which you do not have access to.""",
    "node_032": """Use Docker for the software environment and host the data on the local disk, or shared NFS volumes, or object storage such as S3""",
    "node_033": """Use the cloud. Create Linux or Windows instances in the cloud, install the required software on it and share with the instructors and the participants""",
    "node_034": """Use the cloud. Create Windows instances in the cloud, install the required software on it and share with the instructors and the participants""",
    "node_035": """Will all the computer have access to internet during the course?""",
    "leaf_yes": """YES""",
    "leaf_no": """NO""",
}

if "current_node" not in st.session_state:
    st.session_state.current_node = "node_022"
    st.session_state.history = []
    st.session_state.answers = []

node_id = st.session_state.current_node
children = tree.get(node_id, [])

if children:
    st.markdown(f"### {labels.get(node_id, '[Unknown]')}")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Yes"):
            st.session_state.history.append(node_id)
            st.session_state.answers.append("Yes")
            st.session_state.current_node = children[0]
            st.rerun()
    with col2:
        if st.button("❌ No"):
            st.session_state.history.append(node_id)
            st.session_state.answers.append("No")
            st.session_state.current_node = children[1]
            st.rerun()
    if st.button("⬅️ Back") and st.session_state.history:
        st.session_state.current_node = st.session_state.history.pop()
        st.session_state.answers.pop()
        st.rerun()
else:
    label = labels.get(node_id, "[Unknown]")
    if label.startswith(('Create', 'Install', 'Use', 'Run', 'Deploy', 'Provide', 'Reconsider', 'Consider', 'Google', 'Discussion-Based')):
        st.success("✅ " + label)
    else:
        st.info("Final Decision: " + label)

    st.markdown("### ✅ Full Decision Path")
    full_path = st.session_state.history + [node_id]
    full_answers = st.session_state.answers + ["[End]"]
    for i in range(len(full_path)):
        st.markdown("**{}. {} → _{}_**".format(i + 1, labels.get(full_path[i], "[Unknown]"), full_answers[i]))

    df = pd.DataFrame({
        "Step": list(range(1, len(full_path) + 1)),
        "Question": [labels.get(nid, "[Unknown]") for nid in full_path],
        "Answer": full_answers
    })

    st.download_button("📄 Download Decision Summary", data=df.to_csv(index=False).encode(),
                       file_name="decision_summary.csv")

    if st.button("🔄 Restart"):
        st.session_state.current_node = "node_022"
        st.session_state.history = []
        st.session_state.answers = []
        st.rerun()
