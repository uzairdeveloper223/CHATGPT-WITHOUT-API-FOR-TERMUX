#!/bin/bash
RED="\e[31m"
GREEN="\e[32m"
BLUE="\e[34m"
RESET="\e[0m"

echo -e "${GREEN}Installing Termux-tool to run SOYES${RESET}"
if ! command -v termux-open &> /dev/null; then
  echo "Installing termux-tools..."                                                                                                            pkg install termux-tools
fi


echo "Starting your Script please wait"
  sleep 3

# ASCII art for "CHATGPT" in green
echo -e "${GREEN}  ____        _   _        ____   "
echo -e "${GREEN} / ___|  ___ | | | | ___  / ___|  "
echo -e "${GREEN} \___ \ / _ \| | | |/ _ \ \___ \  "
echo -e "${GREEN}  ___) | (_) | |_| |  __/  ___) | "
echo -e "${GREEN} |____/ \___/ \__, |\___| |____/  "
echo -e "${GREEN}               |_|               "

# Additional text in blue and green
echo -e "${BLUE}Ask anything${RESET}"
echo -e "${GREEN}Created by Uzairdeveloper223${RESET}"
                                                                                                                                             # Declare a variable to store the responses
declare -A responses                                                                                                                                                                                                                                                                      # Define your responses here, case-insensitive
responses["hello"]="Hello there!"                                                                                                            responses["how are you?"]="I'm doing well, thank you for asking."
responses["meaning of life?"]="That's a profound question! It is something that philosophers have debated for centuries. I believe the meaning of life is unique to each individual, and it is up to us to discover what gives our lives purpose and meaning."
responses["How are you?"]="I'm doing well, thanks for asking! I'm always ready to help with whatever you need."
responses["a joke."]="What do you call a lazy kangaroo? A pouch potato!"
responses["weather"]="I'm not able to access weather information directly, but I can help you find a reliable weather forecast online."
responses["song."]="(In a robotic voice) I'm not much of a singer, but here's a little ditty: 01010101 10101010..."
responses["favorite color?"]="My favorite color is a rich, vibrant green, like the color of nature and growth."
responses["advice for me?"]="Always be kind to yourself and others, follow your dreams, and never give up on learning and growing."
responses["write html"]="HTML is used to create structure and content of web pages. Here's a basic example of an HTML document:<!DOCTYPE html>(next line)<html>(next line)<head>(next line)<title>This is a simple HTML page</title>(next line)</head>(next line)<body>(next line)<h1>Hello, world!</h1><p>This is a paragraph of text.</p></body></html>":
responses["write python"]="Python is a versatile programming language used for web development, data analysis, machine learning, and more. Here's a simple Python program that prints a greeting:print('Hello, Python world!'"
responses["shell"]="Shell scripts are used...Shell scripts are used to automate tasks on Unix-like operating systems. Here's a simple Shell script that echoes a message:remove the brackets (#!/bin/bash(on next line)echo 'Hello from a Bash script!')"
# Add more responses as needed

# Display a loading animation for 4 seconds
for i in {1..4}; do
  echo -n "Loading .. "
  sleep 1
  echo -n "."
done
echo

# Prompt the user for input
while true; do
read -p "Enter a quote or word: " quote

if [[ "$quote" == "exit" ]]; then
    echo -e "${BLUE}Thanks for Using!"                                                                                                           break
  fi                                                                                                                                         
# Convert the input to lowercase for case-insensitive matching                                                                               quote_lower=$(echo "$quote" | tr '[:upper:]' '[:lower:]')                                                                                                                                                                                                                                 # Search for full or partial word matches                                                                                                    for keyword in "${!responses[@]}"; do                                                                                                          if [[ "$quote_lower" == "$keyword" || "$quote_lower" =~ "$keyword" ]]; then                                                                    response="${responses[$keyword]}"
    echo -e "${GREEN}$response${RESET}"                                                                                                          break  # Exit the loop if a match is found                                                                                                 fi                                                                                                                                         done
                                                                                                                                             # If no match found, proceed with original logic                                                                                             if [[ -z "$response" ]]; then                                                                                                                  # Search for a matching response using the original method                                                                                   response="${responses[$quote_lower]}"

  if [[ -n "$response" ]]; then
    # Response found, display it
    echo "$response"
  else
    # Response not found, prompt for browser search
    read -p "Response not found. Open in browser? (y/n): " open_browser

    if [[ "$open_browser" =~ ^[Yy]$ ]]; then
      # Escape the quote for safe command injection
      escaped_quote=$(echo "$quote" | sed 's/[^a-zA-Z0-9 ]/\\&/g')
      # Open the browser with the Google search link
      termux-open "https://www.google.com/search?q=$escaped_quote"
    fi
  fi
fi
done