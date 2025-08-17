import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def do_encrypt():
    msg = entry_message.get()
    try:
        shift = int(entry_shift.get())
        encrypted_text.set(encrypt(msg, shift))
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")

def do_decrypt():
    msg = entry_message.get()
    try:
        shift = int(entry_shift.get())
        decrypted_text.set(decrypt(msg, shift))
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")

def do_clear():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    encrypted_text.set("")
    decrypted_text.set("")


root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x420") 
root.resizable(False, False)

tk.Label(root, text="Enter Message:").pack(pady=5)
entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=5)

tk.Label(root, text="Enter Shift Value:").pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack(pady=5)

tk.Button(root, text="Encrypt", command=do_encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=do_decrypt).pack(pady=5)
tk.Button(root, text="Clear All", command=do_clear).pack(pady=5)  # 👉 नवीन बटण

encrypted_text = tk.StringVar()
decrypted_text = tk.StringVar()

tk.Label(root, text="Encrypted Text:").pack(pady=5)
tk.Entry(root, textvariable=encrypted_text, width=40, state='readonly').pack(pady=5)

tk.Label(root, text="Decrypted Text:").pack(pady=5)
tk.Entry(root, textvariable=decrypted_text, width=40, state='readonly').pack(pady=5)

root.mainloop()
