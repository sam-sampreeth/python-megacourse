import webbrowser

term = input("Enter a word: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q=" + term)
