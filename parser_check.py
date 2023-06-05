import difflib


def command_parser(input_string, command_list):
    if input_string.lower() in command_list:
        print(f"I follow the command: {input_string}")
        return command_list[input_string]

    suggestion = difflib.get_close_matches(input_string, command_list, cutoff=0.55)
    if suggestion:
        return f"An unknown command. Maybe you mean: {', '.join(suggestion)}."
    else:
        return "An unknown command."

