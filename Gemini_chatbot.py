import google.generativeai as genai


genai.configure(api_key="your own api-key collected form Gemini")
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "" 

while True:
    print("Type 'exit' to quit or 'clear' to delete all!")
    prompt = input("Enter your prompt here: ")

    if prompt.lower() == "exit":
        print("You are out of the loop")
        break
    elif prompt.lower() == "clear":
        print("\033[H\033[J", end="")
    else:
        response = model.generate_content(prompt)
        print("\n\n\n", response.text)
