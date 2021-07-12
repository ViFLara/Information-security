import ctypes

attribute_hide = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('concealer.txt', attribute_hide)

if retorno:
    print('File has been hidden')
else:
    print('ile was not hidden')