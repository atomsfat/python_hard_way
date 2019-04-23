import sys, binascii
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    print(f"RAW {raw_bytes}")
    raw_bytes = binascii.unhexlify(raw_bytes)
    print(f"RAW1 {raw_bytes}")
    cooked_string =  raw_bytes.decode(encoding)

    print(raw_bytes, "<=========>", cooked_string)


languages = open("languages2.txt", encoding="utf-8")
main(languages, encoding, error)
