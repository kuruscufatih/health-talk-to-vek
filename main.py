import whisper

def main():
    print("Hello from healt-talk-to!")
    model = whisper.load_model("turbo")
    result = model.transcribe("Snapins.mp3")
    print(result["text"])


if __name__ == "__main__":
    main()
