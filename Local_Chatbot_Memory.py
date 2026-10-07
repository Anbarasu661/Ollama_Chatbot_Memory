import json
import ollama

MODEL = "llama3.2"  # use your exact model name from `ollama list`
history = []

print("Commands: /history = show memory | /forget = clear memory | quit = exit")

while True:
    user = input("\nYou: ")
    if user.lower() in ("quit", "exit"):
        break
    if user == "/history":
        print(json.dumps(history, indent=2))
        continue
    if user == "/forget":
        history.clear()
        print("Memory cleared.")
        continue

    history.append({"role": "user", "content": user})
    print(f"[Sending {len(history)} message(s) to the model]")

    response = ollama.chat(model=MODEL, messages=history)
    reply = response["message"]["content"]

    history.append({"role": "assistant", "content": reply})
    print("AI:", reply)