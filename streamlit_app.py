import streamlit as st
import random
import uuid
import os
import base64
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("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")

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

# Function to generate a haiku about AI using OpenAI
def generate_haiku():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "write a haiku about ai"}
        ]
    )
    return response.choices[0].message['content']

# SupportService Class (simplified for this example)
class SupportService:
    def __init__(self):
        self.resources = {
            "resource1": Resource("resource1", "National Suicide Prevention Lifeline", "Call or text 988", "Hotlines")
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
        self.chat_history = []

    def run(self):
        st.title("Panic Pal")
        st.write("Your Personal Anxiety Support App")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Chat Box")
            user_input = st.text_input("What do you need help with today?")
            if st.button("Send"):
                self.chat_history.append(f"You: {user_input}")
                self.chat_history.append(f"Bot: I'm here to help you with your anxiety. How can I assist?")
            for message in self.chat_history:
                st.write(message)

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
