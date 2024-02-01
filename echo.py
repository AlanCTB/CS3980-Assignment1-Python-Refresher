#echo.py
#Author: Alan Chen

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text =""
    for i in range(repetitions, 0, -1):
        echoed_text += text[-i:] + "\n"  # Append the sliced text and a newline
    return echoed_text  # Return the echoed text newlines

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
