# Step 1: Define the bot's personality
bot_name = "CryptoBuddy"

def greet():
    print(f"Hey there! I'm {bot_name}, your AI-powered financial sidekick. Let's find you the best crypto investments!")

# Step 2: Predefined Crypto Data
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# Step 3: Chatbot logic with simple if-else
def get_response(user_query):
    user_query = user_query.lower()
    
    if "trending up" in user_query or "price trend" in user_query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending:
            return f"The following cryptocurrencies are trending up: {', '.join(trending)} 🚀"
        else:
            return "No cryptocurrencies are currently trending up."
    
    elif "most sustainable" in user_query or "sustainability" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        score = crypto_db[recommend]["sustainability_score"]
        return f"Invest in {recommend}! 🌱 It has the highest sustainability score of {score:.1f}."
    
    elif "best for long-term growth" in user_query:
        # Prioritize rising price trend and high market cap
        candidates = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if candidates:
            return f"{candidates[0]} is trending up with a high market cap – great for long-term growth!"
        else:
            # fallback to highest sustainability score with rising trend
            sustainable_candidates = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            if sustainable_candidates:
                recommend = max(sustainable_candidates, key=lambda x: crypto_db[x]["sustainability_score"])
                return f"{recommend} is trending up and has a strong sustainability score for long-term growth!"
            else:
                return "No strong candidates found for long-term growth."
    
    else:
        return "Sorry, I didn't understand that. Can you ask about trending cryptos, sustainability, or long-term growth?"

# Step 5: Interact with the bot
greet()
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print(f"{bot_name}: Goodbye! Happy investing! 💰")
        break
    response = get_response(user_input)
    print(f"{bot_name}: {response}")