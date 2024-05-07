import random
import datetime

class Chatbot:
    def __init__(self):
        self.memory = {}
        self.responses = {
            "greetings": ["Hello!", "Hi there!", "Hey!", "Hey, how are you?"],
            "farewell": ["Goodbye!", "See you later!", "Bye! Take care!"],
            "acknowledge": ["Great! Let me know if there's anything else I can help with."],
            "thankyou": ["You're welcome! If you have any further questions or need assistance, feel free to ask."],
            "questions": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good!"],
            "default_responses": ["Sorry, I didn't catch that. Could you please repeat?",
                                  "I'm not sure I understand. Could you provide more details?",
                                  "Hmm, I'm having trouble understanding. Can you rephrase that?",
                                  "Apologies, could you clarify what you mean?",
                                  "I'm still learning! Can you try saying that another way?",
                                  "It seems I'm not following. Could you explain again?",
                                  "I'm having trouble processing that. Can you try again?",
                                  "That's a bit unclear to me. Can you give me more context?",
                                  "I'm afraid I didn't get that. Can you elaborate?",
                                  "Sorry, could you please clarify what you're asking?",
                                  "I'm not quite sure what you mean. Could you explain further?",
                                  "Hmm, that's not ringing any bells. Can you give me more details?",
                                  "I'm having trouble processing your request. Can you try again?",
                                  "It seems like I'm missing something. Could you provide additional information?",
                                  "Sorry, I'm drawing a blank. Can you give me some more context?",
                                  "I'm not sure I'm following. Could you break it down for me?",
                                  "I'm having difficulty understanding your message. Can you simplify it?",
                                  "I'm struggling to understand. Could you phrase it differently?",
                                  "It appears I'm not getting your point. Can you try expressing it differently?",
                                  "Sorry, I'm a bit confused. Can you provide more clarity?"],
        }
        self.commands = {
            "greet": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
            "farewell": ["bye", "quit", "exit", "see you later"],
            "thankyou": ["thanks", "thank you", "appreciate it"],
            "time": ["what time is it?", "current time", "time"],
        }
        self.user_name = None

    def respond(self, input_text):
        input_text_lower = input_text.lower()
        if input_text_lower in self.memory:
            return self.memory[input_text_lower]

        for intent, keywords in self.commands.items():
            if any(keyword in input_text_lower for keyword in keywords):
                response = self._handle_command(intent)
                self.memory[input_text_lower] = response
                return response

        if "my name is" in input_text_lower:
            self.user_name = input_text_lower.split("my name is")[-1].strip()
            response = f"Nice to meet you, {self.user_name}!"
            self.memory[input_text_lower] = response
            return response

        response = random.choice(self.responses["default_responses"])
        self.memory[input_text_lower] = response
        return response

    def _handle_command(self, intent):
        if intent == "greet":
            return random.choice(self.responses["greetings"])
        elif intent == "farewell":
            return random.choice(self.responses["farewell"])
        elif intent == "thankyou":
            return random.choice(self.responses["thankyou"])
        elif intent == "time":
            current_time = datetime.datetime.now().strftime("%H:%M")
            return f"The current time is {current_time}."

    def start(self):
        print("Chatbot: Hi! I'm a smart chatbot. What can I do for you today?")
        while True:
            user_input = input("You: ")
            response = self.respond(user_input)
            print("Chatbot:", response)
            if user_input.lower() in self.commands["farewell"]:
                break

chatbot = Chatbot()
chatbot.start()
