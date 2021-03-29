# 2fa.py
Google Authenticator but python

- [Install for linux]
- [Install for android]
- [Setup]
- [Run]

# Install [linux]
```sh
$ sudo apt install oathtool -y
$ python3 -m pip install -U pyperclip
```

# Install [android]
```sh
$ pkg install oathtool -y
$ pkg install termux-api -y
$ pkg install python3 -y
```

# Setup your keys
Edit `2fa.py` and find the section that looks like
```py
codes = {
    "Name": "<KEY>",
    "Some bullshit": "MUOI@FE4NBWXN7EW",
}
```
Self explanatory, `Name` is the platform name or whatever and the `<KEY>` should be your token

# Run
```sh
$ python3 2fa.py
```

You can also add `alias 2fa="python3 /path/to/2fa.py"` to your `.bashrc` so you dont have to type `python3` constantly
