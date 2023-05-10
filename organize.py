from os import path, mkdir, listdir, rename, getcwd


def format_path(folder_path):
    var_format_path = ""
    for caracter in folder_path:
        if caracter == '\\':
            var_format_path = var_format_path + '/'
        else:
            var_format_path = var_format_path + caracter
    return var_format_path


def current_route():
    route = getcwd()
    format_path(route)
    return route


def organize_files(ruta_actual, checks_options):
    folder_to_organize = format_path(ruta_actual) + "/"

    if path.exists(folder_to_organize):
        # New paths to organize files
        folder_organize = folder_to_organize + 'Archivos_Organizados'
        folder_organize_images = folder_to_organize + 'Archivos_Organizados/Imágenes'
        folder_organize_audios = folder_to_organize + 'Archivos_Organizados/Audios'
        folder_organize_videos = folder_to_organize + 'Archivos_Organizados/Videos'
        folder_organize_word = folder_to_organize + 'Archivos_Organizados/Word'
        folder_organize_excel = folder_to_organize + 'Archivos_Organizados/Excel'
        folder_organize_powerpoint = folder_to_organize + 'Archivos_Organizados/Power_Point'
        folder_organize_pdf = folder_to_organize + 'Archivos_Organizados/Pdf'
        folder_organize_rar = folder_to_organize + 'Archivos_Organizados/Comprimidos'
        folder_organize_exe = folder_to_organize + 'Archivos_Organizados/Exe'
        folder_organize_apk = folder_to_organize + 'Archivos_Organizados/Apk'
        folder_organize_txt = folder_to_organize + 'Archivos_Organizados/Txt'
        folder_organize_web = folder_to_organize + 'Archivos_Organizados/Web'
        folder_organize_code = folder_to_organize + 'Archivos_Organizados/Code'

        # File extensions
        extension_audio = ['.mp3', '.ogg', '.wav', '.flac']
        extension_images = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.ico', '.svg']
        extension_videos = ['.mp4', '.avi', '.mkv', '.flv', '.mov']
        extension_word = ['.doc', '.docx', '.docm', '.odt', '.rtf']
        extension_excel = ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xls', '.xltm', '.csv', '.tsv', '.ods']
        extension_powerpoint = ['.pptx', '.pptm', '.ppt', '.potx', '.potm', '.pot', '.ppsx', '.ppsm', '.pps', '.ppam',
                                '.ppa', '.odp']
        extension_pdf = ['.pdf', '.epub']
        extension_compressed = ['.rar', '.zip', '.7z', '.tar', '.gzip', '.bzip2']
        extension_exe = ['.exe', '.msi', '.appx', '.iso']
        extension_apk = ['.apk', '.apkx']
        extension_txt = ['.txt', '.sh', '.cmd', '.bat']
        extension_web = ['.html', '.css', '.xml', '.js', '.ts', '.php']
        extension_code = ['.py', '.java', '.sql', '.cs', '.cpp', '.js', '.swift', '.rb', '.kt']

        # Create folders
        if not path.exists(folder_organize):
            mkdir(folder_organize)
        if not path.exists(folder_organize_audios) and checks_options[0]:
            mkdir(folder_organize_audios)
        if not path.exists(folder_organize_images) and checks_options[1]:
            mkdir(folder_organize_images)
        if not path.exists(folder_organize_videos) and checks_options[2]:
            mkdir(folder_organize_videos)
        if not path.exists(folder_organize_word) and checks_options[3]:
            mkdir(folder_organize_word)
        if not path.exists(folder_organize_excel) and checks_options[4]:
            mkdir(folder_organize_excel)
        if not path.exists(folder_organize_powerpoint) and checks_options[5]:
            mkdir(folder_organize_powerpoint)
        if not path.exists(folder_organize_pdf) and checks_options[6]:
            mkdir(folder_organize_pdf)
        if not path.exists(folder_organize_rar) and checks_options[7]:
            mkdir(folder_organize_rar)
        if not path.exists(folder_organize_exe) and checks_options[8]:
            mkdir(folder_organize_exe)
        if not path.exists(folder_organize_apk) and checks_options[9]:
            mkdir(folder_organize_apk)
        if not path.exists(folder_organize_txt) and checks_options[10]:
            mkdir(folder_organize_txt)
        if not path.exists(folder_organize_web) and checks_options[11]:
            mkdir(folder_organize_web)
        if not path.exists(folder_organize_code) and checks_options[12]:
            mkdir(folder_organize_code)

        # Organize files
        for filename in listdir(folder_to_organize):
            name, extension = path.splitext(folder_to_organize + filename)

            # AUD
            if extension in extension_audio and checks_options[0]:
                rename(folder_to_organize + filename, folder_organize_audios + '/' + filename)

            # IMG
            if extension in extension_images and checks_options[1]:
                rename(folder_to_organize + filename, folder_organize_images + '/' + filename)

            # MOV
            if extension in extension_videos and checks_options[2]:
                rename(folder_to_organize + filename, folder_organize_videos + '/' + filename)

            # WORD
            if extension in extension_word and checks_options[3]:
                rename(folder_to_organize + filename, folder_organize_word + '/' + filename)

            # EXCEL
            if extension in extension_excel and checks_options[4]:
                rename(folder_to_organize + filename, folder_organize_excel + '/' + filename)

            # POWERPOINT
            if extension in extension_powerpoint and checks_options[5]:
                rename(folder_to_organize + filename, folder_organize_powerpoint + '/' + filename)

            # PDF
            if extension in extension_pdf and checks_options[6]:
                rename(folder_to_organize + filename, folder_organize_pdf + '/' + filename)

            # RAR
            if extension in extension_compressed and checks_options[7]:
                rename(folder_to_organize + filename, folder_organize_rar + '/' + filename)

            # EXE
            if extension in extension_exe and checks_options[8]:
                rename(folder_to_organize + filename, folder_organize_exe + '/' + filename)
            # APK
            if extension in extension_apk and checks_options[9]:
                rename(folder_to_organize + filename, folder_organize_apk + '/' + filename)

            # TXT
            if extension in extension_txt and checks_options[10]:
                rename(folder_to_organize + filename, folder_organize_txt + '/' + filename)

            # WEB
            if extension in extension_web and checks_options[11]:
                rename(folder_to_organize + filename, folder_organize_web + '/' + filename)

            # CODE
            if extension in extension_code and checks_options[12]:
                rename(folder_to_organize + filename, folder_organize_code + '/' + filename)
        return True
    return False
