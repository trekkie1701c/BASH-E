from consts import ModelSize


def parse_arg_boolean(value):
    value = value.lower()

    if value in ["true", "yes", "y", "1", "t"]:
        return True
    elif value in ["false", "no", "n", "0", "f"]:
        return False

    return False

def parse_arg_dalle_version(value):
    value = value.lower()
    return ModelSize[value.upper()]

def parse_arg_save_dir(value):
	return value

def parse_arg_format(value):
	return value

def parse_arg_save_dir(value):
	return value

def parse_arg_prompt(value):
	return value

def parse_arg_list(value):
	if value == "":
		return ""
	else:
		listfile = open(value, "r")
		value = listfile.read()
		value = value.splitlines()
		return value
