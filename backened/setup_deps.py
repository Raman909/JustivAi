import subprocess
import sys

def main():
    print("Installing requirements.txt and nltk...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk", "-r", "requirements.txt"])
    
    print("Downloading NLTK data...")
    import nltk
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
    print("Dependencies installed successfully.")

if __name__ == "__main__":
    main()
