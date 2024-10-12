import os
from tkinter import *
from functools import partial
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

class PDFApp:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("700x420")
        self.window.title('Encrypt & Decrypt PDFs')
        self.window.resizable(width=False, height=False)

        # Creating a Frame
        self.frame = Frame(self.window, bg="gray22", width=700, height=420)
        self.frame.place(x=0, y=0)
    
        # Call the main window setup
        self.main_window()

    def main_window(self):
        self.clear_screen()

        # Encrypt Button
        encrypt_button = Button(self.frame, text='Encrypt',
            font=("Helvetica", 18, 'bold'), bg="red", fg="white", width=7,
            command=partial(self.select_file, 1))
        encrypt_button.place(x=280, y=130)
        
        # Decrypt Button
        decrypt_button = Button(self.frame, text='Decrypt', 
            font=("Helvetica", 18, 'bold'), bg="yellow", fg="black", 
            width=7, command=partial(self.select_file, 2))
        decrypt_button.place(x=280, y=200)

    def clear_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
    def select_file(self, to_call):
        self.PDF_path = filedialog.askopenfilename(initialdir="/", 
            title="Select a PDF File", 
            filetypes=(("PDF files", "*.pdf*"),))
        if len(self.PDF_path) != 0:
            if to_call == 1:
                self.encrypt_password()
            else:
                self.decrypt_password()

    def encrypt_password(self):
        pdfReader = PdfReader(self.PDF_path)
        total_pages = len(pdfReader.pages)

        self.clear_screen()

        # Button for getting back to the Home Page
        home_btn = Button(self.frame, text="Home", 
            font=("Helvetica", 8, 'bold'), command=self.main_window)
        home_btn.place(x=10, y=10)

        # Header Label
        header = Label(self.frame, text="Encrypt PDF", 
            font=("Kokila", 25, "bold"), bg="gray22", fg="yellow")
        header.place(x=250, y=15)

        # Label for showing the total number of pages
        pages_label = Label(self.frame, 
            text=f"Total Number of Pages: {total_pages}", 
            font=("Times New Roman", 18, 'bold'), bg="gray22", fg="white")
        pages_label.place(x=40, y=90)

        # Label for showing the filename
        name_label = Label(self.frame, 
            text=f"File Name: {os.path.basename(self.PDF_path)}", 
            font=("Times New Roman", 18, 'bold'), bg="gray22", fg="white")
        name_label.place(x=40, y=130)

        # Set Password Label
        set_password = Label(self.frame, 
            text="Set Password: ", 
            font=("Times New Roman", 18, 'bold'), bg="gray22", fg="white")
        set_password.place(x=40, y=170)
        
        # Entrybox to set the password to encrypt the PDF file
        self.set_password = Entry(self.frame, 
            font=("Helvetica, 12"), show='*')
        self.set_password.place(x=190, y=174)

        # Encrypt Button
        Encrypt_btn = Button(self.frame, text="Encrypt", 
            font=("Kokila", 10, "bold"), cursor="hand2", 
            command=self.encrypt_pdf)
        Encrypt_btn.place(x=290, y=220)

    def decrypt_password(self):
        self.clear_screen()

        # Button for getting back to the Home Page
        home_btn = Button(self.frame, text="Home", 
            font=("Helvetica", 8, 'bold'), command=self.main_window)
        home_btn.place(x=10, y=10)

        # Header Label
        header = Label(self.frame, text="Decrypt PDF", 
            font=("Kokila", 25, "bold"), bg="gray22", fg="yellow")
        header.place(x=250, y=15)

        # Enter Password Label
        enter_password = Label(self.frame, 
            text="Enter Password: ", 
            font=("Times New Roman", 18, 'bold'), bg="gray22", fg="white")
        enter_password.place(x=40, y=170)

        # Entrybox to get the password to decrypt the PDF file
        self.ent_password = Entry(self.frame, 
            font=("Helvetica, 12"), show='*')
        self.ent_password.place(x=220, y=174)

        # Decrypt Button
        Decrypt_btn = Button(self.frame, text="Decrypt", 
            font=("Kokila", 10, "bold"), cursor="hand2", 
            command=self.decrypt_pdf)
        Decrypt_btn.place(x=290, y=220)

    def encrypt_pdf(self):
        if self.set_password.get() == '':
            messagebox.showwarning('Warning', "Please set the password")
        else:
            try:
                # Read the PDF file
                pdfFile = PdfReader(self.PDF_path)
                # Create a PdfWriter object
                pdfWriter = PdfWriter()
                # The Result file: Same name as the original
                result = open(self.PDF_path, 'wb')

                # Iterate through every page of the PDF file
                for page in pdfFile.pages:
                    # Add the page to the pdfWriter variable
                    pdfWriter.add_page(page)

                # Encrypt the PDF file
                pdfWriter.encrypt(user_pwd=self.set_password.get())
                # Write the result file
                with open(self.PDF_path, 'wb') as result_file:
                    pdfWriter.write(result_file)
                messagebox.showinfo('Done!', "The PDF file has been encrypted")
                self.main_window()
                # Set the self.PDF_path to None value
                self.PDF_path = None
            except Exception as es:
                messagebox.showerror('Error!', f"Error due to {es}")

    def decrypt_pdf(self):
        if self.ent_password.get() == '':
            messagebox.showwarning('Warning', "Please enter the password")
        else:
            try:
                pdf_file = open(self.PDF_path, 'rb')
                pdf_reader = PdfReader(pdf_file)

                if pdf_reader.is_encrypted:
                    pdf_reader.decrypt(password=self.ent_password.get())
                    
                    pdf_writer = PdfWriter()

                    for page_num in pdf_reader.pages:
                        pdf_writer.add_page(page_num)

                    # Save the decrypted PDF to a new file
                    output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", 
                        filetypes=[("PDF files", "*.pdf")])
                    if output_file_path:
                        with open(output_file_path, 'wb') as output_file:
                            pdf_writer.write(output_file)
                            messagebox.showinfo("Success", 
                                "PDF decrypted and saved successfully!")

                            self.main_window()
                            self.PDF_path = None

            except Exception as e:
                messagebox.showerror('Error!', "Invalid password, Please try again.")

if __name__ == "__main__":
    root = Tk()
    obj = PDFApp(root)
    root.mainloop()
