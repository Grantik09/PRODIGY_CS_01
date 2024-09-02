import tkinter as tk
from tkinter import messagebox


# Function to encrypt the message
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text


# Function to decrypt the message
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Function to handle encryption and decryption
def handle_cipher(action):
    message = entry_message.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number.")
        return

    shift = int(shift)
    if action == 'Encrypt':
        result = caesar_encrypt(message, shift)
    else:
        result = caesar_decrypt(message, shift)

    label_result.config(text=f"Result: {result}")


# Function to copy the result to the clipboard
def copy_result():
    result_text = label_result.cget("text")[8:]  # Remove the "Result: " prefix
    window.clipboard_clear()
    window.clipboard_append(result_text)
    messagebox.showinfo("Copied", "Result has been copied to clipboard.")


# Function to clear the inputs
def clear_inputs():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    label_result.config(text="Result: ")


# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x350")
window.config(bg="#344955")

# Title label
label_title = tk.Label(window, text="Caesar Cipher Encryptor/Decryptor", font=("Helvetica", 16), bg="#344955",
                       fg="#F9AA33")
label_title.pack(pady=20)

# Message input
label_message = tk.Label(window, text="Enter Message:", font=("Helvetica", 12), bg="#344955", fg="white")
label_message.pack()
entry_message = tk.Entry(window, width=30, font=("Helvetica", 12))
entry_message.pack(pady=5)

# Shift input
label_shift = tk.Label(window, text="Enter Shift Value:", font=("Helvetica", 12), bg="#344955", fg="white")
label_shift.pack()
entry_shift = tk.Entry(window, width=10, font=("Helvetica", 12))
entry_shift.pack(pady=5)

# Encrypt and Decrypt buttons
frame_buttons = tk.Frame(window, bg="#344955")
frame_buttons.pack(pady=10)

button_encrypt = tk.Button(frame_buttons, text="Encrypt", font=("Helvetica", 12),
                           command=lambda: handle_cipher('Encrypt'), bg="#F9AA33", fg="#344955")
button_encrypt.grid(row=0, column=0, padx=10)

button_decrypt = tk.Button(frame_buttons, text="Decrypt", font=("Helvetica", 12),
                           command=lambda: handle_cipher('Decrypt'), bg="#F9AA33", fg="#344955")
button_decrypt.grid(row=0, column=1, padx=10)

# Result label
label_result = tk.Label(window, text="Result: ", font=("Helvetica", 14), bg="#344955", fg="white")
label_result.pack(pady=10)

# Copy button
button_copy = tk.Button(window, text="Copy Result", font=("Helvetica", 12), command=copy_result, bg="#F9AA33",
                        fg="#344955")
button_copy.pack(pady=5)

# Clear button
button_clear = tk.Button(window, text="Clear", font=("Helvetica", 12), command=clear_inputs, bg="#F9AA33", fg="#344955")
button_clear.pack(pady=5)

# Run the application
window.mainloop()



