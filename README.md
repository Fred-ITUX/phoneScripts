# 📱 phoneScripts

![Platform](https://img.shields.io/badge/platform-iSH%20(iOS)-555?logo=apple&logoColor=white)
![Shell](https://img.shields.io/badge/shell-Alpine%20bash-0D597F?logo=alpinelinux&logoColor=white)
![Python](https://img.shields.io/badge/python-3-3776AB?logo=python&logoColor=white)

**Date**: 2026_10_29

Scripts for [iSH](https://ish.app), the Alpine Linux shell for iOS: profile and aliases, repo self-update, and small Python tools and games.

```text
phoneScripts/
├── 🛠️ Utilities/
│   ├── setup.sh             first run: git identity, exec bits, installs the profile
│   ├── profile.sh           copied to ~/.profile: paths and aliases
│   ├── repo_update.sh       discards local changes, pulls, reinstalls the profile
│   ├── new_install.sh       apk packages (log in log_install.txt)
│   ├── loop.sh              keeps iSH alive in the background
│   ├── welcome_home.sh      /etc/motd text
│   └── startup_routine.sh
└── 🐍 Scripts/
    ├── perc_calc.py         percentage calculator
    └── Games/               math quiz, poker-jack, Pokémon randomizer, Dark Souls randomizer and bingo
```

## 📥 Setup

```bash
apk add git bash python3
git clone https://github.com/Fred-ITUX/phoneScripts.git ~/phoneScripts
~/phoneScripts/Utilities/setup.sh
```

## ⌨️ Aliases

Defined in `profile.sh`, available after `setup`:

| Alias | Runs |
|---|---|
| `repoUPD` | `repo_update.sh`: pull the latest version |
| `setup` | `setup.sh` |
| `loop` | `loop.sh` in the background |
| `percentage` | `perc_calc.py` |
| `math` / `poker-jack` | the games in `Scripts/Games/` |
| `profile` / `welcome` | edit `~/.profile` / `/etc/motd` |

## ⚠️ Local changes

`repo_update.sh` runs `git reset --hard`: anything edited on the phone is lost on the next update. Edit in Nextcloud instead.
