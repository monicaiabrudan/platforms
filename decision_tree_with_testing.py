import streamlit as st
import pandas as pd
# === Automated Testing Function ===
def simulate_decision_path(tree, labels, start_node, answers):
    current = start_node
    for ans in answers:
        children = tree.get(current)
        if not children:
            return labels.get(current, "Unknown")
        current = children[0] if ans == "Yes" else children[1]
    return labels.get(current, "Unknown")
# ==================================

st.set_page_config(page_title="Decision Tree Assistant", layout="centered")
st.title("🧠 Interactive Decision Tree")

# Tree structure
tree = {}
labels = {}

tree["JK4KtthaC9JlMCbLSFZd-7"] = ['JK4KtthaC9JlMCbLSFZd-11', 'tGIDDYov4WynkGOIi6uA-68']
tree["JK4KtthaC9JlMCbLSFZd-11"] = ['JK4KtthaC9JlMCbLSFZd-14', 'tGIDDYov4WynkGOIi6uA-65']
tree["JK4KtthaC9JlMCbLSFZd-14"] = ['JK4KtthaC9JlMCbLSFZd-17', 'JK4KtthaC9JlMCbLSFZd-20']
tree["JK4KtthaC9JlMCbLSFZd-17"] = ['tGIDDYov4WynkGOIi6uA-1', 'tGIDDYov4WynkGOIi6uA-20']
tree["JK4KtthaC9JlMCbLSFZd-20"] = ['JK4KtthaC9JlMCbLSFZd-17', 'tGIDDYov4WynkGOIi6uA-117']
tree["tGIDDYov4WynkGOIi6uA-1"] = ['tGIDDYov4WynkGOIi6uA-4', 'tGIDDYov4WynkGOIi6uA-20']
tree["tGIDDYov4WynkGOIi6uA-4"] = ['tGIDDYov4WynkGOIi6uA-12', 'tGIDDYov4WynkGOIi6uA-20']
tree["tGIDDYov4WynkGOIi6uA-20"] = ['tGIDDYov4WynkGOIi6uA-27', 'tGIDDYov4WynkGOIi6uA-122']
tree["tGIDDYov4WynkGOIi6uA-27"] = ['tGIDDYov4WynkGOIi6uA-32', 'tGIDDYov4WynkGOIi6uA-51']
tree["tGIDDYov4WynkGOIi6uA-32"] = ['tGIDDYov4WynkGOIi6uA-39', 'tGIDDYov4WynkGOIi6uA-42']
tree["tGIDDYov4WynkGOIi6uA-42"] = ['tGIDDYov4WynkGOIi6uA-45', 'tGIDDYov4WynkGOIi6uA-48']
tree["tGIDDYov4WynkGOIi6uA-51"] = ['tGIDDYov4WynkGOIi6uA-63', 'tGIDDYov4WynkGOIi6uA-57']
tree["tGIDDYov4WynkGOIi6uA-65"] = ['tGIDDYov4WynkGOIi6uA-74', 'tGIDDYov4WynkGOIi6uA-113']
tree["tGIDDYov4WynkGOIi6uA-74"] = ['tGIDDYov4WynkGOIi6uA-77', 'tGIDDYov4WynkGOIi6uA-99']
tree["tGIDDYov4WynkGOIi6uA-77"] = ['tGIDDYov4WynkGOIi6uA-85', 'tGIDDYov4WynkGOIi6uA-82']
tree["tGIDDYov4WynkGOIi6uA-85"] = ['tGIDDYov4WynkGOIi6uA-87', 'tGIDDYov4WynkGOIi6uA-90']
tree["tGIDDYov4WynkGOIi6uA-90"] = ['tGIDDYov4WynkGOIi6uA-93', 'tGIDDYov4WynkGOIi6uA-96']
tree["tGIDDYov4WynkGOIi6uA-99"] = ['tGIDDYov4WynkGOIi6uA-77', 'tGIDDYov4WynkGOIi6uA-102']
labels["JK4KtthaC9JlMCbLSFZd-13"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-70"] = "NO"
labels["JK4KtthaC9JlMCbLSFZd-7"] = "Is a computer mandatory?"
labels["JK4KtthaC9JlMCbLSFZd-16"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-67"] = "NO"
labels["JK4KtthaC9JlMCbLSFZd-11"] = "Do you need software installed for the course?"
labels["JK4KtthaC9JlMCbLSFZd-19"] = "YES"
labels["JK4KtthaC9JlMCbLSFZd-14"] = "Is the software free to use?"
labels["tGIDDYov4WynkGOIi6uA-21"] = "NO"
labels["JK4KtthaC9JlMCbLSFZd-17"] = "Is the software cross platform?"
labels["tGIDDYov4WynkGOIi6uA-119"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-121"] = "YES"
labels["JK4KtthaC9JlMCbLSFZd-20"] = "Do you have a licence to run the software for the number of participants and instructors expected in the course?"
labels["JK4KtthaC9JlMCbLSFZd-22"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-18"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-19"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-126"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-1"] = "Can participants bring their own computers"
labels["tGIDDYov4WynkGOIi6uA-10"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-31"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-4"] = "Can the software run on participants own computers"
labels["tGIDDYov4WynkGOIi6uA-12"] = "Provide participants with instructions on how to install the software"
labels["tGIDDYov4WynkGOIi6uA-29"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-124"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-20"] = "Can you provide access to computers (as in a computer lab),  with a minimum specification of: 8GB RAM,i5 or equivalent processor, 100GB of disk space?"
labels["tGIDDYov4WynkGOIi6uA-36"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-53"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-27"] = "Is the software only running on Windows?"
labels["tGIDDYov4WynkGOIi6uA-41"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-44"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-32"] = "Do the computers in the lab have a Windows licence?"
labels["tGIDDYov4WynkGOIi6uA-39"] = "Install the software on the Windows machines in the lab"
labels["tGIDDYov4WynkGOIi6uA-47"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-50"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-42"] = "Do you have a Windows licence?"
labels["tGIDDYov4WynkGOIi6uA-45"] = "Deploy a VM with a Windows OS and install the software on it."
labels["tGIDDYov4WynkGOIi6uA-48"] = "Use the cloud. Create Windows instances in the cloud, install the required software on it and share with the instructors and the participants"
labels["tGIDDYov4WynkGOIi6uA-59"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-64"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-51"] = "Do the computers in the lab run Linux"
labels["tGIDDYov4WynkGOIi6uA-57"] = "Create a VM with Linux. Install the software. Run the VM on the computer labs."
labels["tGIDDYov4WynkGOIi6uA-63"] = "Install the software on the  machines in the lab"
labels["tGIDDYov4WynkGOIi6uA-76"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-115"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-65"] = "Can all your software needs be met by existing webservers that have a graphical user interface?"
labels["tGIDDYov4WynkGOIi6uA-68"] = "Discussion-BasedCourse"
labels["tGIDDYov4WynkGOIi6uA-81"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-101"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-74"] = "Are these existing webservers open or publicly accessible?"
labels["tGIDDYov4WynkGOIi6uA-86"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-116"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-77"] = "Must participants code and execute on data accessed in the cloud?"
labels["tGIDDYov4WynkGOIi6uA-82"] = "Use the webservers"
labels["tGIDDYov4WynkGOIi6uA-89"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-92"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-85"] = "Can you make it work on Colab or other cloud systems?"
labels["tGIDDYov4WynkGOIi6uA-87"] = "Google ColabN.B: It requires access to course data via a command-line accessible internet source."
labels["tGIDDYov4WynkGOIi6uA-95"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-98"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-90"] = "Can you provide access to computers (as in a computer lab),  with a minimum specification of: 8GB RAM,i5 or equivalent processor, 100GB of disk space?"
labels["tGIDDYov4WynkGOIi6uA-93"] = "Create and deply a VM with Linux. Access the webservers from the VM"
labels["tGIDDYov4WynkGOIi6uA-96"] = "Consider retracing steps or re-planning your course design."
labels["tGIDDYov4WynkGOIi6uA-106"] = "YES"
labels["tGIDDYov4WynkGOIi6uA-112"] = "NO"
labels["tGIDDYov4WynkGOIi6uA-99"] = "Can you ensure access to the private webservers for all participants?"
labels["tGIDDYov4WynkGOIi6uA-102"] = "Consider retracing steps or re-planning your course design."
labels["tGIDDYov4WynkGOIi6uA-113"] = "Consider retracing steps or re-planning your course design."
labels["tGIDDYov4WynkGOIi6uA-117"] = "Reconsider your course design. You cannot create a training on a software which you do not have access to."
labels["tGIDDYov4WynkGOIi6uA-122"] = "Use the cloud. Create Linux or Windows instances in the cloud, install the required software on it and share with the instructors and the participants"

# Initialize session state
if "current_node" not in st.session_state:
    st.session_state.current_node = "JK4KtthaC9JlMCbLSFZd-7"
if "history" not in st.session_state:
    st.session_state.history = []
if "answers" not in st.session_state:
    st.session_state.answers = []

node_id = st.session_state.current_node
children = tree.get(node_id, [])

# Display decision path with answers
st.markdown("### 👣 Decision Path")
for i in range(len(st.session_state.history)):
    q_id = st.session_state.history[i]
    ans = st.session_state.answers[i]
    st.markdown("**{}. {} → _{}_**".format(i + 1, labels.get(q_id, "[Unknown]"), ans))

st.markdown("---")
st.markdown("### **Current Question:**")
st.write("#### {}".format(labels.get(node_id, "Unknown Question")))

if children:
    answer = st.radio("Your answer:", ["Yes", "No"], key=node_id)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Next"):
            st.session_state.history.append(node_id)
            st.session_state.answers.append(answer)
            if answer == "Yes":
                st.session_state.current_node = children[0]
            elif len(children) > 1:
                st.session_state.current_node = children[1]
            else:
                st.session_state.current_node = children[0]
            st.rerun()
    with col2:
        if st.button("Back") and st.session_state.history:
            st.session_state.current_node = st.session_state.history.pop()
            st.session_state.answers.pop()
            st.rerun()
else:
    st.success("✅ Final Decision: {}".format(labels.get(node_id)))
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

    if st.button("Restart"):
        st.session_state.current_node = "JK4KtthaC9JlMCbLSFZd-7"
        st.session_state.history = []
        st.session_state.answers = []
        st.rerun()