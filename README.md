#Readability
This is a simple Weechat script to strip the colours from recent messages. After receiving a coloured message, use `/readable` in the same buffer to display it as plain text. If multiple coloured messages were received, use `/readable 3` to read 3 messages ago (last message has index 0).

##Installing
Clone the repository or just download readability.py somewhere on your system. Then run `/script load /path/to/readability.py` in Weechat. If you want it to automatically load whenever you start Weechat, copy or link readability.py to `~/.weechat/python/autoload/readability.py`.
