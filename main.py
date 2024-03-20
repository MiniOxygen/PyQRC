import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import ImageTk, Image

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.label = tk.Label(master, text="Enter content for QR Code:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.preview_label = tk.Label(master, text="Preview:")
        self.preview_label.pack()

        self.qr_image = None
        self.preview_canvas = tk.Canvas(master, width=400, height=400)
        self.preview_canvas.pack()

        self.save_button = tk.Button(master, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack()

    def generate_qr_code(self):
        qr_content = self.entry.get()
        if qr_content.strip() == "":
            messagebox.showerror("Error", "Please enter content for QR code.")
            return

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_content)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_image = ImageTk.PhotoImage(img.resize((400, 400), Image.FIXED))
        self.preview_canvas.create_image(0, 0, anchor=tk.NW, image=self.qr_image)

    def save_qr_code(self):
        if self.qr_image is None:
            messagebox.showerror("Error", "No QR code generated to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img = self.qr_image
            img_data = img._PhotoImage__photo.subsample(1, 1)
            img_data.write(file_path, format="png")

            messagebox.showinfo("Success", f"QR code saved as '{file_path}'.")


def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
