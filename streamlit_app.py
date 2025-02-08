import streamlit as st
import random

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
            "resource1": Resource("resource1", "Calm Breathing Exercise", "A guided breathing exercise...", "Coping Strategies", "calm_breathing"),
            "resource2": Resource("resource2", "National Suicide Prevention Lifeline", "Call or text 988", "Hotlines")
        }

    def add_resource(self, name, description, category, link=None):
        resource_id = str(uuid.uuid4())
        new_resource = Resource(resource_id, name, description, category, link)
        self.resources[resource_id] = new_resource

    def get_resources_by_category(self, category):
        return [resource for resource in self.resources.values() if resource.category == category]

    def find_resource_by_id(self, resource_id):
        return self.resources.get(resource_id)

# Define Resource class
class Resource:
    def __init__(self, resource_id, name, description, category, link=None):
        self.resource_id = resource_id
        self.name = name
        self.description = description
        self.category = category
        self.link = link

# Define the UI class
class PanicPal:
    def __init__(self, support_service):
        self.support_service = support_service
        self.chat_history = []

    def run(self):
        st.title("PanicPal - Anxiety Support App")
        
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
        categories = ["Coping Strategies", "Hotlines"]
        for category in categories:
            resources = self.support_service.get_resources_by_category(category)
            st.write(f"### {category}")
            for resource in resources:
                if resource.link:
                    if resource.link == "calm_breathing":
                        st.write(f"- [{resource.name}](/?page=calm_breathing): {resource.description}")
                    else:
                        st.write(f"- [{resource.name}]({resource.link}): {resource.description}")
                else:
                    st.write(f"- {resource.name}: {resource.description}")

        # Handle resource pages
        page = st.query_params.get("page", [None])[0]
        if page == "calm_breathing":
            self.show_calm_breathing_page()

    def show_calm_breathing_page(self):
        st.title("Calm Breathing Exercise")
        st.write("""
        ### Diaphragmatic Breathing
        Place one hand on your chest and the other on your abdomen. Inhale slowly through your nose, feeling your abdomen rise. Exhale slowly through your mouth, allowing your abdomen to fall. This technique promotes relaxation and helps counteract hyperventilation.

        ### Box Breathing
        Visualize a square and follow this pattern: Inhale for 4 counts, hold for 4 counts, exhale for 4 counts, and hold for 4 counts. Repeat several times. This structured technique can bring immediate relief during a panic attack.

        ### 4-7-8 Breathing
        Inhale silently through your nose for 4 counts, hold your breath for 7 counts, then exhale completely through your mouth for 8 counts, making a whooshing sound. Repeat at least four times.

        ### Alternate Nostril Breathing
        Use your right thumb to block your right nostril, inhale through the left nostril, then block the left nostril with your ring finger and exhale through the right nostril. Alternate nostrils with each breath cycle.

        ### 4-4-4 Breathing (Box Breathing)
        Take a breath, exhale for 4 counts, hold for 4 counts, inhale for 4 counts, and hold again for 4 counts. This technique can help keep a raised heart rate down and distract you from anxiety-inducing situations.

        ### Long Exhaling
        Inhale for 2-3 seconds, pause briefly, then exhale gently for 4-6 seconds (double the inhale time). Continue for at least 5 minutes. This technique can help combat the fight-or-flight stress response.
        """)

if __name__ == "__main__":
    support_app = SupportService()

    ui = PanicPal(support_app)
    ui.run()
