import streamlit as st

st.set_page_config(page_title="Pizza Recipes", page_icon="🍕")

st.title("🍕 Pizza Recipes Explorer")

st.write("Select a pizza and explore its ingredients and preparation steps!")

# Pizza recipes database (can be extended)
recipes = {
    "Margherita": {
        "ingredients": [
            "Pizza dough",
            "Tomato sauce",
            "Fresh mozzarella",
            "Fresh basil leaves",
            "Olive oil",
            "Salt"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread tomato sauce evenly on the pizza base.",
            "Add slices of fresh mozzarella.",
            "Bake for 7–10 minutes until cheese melts.",
            "Garnish with fresh basil and drizzle with olive oil before serving."
        ]
    },
    "Pepperoni": {
        "ingredients": [
            "Pizza dough",
            "Tomato sauce",
            "Mozzarella cheese",
            "Pepperoni slices",
            "Olive oil"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread tomato sauce over the base.",
            "Top with mozzarella cheese and pepperoni slices.",
            "Bake for 8–12 minutes until crust is golden and cheese is bubbly."
        ]
    },
    "Veggie": {
        "ingredients": [
            "Pizza dough",
            "Tomato sauce",
            "Mozzarella cheese",
            "Bell peppers",
            "Mushrooms",
            "Onions",
            "Olives",
            "Spinach"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread tomato sauce on the base.",
            "Add cheese and arrange vegetables evenly.",
            "Bake for 10–12 minutes until crust is crisp.",
            "Optionally drizzle with olive oil before serving."
        ]
    }
}

# User selection
pizza_choice = st.selectbox("Choose a pizza", list(recipes.keys()))

# Show recipe
st.subheader(f"{pizza_choice} Recipe")

st.markdown("**Ingredients:**")
for ingredient in recipes[pizza_choice]["ingredients"]:
    st.write(f"- {ingredient}")

st.markdown("**Preparation Steps:**")
for i, step in enumerate(recipes[pizza_choice]["steps"], start=1):
    st.write(f"{i}. {step}")
