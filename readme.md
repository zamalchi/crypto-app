# crypto app
### bottle app for receiving and logging encrypted hours
- `run.py` requires:
    - `-a` : host address
    - `-p` : port
- use `launcher.sh` to run with presets
- requires `config/crypto` for decrypting records
    - contains two 16-charater keys
    - separated by a newline
    - must match crypto file in the sending server
