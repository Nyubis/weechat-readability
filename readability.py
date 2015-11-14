import weechat as w

w.register("readability", "nyubis", "0.0", "GPLv3",
    "Make messages with markup more readable", "", "")

w.prnt("asfd", "hello")

# dict of buffers to lists. Lists contain coloured messages from buffer
storage = {}

w.hook_print("", "irc_privmsg", "", 0, "messagehook", "")
w.hook_command("readable", "Show the last message with colours stripped out",
    "", "", "", "retrieve", "")

def messagehook(data, buffer, date, tags, displayed, highlight, prefix, message):
    w.prnt("asfd", "Received message: '%s'" % repr(message))
    w.prnt("asfd", "len: %d" % len(message))
    w.prnt("asfd", "buffer: %s" % buffer)
    if not "\x19" in message:
        return w.WEECHAT_RC_OK
    if not buffer in storage:
        storage[buffer] = []
    storage[buffer].append(message)
    return w.WEECHAT_RC_OK

def retrieve(data, buffer, args):
    index = -1
    if len(args) > 0:
        index = -(args[0]+1)
    w.prnt(buffer, w.string_remove_color(storage[buffer][index], ""))
    return w.WEECHAT_RC_OK
