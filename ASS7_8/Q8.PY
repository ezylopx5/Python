def decode_message(s, output=""):
    if not s:
        print(output)
        return

    if s[0] != '0':
        decode_message(s[1:], output + chr(int(s[:1]) + 64))

    if len(s) > 1 and "10" <= s[:2] <= "26":
        decode_message(s[2:], output + chr(int(s[:2]) + 64))

decode_message("11106")