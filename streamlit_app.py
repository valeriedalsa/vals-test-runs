import streamlit as st
import random
import uuid
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Coping Mechanisms List (for panic attacks)
COPING_MECHANISMS = [
    "Breathe in for 4 counts, hold for 4 counts, and breathe out for 4 counts.",
    "Try to ground yourself by naming 5 things you can see, 4 things you can feel, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
    "Focus on your breathing. Inhale for a count of 4, hold for 7, exhale for 8.",
    "Clench your fists tightly for a few seconds, then slowly release them to relieve tension.",
    "Try visualizing a calming scene, like a beach or forest, and focus on the details of it.",
    "Recite a calming affirmation: 'This will pass, I am safe, and I can handle this.'"
]

# Function to select a random coping mechanism
def get_random_coping_mechanism():
    return random.choice(COPING_MECHANISMS)

# SupportService Class (simplified for this example)
class SupportService:
    def __init__(self):
        self.resources = {
            "resource1": Resource("resource2", "National Suicide Prevention Lifeline", "Call or text 988", "Hotlines")
        }

    def add_resource(self, name, description, category):
        resource_id = str(uuid.uuid4())
        new_resource = Resource(resource_id, name, description, category)
        self.resources[resource_id] = new_resource

    def get_resources_by_category(self, category):
        return [resource for resource in self.resources.values() if resource.category == category]

    def find_resource_by_id(self, resource_id):
        return self.resources.get(resource_id)

# Define Resource class
class Resource:
    def __init__(self, resource_id, name, description, category):
        self.resource_id = resource_id
        self.name = name
        self.description = description
        self.category = category

# Define the UI class
class PanicPal:
    def __init__(self, support_service):
        self.support_service = support_service
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

    def run(self):
        st.title("PanicPal - Anxiety Support App")
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Chat Box")
            for message in st.session_state["messages"]:
                st.chat_message(message["role"], message["content"])

            user_input = st.chat_input("Enter your message:")
            if user_input:
                st.session_state["messages"].append({"role": "user", "content": user_input})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state["messages"]
                )
                st.session_state["messages"].append({"role": "assistant", "content": response.choices[0].message["content"]})

        with col2:
            st.subheader("Random Coping Mechanism Generator")
            if st.button("Get a Random Coping Mechanism"):
                st.write(get_random_coping_mechanism())

        st.subheader("Available Resources")
        categories = ["Hotlines"]
        for category in categories:
            resources = self.support_service.get_resources_by_category(category)
            st.write(f"### {category}")
            for resource in resources:
                st.write(f"- {resource.name}: {resource.description}")

if __name__ == "__main__":
    support_app = SupportService()

    ui = PanicPal(support_app)
    ui.run()
