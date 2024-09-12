# calling function in dll/lib
import ctypes

window_title = "VALORANT  "

# search valorant window
window_handle = ctypes.windll.user32.FindWindowW(None, window_title)

if window_handle == 0:
    # displaying msg box
    ctypes.windll.user32.MessageBoxW(0, "Valorant not Running", "EZ True Stretch", 0)
else:
    # change window properties
    style = ctypes.windll.user32.GetWindowLongW(window_handle, ctypes.c_int(-16))
    style = style & ~0x00800000 # removing WS_DLGFRAME
    style = style & ~0x00040000 # removing WS_BORDER
    ctypes.windll.user32.SetWindowLongW(window_handle, ctypes.c_int(-16), style)

    # maximize window
    ctypes.windll.user32.ShowWindow(window_handle, ctypes.c_int(3))

    ctypes.windll.user32.MessageBoxW(0, "True Strech applied", "EZ True Stretch", 0)