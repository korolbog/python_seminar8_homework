
import ui
import operations_shell as opshell

def start_system():
    ui.show_instructions()
    input_command = ui.user_command()
    
    if input_command == 1:
        opshell.show_all_files_content()
    elif input_command == 2:
        opshell.add_data()
