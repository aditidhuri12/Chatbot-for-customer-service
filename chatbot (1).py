import random
import re

class SupportBot:

    def __init__(self):
        self.negative_res = ("no", "nope", "not a chance", "sorry")
        self.exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

        self.support_responses = {
            'ask_about_product': r'.*\bproduct\b.*',
            'technical_support': r'.*\btechnical.*support\b.*',
            'about_returns': r'.*\breturn\b.*',
            'general_query': r'.*\bhelp\b.*'
        }

    def greet(self):
        self.name = input("Hello! Welcome to our customer support. What's your name?\n")
        will_help = input(f"Hi {self.name}, How can I assist you today?\n").lower()
        if will_help in self.negative_res:
            print("Alright, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thanks for reaching out. Have a great day!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query:\n").lower()
        while not self.make_exit(reply):
            response = self.match_reply(reply)
            print(response)
            reply = input("Do you have any other questions?\n").lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'ask_about_product':
                return self.ask_about_product()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_returns':
                return self.about_returns()
            elif found_match and intent == 'general_query':
                return self.general_query()
        return "I'm not sure about that. Could you please clarify?"

    # --- Sample responses ---
    def ask_about_product(self):
        return "Our products are of the highest quality and come with a 1-year warranty."

    def technical_support(self):
        return "For technical support, please visit our website or call our helpline."

    def about_returns(self):
        return "Our return policy allows returns within 30 days with the receipt."

    def general_query(self):
        return "I'm here to help you with any questions you have about our services."
        

# ✅ Run the bot
bot = SupportBot()
bot.greet()
