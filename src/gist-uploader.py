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

        if str(f.name).find(os.path.sep) != -1:
            fileName = f.name[f.name.rindex(os.path.sep) + 1:]

        data["files"] = {fileName: {"content": str(f.read())}}
    else:
        print("Wrong input was given.")
        exit(0)

    token = os.getenv("GIST_TOKEN")
    if token is None:
        raise EnvironmentError("Can't find GIST_TOKEN env variable.")

    response = requests.request('post', 'https://api.github.com/gists', json=data,
                                headers={"Accept": "application/vnd.github.v3+json",
                                         "Authorization": "token " + token})

    if response.status_code != 201:
        print(response.content)
        input("Press ENTER to close window.")
        exit()

    response = response.json()
    print("https://gist.github.com/" + response['owner']['login'] + "/" + response['id'])
    clipboard.copy("https://gist.github.com/" + response['owner']['login'] + "/" + response['id'])
    input("Link to just created gist has been copied to your clipboard.\nPress ENTER to close window.")