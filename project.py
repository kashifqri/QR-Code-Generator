import pywhatkit as pw

text = '''Python is a high-level, interpreted programming language known for its simplicity, readability, and 
versatility. It was created by Guido van Rossum and first released in 1991. Python emphasizes code readability, 
allowing developers to express concepts in fewer lines of code compared to other languages like C++ or Java.'''

pw.text_to_handwriting(text, "demo1.png", [0, 0, 138])

print("END")
