# Bitwarden Backup
Creates a GPG encrypted backup file of your Bitwarden vault along with any attachments.

Installation: `pip install git+https://github.com/Laharah/bitwarden_backup.git`

Usage: `bw-backup <EMAIL> [<OUTFILE>]`

### Requires 
* [gnugpg](https://gnupg.org/download/index.html#GnuPG)
* [pinentry](https://gnupg.org/download/index.html#pinentry) 
* [bitwarden CLI tool](https://bitwarden.com/help/article/cli/#download-and-install)
* python 3.6+

### Example backup
```
bitwarden_backup.tar.gpg        # Encrypted with your BitWarden password
├── bitwarden_vault.json
├── esurance                    # Attachments filed under vault item name
│   └── insurance_card.jpg
└── truman vpn
    └── openvpn_bkp.tar.gz.gpg
```


