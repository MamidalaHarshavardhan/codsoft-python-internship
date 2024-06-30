import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
        
def main():
    global entry1, entry2, operator, result_label


    root = tk.Tk()
    root.title("Simple Calculator")

    tk.Label(root, text="Enter the first number:").grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)

    tk.Label(root, text="Enter the second number:").grid(row=1, column=0)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    tk.Label(root, text="Choose operation:").grid(row=2, column=0)
    operator = tk.StringVar(root)
    operator.set("+")
    tk.OptionMenu(root, operator, "+", "-", "*", "/").grid(row=2, column=1)

    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

    result_label = tk.Label(root, text="Result:")
    result_label.grid(row=4, column=0, columnspan=2)

  
    root.mainloop()

# Run the main program
if __name__ == "__main__":
    main()
