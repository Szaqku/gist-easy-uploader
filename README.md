## An app that let you upload piece of code as gist with only few clicks. 

### Installation process: 
###### Clone this app and download packages below:
- requests
- clipboard
1. Generate authorization token for your github acc.
[Link to github tutorial](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
2. Set system environment variable GIST_TOKEN with just generated token.

###### Windows
```setx GIST_TOKEN your_token```
###### Linux
```export GIST_TOKEN=your_token```

### If you want to compile this app to .exe file,
#### Install package auto-py-to-exe (for example with pip) and run this command.
```pyinstaller -y -F  "path\to\app\gist-uploader.py"```


## How to use it ?

### When you want to share file.
#### Using CLI:
````py gist-uploader.py path/to/file/snippet.cpp````

It will upload given file to your github account as gist.

#### Using compiled .exe file on Windows:
Drag file that you want to upload and drop it on this app.

### When you want to share current clipboard.
- Put prefix: "github:" before code that you want to share.
- Select code:
```
github:
template<typename T>
class Node{
	Node* next;
	Node* previous;
	T value;
};
```
- Use app in CLI or as .exe app as described below.
#### Using CLI:
````py gist-uploader.py````
#### Using compiled .exe file on Windows:
Double click on app
