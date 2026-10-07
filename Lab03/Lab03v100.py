inp_milliseconds = 10000123
milliseconds = inp_milliseconds


hours = milliseconds // 3600000
milliseconds = milliseconds % 3600000
minutes = milliseconds // 60000
milliseconds = milliseconds % 60000
seconds = milliseconds // 1000
milliseconds = milliseconds % 1000



print(
    "Lab03, 80 Point Version\n\n"
    f"Starting milli-seconds: {inp_milliseconds}\n"
    "Hours:" + " "*18 + f"{hours}\n"
    "Minutes:" + " "*16 + f"{minutes}\n"
    "Seconds:" + " "*16 + f"{seconds}\n"
    "Milli Seconds:" + " "*10 + f"{milliseconds}\n"
)