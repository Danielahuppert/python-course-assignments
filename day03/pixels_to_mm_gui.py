import tkinter as tk
from tkinter import ttk, messagebox
from pixels_to_mm import pixels_to_mm2, normalized_area

class PixelsToMMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Area to mm² Converter (day03)")
        self.root.geometry("420x320")
        self.root.resizable(False, False)
        
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Pixel Area:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.pixel_entry = ttk.Entry(main_frame, font=("Arial", 12), width=20)
        self.pixel_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        ttk.Label(main_frame, text="Normalization Value:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.norm_entry = ttk.Entry(main_frame, font=("Arial", 12), width=20)
        self.norm_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        self.calculate_btn = ttk.Button(main_frame, text="Convert & Normalize", command=self.calculate)
        self.calculate_btn.grid(row=2, column=0, columnspan=2, pady=15)

        ttk.Label(main_frame, text="Area in mm²:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.mm2_label = tk.Label(main_frame, text="", font=("Arial", 12), fg="blue", bg="lightgray", relief="sunken", padx=5, pady=5)
        self.mm2_label.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        ttk.Label(main_frame, text="Normalized Area:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.norm_label = tk.Label(main_frame, text="", font=("Arial", 12), fg="green", bg="lightgray", relief="sunken", padx=5, pady=5)
        self.norm_label.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        self.clear_btn = ttk.Button(main_frame, text="Clear", command=self.clear)
        self.clear_btn.grid(row=5, column=0, columnspan=2, pady=(10, 40))

        self.pixel_entry.focus()
        root.bind('<Return>', lambda event: self.calculate())

    def calculate(self):
        try:
            pixel_area = float(self.pixel_entry.get().strip())
            normalization_value = float(self.norm_entry.get().strip())
            mm2 = pixels_to_mm2(pixel_area)
            norm = normalized_area(pixel_area, normalization_value)
            self.mm2_label.config(text=f"{mm2:.6f}")
            self.norm_label.config(text=f"{norm:.6f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Normalization value must be non-zero.")

    def clear(self):
        self.pixel_entry.delete(0, tk.END)
        self.norm_entry.delete(0, tk.END)
        self.mm2_label.config(text="")
        self.norm_label.config(text="")
        self.pixel_entry.focus()


def main():
    root = tk.Tk()
    app = PixelsToMMGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
