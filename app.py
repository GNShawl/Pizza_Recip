import streamlit as st

st.set_page_config(page_title="Pakistani Pizza Recipes", page_icon="🍕")

st.title("🍕 Pakistani Pizza Recipes Explorer")

st.write("Discover delicious pizza recipes with a Pakistani twist! Choose a pizza below to see ingredients and preparation steps.")

# Dough recipe (common for all pizzas)
dough_recipe = {
    "ingredients": [
        "3 ½ cups all-purpose flour",
        "1 cup warm water",
        "2 tsp instant yeast",
        "1 tsp sugar",
        "1 tsp salt",
        "2 tbsp olive oil"
    ],
    "steps": [
        "In a bowl, mix warm water, sugar, and yeast. Let it rest for 5–10 minutes until foamy.",
        "Add flour, salt, and olive oil. Knead into a smooth dough.",
        "Cover and let it rise for 1–2 hours until doubled in size.",
        "Punch down the dough and roll out for pizza base."
    ]
}

# Pakistani pizza recipes
recipes = {
    "Malai Boti Pizza": {
        "ingredients": [
            "Prepared pizza dough",
            "Malai boti chicken chunks (marinated with cream, yogurt, spices, grilled)",
            "Mozzarella & cheddar cheese",
            "Onions and capsicum (sliced)",
            "White sauce (cream, garlic, butter, flour)",
            "Oregano & chili flakes"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread white sauce evenly on pizza base.",
            "Add cheese, malai boti chunks, onions, and capsicum.",
            "Bake for 10–12 minutes until cheese melts and crust is golden.",
            "Sprinkle oregano and chili flakes before serving."
        ]
    },
    "Chicken Tikka Pizza": {
        "ingredients": [
            "Prepared pizza dough",
            "Chicken tikka chunks (marinated in tikka masala and grilled)",
            "Tomato pizza sauce",
            "Mozzarella cheese",
            "Onions and capsicum",
            "Green chilies (optional)"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread tomato sauce on the base.",
            "Top with cheese, chicken tikka, and vegetables.",
            "Bake for 10–12 minutes until cheese is bubbly.",
            "Garnish with sliced green chilies for extra spice."
        ]
    },
    "BBQ Pizza": {
        "ingredients": [
            "Prepared pizza dough",
            "BBQ chicken chunks",
            "BBQ sauce (instead of tomato sauce)",
            "Mozzarella & cheddar cheese",
            "Onions (rings)",
            "Coriander leaves"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread BBQ sauce on the base.",
            "Top with cheese, BBQ chicken, and onions.",
            "Bake for 10–12 minutes until golden.",
            "Sprinkle fresh coriander before serving."
        ]
    },
    "Grill Pizza": {
        "ingredients": [
            "Prepared pizza dough",
            "Grilled chicken strips",
            "Tomato sauce",
            "Mozzarella cheese",
            "Grilled vegetables (zucchini, capsicum, onions)",
            "Olive oil drizzle"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread tomato sauce over base.",
            "Add cheese, grilled chicken, and vegetables.",
            "Bake for 10 minutes until crust is crisp.",
            "Drizzle olive oil before serving."
        ]
    },
    "Smoke Pizza": {
        "ingredients": [
            "Prepared pizza dough",
            "Smoked chicken or beef slices",
            "Tomato sauce",
            "Mozzarella cheese",
            "Onions & black olives",
            "Oregano"
        ],
        "steps": [
            "Preheat oven to 250°C (480°F).",
            "Spread tomato sauce on base.",
            "Add cheese, smoked chicken/beef, onions, and olives.",
            "Bake for 8–10 minutes until cheese melts.",
            "Sprinkle oregano before serving."
        ]
    }
}

# User selection
pizza_choice = st.selectbox("Choose a pizza", list(recipes.keys()) + ["Pizza Dough (Base Recipe)"])

# Show recipe
if pizza_choice == "Pizza Dough (Base Recipe)":
    st.subheader("Pizza Dough Recipe (Base for All Pizzas)")
    st.markdown("**Ingredients:**")
    for ingredient in dough_recipe["ingredients"]:
        st.write(f"- {ingredient}")
    st.markdown("**Preparation Steps:**")
    for i, step in enumerate(dough_recipe["steps"], start=1):
        st.write(f"{i}. {step}")
else:
    st.subheader(f"{pizza_choice} Recipe")
    st.markdown("**Ingredients:**")
    for ingredient in recipes[pizza_choice]["ingredients"]:
        st.write(f"- {ingredient}")
    st.markdown("**Preparation Steps:**")
    for i, step in enumerate(recipes[pizza_choice]["steps"], start=1):
        st.write(f"{i}. {step}")
