# coding: utf-8


def urler(str):
    try:
        link, params = str.split("?", 1)
        path, name = parse_path(link)
        try:
            req, metka = params.split("#", 1)
            try:
                args = req.split("&")
                return path, name, params_to_dict(args), metka
            except ValueError:
                return path, name, req, metka
        except ValueError:
            metka = ""
            try:
                args = params.split("&")
                return path, name, params_to_dict(args), metka
            except ValueError:
                return path, name, params, metka
    except ValueError:
        args = {}
        try:
            link, metka = str.split("#", 1)
            path, name = parse_path(link)
            return path, name, args, metka
        except ValueError:
            metka = ""
            path, name = parse_path(str)
            return path, name, args, metka


def parse_path(link):
    name = link.split("/")[-1:][0]
    tree = link.split("/")[3:-1]
    path = ""
    for i in tree:
        path += "/" + i
    return path, name


def params_to_dict(params):
    d = {}
    for i in params:
        key, value = i.split("=")
        d[key] = value
    return d
