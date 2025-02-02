import tkinter as tk
from tkinter import ttk, messagebox
import string
import pyperclip  # type: ignore # For copying text to clipboard

def caesar_cipher(text, shift, decrypt=False):
    """Encrypts or decrypts text using Caesar cipher, including special characters."""
    if decrypt:
        shift = -shift

    alphabet = string.ascii_letters + string.digits + string.punctuation  # Encrypt everything!
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(table)

def encrypt_text():
    """Encrypts input text and displays the result."""
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_var.get())
    encrypted_text = caesar_cipher(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt_text():
    """Decrypts input text and displays the result."""
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_var.get())
    decrypted_text = caesar_cipher(text, shift, decrypt=True)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

def copy_to_clipboard():
    """Copies output text to clipboard."""
    text = output_text.get("1.0", "end-1c")
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Enhanced Caesar Cipher")
root.geometry("550x400")
root.config(bg="#2C2F33")

# Title Label
tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 16, "bold"), fg="white", bg="#2C2F33").pack(pady=10)

# Input Text Field
tk.Label(root, text="Input Text:", font=("Arial", 12), fg="white", bg="#2C2F33").pack()
input_text = tk.Text(root, height=3, width=60, bg="#40444B", fg="white", font=("Arial", 10))
input_text.pack()

# Shift Dropdown
tk.Label(root, text="Shift:", font=("Arial", 12), fg="white", bg="#2C2F33").pack()
shift_var = tk.StringVar(value="3")
shift_dropdown = ttk.Combobox(root, textvariable=shift_var, values=[str(i) for i in range(1, 26)])
shift_dropdown.pack()

# Buttons
button_frame = tk.Frame(root, bg="#2C2F33")
button_frame.pack(pady=10)

encrypt_btn = tk.Button(button_frame, text="Encrypt", command=encrypt_text, font=("Arial", 12), bg="lightblue")
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(button_frame, text="Decrypt", command=decrypt_text, font=("Arial", 12), bg="lightgreen")
decrypt_btn.grid(row=0, column=1, padx=5)

copy_btn = tk.Button(button_frame, text="Copy", command=copy_to_clipboard, font=("Arial", 12), bg="yellow")
copy_btn.grid(row=0, column=2, padx=5)

# Output Text Field
tk.Label(root, text="Output Text:", font=("Arial", 12), fg="white", bg="#2C2F33").pack()
output_text = tk.Text(root, height=3, width=60, bg="#40444B", fg="white", font=("Arial", 10))
output_text.pack()

# Run the application
root.mainloop()

