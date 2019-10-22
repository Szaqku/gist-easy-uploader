import os
import sys
import requests
import clipboard

if __name__ == '__main__':
    print(sys.argv)
    data = {
        "description": "default",
        "public": True,
        "files": {}
    }

    cp = str(clipboard.paste())
    if cp.startswith("github:") and len(sys.argv) < 2:
        data["files"] = {"clipboard": {"content": cp[7:]}}
    elif len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
        fileName = "default-name"

        try:
            fileName = f.name[f.name.rindex("/") + 1:]
        except ValueError as ex:
            fileName = f.name
            # print(ex)

        data["files"] = {fileName: {"content": str(f.read())}}
    else:
        print("Wrong args were given.")
        exit(0)

    # print(data)
    token = os.getenv("GIST_TOKEN")
    if token is None:
        raise EnvironmentError("Can't find GIST_TOKEN env variable.")
    # print(token)
    output = requests.request('post', 'https://api.github.com/gists', json=data,
                              headers={"Accept": "application/vnd.github.v3+json",
                                       "Authorization": "token " + token})

    # print(output.headers)
    output = output.json()
    # print(output)
    print("https://gist.github.com//" + output['owner']['login'] + "//" + output['id'])
    clipboard.copy("https://gist.github.com/" + output['owner']['login'] + "/" + output['id'])
