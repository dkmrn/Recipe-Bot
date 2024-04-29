import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_AI_KEY"))

def chatbot():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    numIngredients = 3
    while True:
        ingredients = []
        for i in range(numIngredients):
            message = input(f"Ingredient {i+1}: ")
            if message.lower() == "quit":
                return 0;     
            ingredients.append(message)
        recipePrompt = "Give me a recipe using the following ingredients: "
        for i in range(numIngredients):
            recipePrompt = recipePrompt + ingredients[i] + ", "
            
        messages.append({"role": "user", "content": recipePrompt})

        response = client.chat.completions.create(model = "gpt-3.5-turbo", messages=messages)

        chat_message = response.choices[0].message.content
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})
        
if __name__ == "__main__":
    print("Enter three ingredients and I'll suggest a recipe!(type 'quit' to stop)!")
    chatbot()
