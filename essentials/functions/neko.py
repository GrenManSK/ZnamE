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
        typewriter("Getting image from nekos.best server", ttime=0.01)
        resp = requests.get("https://nekos.best/api/v2/neko", timeout=5)
        data: dict[str, str] = resp.json()
        return requests.get(data["results"][0]["url"], stream=True, timeout=5), data
    elif config["neko settings"]["server"] == "waifu.pics":
        typewriter("Getting image from waifu.pics server", ttime=0.01)
        resp = requests.get("https://api.waifu.pics/sfw/neko", timeout=5)
        data: dict[str, str] = resp.json()
        return requests.get(data["url"], stream=True, timeout=5), data
    elif config["neko settings"]["server"] == "kyoko":
        typewriter("Getting image from kyoko server", ttime=0.01)
        resp = requests.get("https://kyoko.rei.my.id/api/sfw.php", timeout=5)
        data: dict[str, str] = resp.json()
        return requests.get(data["apiResult"]["url"][0], stream=True, timeout=5), data
    elif config["neko settings"]["server"] == "nekos_api":
        typewriter("Getting image from nekos_api server", ttime=0.01)
        resp = requests.get(
            "https://nekos.nekidev.com/api/image/random?categories=catgirl",
            timeout=5,
        )
        data: dict[str, str] = resp.json()
        return requests.get(data["data"][0]["url"], stream=True, timeout=5), data
    else:
        typewriter("No server provided", ttime=0.01)
        return None
