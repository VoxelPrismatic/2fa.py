# 2fa.py
Google Authenticator but python

- [Install for linux](#install-linux)
- [Install for android](#install-android)
- [Setup](#setup)
- [Run](#run)

# Install [linux]
```sh
$ sudo apt install oathtool -y
$ python3 -m pip install -U pyperclip
```

# Install [android]
note: assuming termux
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

# Exit
Just hit `CTRL`+`C`, your terminal data should not have been cleared

# Features
If you click on a code, granted you running it in a VT200 compatible emulator, it'll turn a different color and will be copied to your clipboard.

# Screenshots
![image 1](https://media.discordapp.net/attachments/569698278271090728/826126157765410826/unknown.png)
![image 2](https://media.discordapp.net/attachments/569698278271090728/826126193244766228/unknown.png)
