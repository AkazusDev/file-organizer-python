import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from organize import organize_files

'''
##########
########## METHODS
##########
'''


def browse_folder():
    folder_path = filedialog.askdirectory()
    ruta_stv.set(folder_path)


def organize():
    var_options = [bool(var_audios_chk.get()),
                   bool(var_images_chk.get()),
                   bool(var_videos_chk.get()),
                   bool(var_word_chk.get()),
                   bool(var_excel_chk.get()),
                   bool(var_powerPoint_chk.get()),
                   bool(var_pdf_chk.get()),
                   bool(var_compressed_chk.get()),
                   bool(var_exe_chk.get()),
                   bool(var_apk_chk.get()),
                   bool(var_txt_chk.get()),
                   bool(var_web_chk.get()),
                   bool(var_code_chk.get())]
    if ruta_stv.get() == '':
        messagebox.showerror("Sin carpeta", "Elija una carpeta")
    else:
        status = organize_files(ruta_stv.get(), var_options)
        if status:
            messagebox.showinfo("Completado", "Archivos organizados correctamente.")
        else:
            messagebox.showerror("Elija una carpeta", "Inserte una ruta o carpeta válida")




'''
##########
########## GUI
##########
'''
root = tk.Tk()
root.title("File Organizer")

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight() - 40
width_window = 550  # root.winfo_reqheight()
height_window = 450  # root.winfo_reqwidth()

pwidth = round(width_screen/2-width_window/2)
pheight = round(height_screen/2-height_window/2)
root.geometry(str(width_window)+"x"+str(height_window)+"+"+str(pwidth)+"+"+str(pheight))

'''
##########
########## ROOT
##########
'''
tittle_frm = tk.Label(root, text="Organizador de Archivos", font=("Arial", 12), pady=5)
tittle_frm.grid(row=0, column=0)

container = tk.Frame(root, padx=10, pady=10)  # , bg="#D9D9D9"
container.grid(row=1, column=0)

watermark = tk.Label(root, text="Developed by MFES")
watermark.grid(row=2, column=0)

# StringVar
ruta_stv = tk.StringVar()
ruta_stv.set("")

# BooleanVar
var_audios_chk = tk.BooleanVar()
var_images_chk = tk.BooleanVar()
var_videos_chk = tk.BooleanVar()
var_word_chk = tk.BooleanVar()
var_excel_chk = tk.BooleanVar()
var_powerPoint_chk = tk.BooleanVar()
var_pdf_chk = tk.BooleanVar()
var_compressed_chk = tk.BooleanVar()
var_exe_chk = tk.BooleanVar()
var_apk_chk = tk.BooleanVar()
var_txt_chk = tk.BooleanVar()
var_web_chk = tk.BooleanVar()
var_code_chk = tk.BooleanVar()

# List
extensionAudio = ['.mp3', '.ogg', '.wav', '.flac']
extensionImages = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.ico', '.svg']
extensionVideos = ['.mp4', '.avi', '.mkv', '.flv', '.mov']
extensionWord = ['.doc', '.docx', '.docm', '.odt', '.rtf']
extensionExcel = ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xls', '.xltm', '.csv', '.tsv', '.ods']
extensionPowerPoint = ['.pptx', '.pptm', '.ppt', '.potx', '.potm', '.pot', '.ppsx', '.ppsm', '.pps', '.ppam', '.ppa',
                       '.odp']
extensionPdf = ['.pdf', '.epub']
extensionCompressed = ['.rar', '.zip', '.7z', '.tar', '.gzip', '.bzip2']
extensionExe = ['.exe', '.msi', '.appx', '.iso']
extensionApk = ['.apk', '.apkx']
extensionTxt = ['.txt', '.sh', '.cmd', '.bat']
extensionWeb = ['.html', '.css', '.xml', '.js', '.ts', '.php']
extensionCode = ['.py', '.java', '.sql', '.cs', '.cpp', '.js', '.swift', '.rb', '.kt']

# StringVar
extensionAudio_stv = tk.StringVar()
extensionImages_stv = tk.StringVar()
extensionVideos_stv = tk.StringVar()
extensionWord_stv = tk.StringVar()
extensionExcel_stv = tk.StringVar()
extensionPowerPoint_stv = tk.StringVar()
extensionPdf_stv = tk.StringVar()
extensionCompressed_stv = tk.StringVar()
extensionExe_stv = tk.StringVar()
extensionApk_stv = tk.StringVar()
extensionTxt_stv = tk.StringVar()
extensionWeb_stv = tk.StringVar()
extensionCode_stv = tk.StringVar()

extensionImages_stv.set(f'[{", ".join(extensionImages)}]')
extensionAudio_stv.set(f'[{", ".join(extensionAudio)}]')
extensionVideos_stv.set(f'[{", ".join(extensionVideos)}]')
extensionWord_stv.set(f'[{", ".join(extensionWord)}]')
extensionExcel_stv.set(f'[{", ".join(extensionExcel)}]')
extensionPowerPoint_stv.set(f'[{", ".join(extensionPowerPoint)}]')
extensionPdf_stv.set(f'[{", ".join(extensionPdf)}]')
extensionCompressed_stv.set(f'[{", ".join(extensionCompressed)}]')
extensionExe_stv.set(f'[{", ".join(extensionExe)}]')
extensionApk_stv.set(f'[{", ".join(extensionApk)}]')
extensionTxt_stv.set(f'[{", ".join(extensionTxt)}]')
extensionWeb_stv.set(f'[{", ".join(extensionWeb)}]')
extensionCode_stv.set(f'[{", ".join(extensionCode)}]')

'''
##########
########## FRAME: Container
##########
'''
ruta_lbl = tk.Label(container, text="Ruta:")
ruta_lbl.grid(row=1, column=0)

ruta_ent = tk.Entry(container, textvariable=ruta_stv, width=50)
ruta_ent.grid(row=1, column=1)

ruta_btn = tk.Button(container, text="Seleccionar Carpeta", bg="#515AA8", foreground="#FFF", relief='groove',
                     command=lambda: browse_folder())
ruta_btn.grid(row=1, column=2)

ruta_btn = tk.Button(container, text="Organizar", bg="#559F53", foreground="#FFF", relief='groove',
                     command=lambda: organize())
ruta_btn.grid(row=1, column=3)

folders_lbf = tk.LabelFrame(container, text="Carpetas")
folders_lbf.grid(row=2, column=0, columnspan=4)

# WIDTH CHECKBUTTON
width_chk = 10

audios_chk = tk.Checkbutton(folders_lbf, text="Audios", width=width_chk, anchor="w", variable=var_audios_chk,
                            onvalue=True, offvalue=False)
audios_chk.grid(row=0, column=0)
audios_chk.select()

images_chk = tk.Checkbutton(folders_lbf, text="Imágenes", width=width_chk, anchor="w", variable=var_images_chk,
                            onvalue=True, offvalue=False)
images_chk.grid(row=1, column=0)
images_chk.select()

videos_chk = tk.Checkbutton(folders_lbf, text="Videos", width=width_chk, anchor="w", variable=var_videos_chk,
                            onvalue=True, offvalue=False)
videos_chk.grid(row=2, column=0)
videos_chk.select()

word_chk = tk.Checkbutton(folders_lbf, text="Word", width=width_chk, anchor="w", variable=var_word_chk, onvalue=True,
                          offvalue=False)
word_chk.grid(row=3, column=0)
word_chk.select()

excel_chk = tk.Checkbutton(folders_lbf, text="Excel", width=width_chk, anchor="w", variable=var_excel_chk, onvalue=True,
                           offvalue=False)
excel_chk.grid(row=4, column=0)
excel_chk.select()

powerPoint_chk = tk.Checkbutton(folders_lbf, text="PowerPoint", width=width_chk, anchor="w",
                                variable=var_powerPoint_chk, onvalue=True, offvalue=False)
powerPoint_chk.grid(row=5, column=0)
powerPoint_chk.select()

pdf_chk = tk.Checkbutton(folders_lbf, text="PDF", width=width_chk, anchor="w", variable=var_pdf_chk, onvalue=True,
                         offvalue=False)
pdf_chk.grid(row=6, column=0)
pdf_chk.select()

compressed_chk = tk.Checkbutton(folders_lbf, text="Comprimido", width=width_chk, anchor="w",
                                variable=var_compressed_chk, onvalue=True, offvalue=False)
compressed_chk.grid(row=7, column=0)
compressed_chk.select()

exe_chk = tk.Checkbutton(folders_lbf, text="Exe", width=width_chk, anchor="w", variable=var_exe_chk, onvalue=True,
                         offvalue=False)
exe_chk.grid(row=8, column=0)
exe_chk.select()

apk_chk = tk.Checkbutton(folders_lbf, text="Apk", width=width_chk, anchor="w", variable=var_apk_chk, onvalue=True,
                         offvalue=False)
apk_chk.grid(row=9, column=0)
apk_chk.select()

txt_chk = tk.Checkbutton(folders_lbf, text="Txt", width=width_chk, anchor="w", variable=var_txt_chk, onvalue=True,
                         offvalue=False)
txt_chk.grid(row=10, column=0)
txt_chk.select()

web_chk = tk.Checkbutton(folders_lbf, text="Web", width=width_chk, anchor="w", variable=var_web_chk, onvalue=True,
                         offvalue=False)
web_chk.grid(row=11, column=0)
web_chk.select()

code_chk = tk.Checkbutton(folders_lbf, text="Code", width=width_chk, anchor="w", variable=var_code_chk, onvalue=True,
                          offvalue=False)
code_chk.grid(row=12, column=0)
code_chk.select()

# WIDTH CHECKBUTTON
width_lbl = 60

audios_lbl = tk.Label(folders_lbf, textvariable=extensionAudio_stv, width=width_lbl, anchor="w")
audios_lbl.grid(row=0, column=1)
images_lbl = tk.Label(folders_lbf, textvariable=extensionImages_stv, width=width_lbl, anchor="w")
images_lbl.grid(row=1, column=1)
videos_lbl = tk.Label(folders_lbf, textvariable=extensionVideos_stv, width=width_lbl, anchor="w")
videos_lbl.grid(row=2, column=1)
word_lbl = tk.Label(folders_lbf, textvariable=extensionWord_stv, width=width_lbl, anchor="w")
word_lbl.grid(row=3, column=1)
excel_lbl = tk.Label(folders_lbf, textvariable=extensionExcel_stv, width=width_lbl, anchor="w")
excel_lbl.grid(row=4, column=1)
powerPoint_lbl = tk.Label(folders_lbf, textvariable=extensionPowerPoint_stv, width=width_lbl, anchor="w")
powerPoint_lbl.grid(row=5, column=1)
pdf_lbl = tk.Label(folders_lbf, textvariable=extensionPdf_stv, width=width_lbl, anchor="w")
pdf_lbl.grid(row=6, column=1)
compressed_lbl = tk.Label(folders_lbf, textvariable=extensionCompressed_stv, width=width_lbl, anchor="w")
compressed_lbl.grid(row=7, column=1)
exe_lbl = tk.Label(folders_lbf, textvariable=extensionExe_stv, width=width_lbl, anchor="w")
exe_lbl.grid(row=8, column=1)
apk_lbl = tk.Label(folders_lbf, textvariable=extensionApk_stv, width=width_lbl, anchor="w")
apk_lbl.grid(row=9, column=1)
txt_lbl = tk.Label(folders_lbf, textvariable=extensionTxt_stv, width=width_lbl, anchor="w")
txt_lbl.grid(row=10, column=1)
web_lbl = tk.Label(folders_lbf, textvariable=extensionWeb_stv, width=width_lbl, anchor="w")
web_lbl.grid(row=11, column=1)
code_lbl = tk.Label(folders_lbf, textvariable=extensionCode_stv, width=width_lbl, anchor="w")
code_lbl.grid(row=12, column=1)

root.mainloop()
