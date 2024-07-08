import business as b


def get_user_input(prompt: str) -> str:
    """
    cleans up the user input a bit
    :param prompt: the prompt you wish to display in the console
    :return: the user's response
    """
    user_response = input(prompt)
    return user_response.strip()


def run_test():
    # address = get_user_input('What is your address? > ')  # get address from user
    address = '930 W Clinton Dr, Fayetteville, AR 72701'
    lat_lon = b.get_lat_long(address)  # retrieve lat/lon from address
    latitude = lat_lon[0]
    longitude = lat_lon[1]
    forecast_data = b.get_forecast_data(latitude, longitude)
    print(forecast_data)
