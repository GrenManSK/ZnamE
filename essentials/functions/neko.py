from .writing import typewriter
import requests


def nekof(config):
    """
    The nekof function is used to get a random neko image from the server specified in the config.json file.
    The function returns a tuple containing an image and some metadata about it.

    :param config: Get the server from the config file
    :return: A tuple of two elements
    """
    if config["neko settings"]["server"] == "nekos.best":
        data = get_response(
            "Getting image from nekos.best server",
            "https://nekos.best/api/v2/neko",
        )
        return requests.get(data["results"][0]["url"], stream=True, timeout=5), data
    elif config["neko settings"]["server"] == "waifu.pics":
        data = get_response(
            "Getting image from waifu.pics server",
            "https://api.waifu.pics/sfw/neko",
        )
        return requests.get(data["url"], stream=True, timeout=5), data
    elif config["neko settings"]["server"] == "kyoko":
        data = get_response(
            "Getting image from kyoko server",
            "https://kyoko.rei.my.id/api/sfw.php",
        )
        return requests.get(data["apiResult"]["url"][0], stream=True, timeout=5), data
    elif config["neko settings"]["server"] == "nekos_api":
        data = get_response(
            "Getting image from nekos_api server",
            "https://nekos.nekidev.com/api/image/random?categories=catgirl",
        )
        return requests.get(data["data"][0]["url"], stream=True, timeout=5), data
    else:
        typewriter("No server provided", ttime=0.01)
        return None


def get_response(arg0, arg1):
    typewriter(arg0, ttime=0.01)
    resp = requests.get(arg1, timeout=5)
    result: dict[str, str] = resp.json()
    return result
