import weechat as w

w.register("readability", "nyubis", "0.1", "GPLv3",
    "Strip colours from recent messages on demand", "", "")

# dict of buffers to lists. Lists contain coloured messages from buffer
storage = {}

w.hook_print("", "irc_privmsg", "", 0, "messagehook", "")
w.hook_command("readable", "Show the last message with colours stripped out",
    "", "", "", "retrieve", "")

def messagehook(data, buffer, date, tags, displayed, highlight, prefix, message):
    if not "\x19" in message: #no colours in the message
        return w.WEECHAT_RC_OK
    if not buffer in storage:
        storage[buffer] = []
    storage[buffer].append(message)
    return w.WEECHAT_RC_OK

def retrieve(data, buffer, args):
    index = -1 #We need to index the list back to front, so negative indices
    if len(args) > 0:
        index = -(int(args[0])+1)
    if not buffer in storage:
        w.prnt(buffer, "Error: No messages stored for this buffer")
        return w.WEECHAT_RC_OK
    if -index > len(storage[buffer]):
        w.prnt(buffer, "Error: I only have %d messages for this buffer"
            % len(storage[buffer]))
        return w.WEECHAT_RC_OK
    w.prnt(buffer, w.string_remove_color(storage[buffer][index], ""))
    return w.WEECHAT_RC_OK
