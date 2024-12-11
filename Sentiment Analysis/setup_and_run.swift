import Foundation

print("Sentiment Analysis Setup and Execution on macOS")

print("\nStep 1: Install Python")
print("macOS usually comes with Python pre-installed, but you can install the latest version using Homebrew if needed.")
print("1. Install Homebrew (if not already installed):")
print("   Open Terminal and run:")
print("   /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
print("2. Install Python using Homebrew:")
print("   brew install python")
print("3. Verify Python installation:")
print("   python3 --version")

print("\nStep 2: Create a Virtual Environment")
print("1. Open Terminal and navigate to the directory where you want to create the project.")
print("2. Create a virtual environment by running:")
print("   python3 -m venv sentiment_env")
print("3. Activate the virtual environment:")
print("   source sentiment_env/bin/activate")

print("\nStep 3: Install Dependencies")
print("1. Create a requirements.txt file with the following content:")
print("   nltk==3.8.1")
print("   textblob==0.17.1")
print("   transformers==4.34.0")
print("   torch==2.0.1")
print("   pandas==2.0.3")
print("   numpy==1.24.4")
print("   matplotlib==3.8.0")
print("   seaborn==0.12.2")
print("   wordcloud==1.9.2")
print("2. Install the dependencies:")
print("   pip install -r requirements.txt")

print("\nStep 4: Run the Sentiment Analysis Script")
print("1. Write the sentiment analysis script (Python) based on the libraries and methods used.")
print("2. Run the script:")
print("   python sentiment_analysis.py")

print("\nStep 5: Deactivate Virtual Environment")
print("Once the script has been run, deactivate the virtual environment by running:")
print("   deactivate")