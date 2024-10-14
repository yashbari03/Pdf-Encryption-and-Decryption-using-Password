PDF Encryption and Decryption Tool
#Overview
This Python-based application allows users to securely encrypt and decrypt PDF files with password protection. The tool uses a graphical user interface (GUI) built with Tkinter, making it easy to use, even for non-technical users. The PyPDF2 library is employed to handle PDF file manipulation, including encrypting and decrypting the contents of PDF documents.

#Features
Encrypt PDF Files: Add password-based encryption to PDF files, preventing unauthorized access.
Decrypt PDF Files: Unlock encrypted PDF files by entering the correct password.
User-Friendly Interface: A simple GUI built using Tkinter for easy file selection and operation.
Secure and Efficient: Provides quick file processing with effective password encryption.

#Requirements
Python 3.x
Tkinter (usually pre-installed with Python)
PyPDF2 library

#How It Works
Encrypt a PDF: The application uses PyPDF2 to add password encryption to the selected PDF file. The encrypted file can only be opened with the password set during encryption.
Decrypt a PDF: For encrypted files, users can provide the password to decrypt the file and save it as a new PDF.
