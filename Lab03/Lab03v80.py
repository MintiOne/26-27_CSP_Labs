inp_seconds = 10000
seconds = inp_seconds

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60



print(
    "Lab03, 80 Point Version\n\n"
    f"Starting seconds: {inp_seconds}\n"
    "Hours:" + " "*12 + f"{hours}\n"
    "Minutes:" + " "*10 + f"{minutes}\n"
    "Seconds:" + " "*10 + f"{seconds}\n"
)