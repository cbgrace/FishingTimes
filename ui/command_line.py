import business as b

def get_user_input(prompt: str):
    """
    retrieves user input from the console
    :param prompt: the prompt you would like to display to the user
    :return: the response to a given prompt (string)
    """
    return input(prompt)

def run_test():
    address = get_user_input('What is your address? > ')  # get address from user
    lat_lon = b.get_lat_long(address)  # retrieve lat/lon from address
    print(lat_lon)
