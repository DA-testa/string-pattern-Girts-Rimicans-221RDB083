# python3
def parse_input_user():
    pattern = str(input().strip())
    text = str(input().strip())
    return pattern, text

def parse_input_file(file_name):
    file = open(file_name, "r", -1, "utf-8")
    pattern = str(file.readline().strip())
    text = str(file.readline().strip())
    return pattern, text

def read_input():
    pattern, text = "", ""

    try:
        key = input().strip()
        # print(key)
        if (key.upper() == "I"):
            pattern, text = parse_input_user()
        elif (key.upper() == "F"):
            file_name = input().strip()
            if (file_name.lower() == "a"):
                pass
            pattern, text = parse_input_file("tests/" + file_name)
    except:
        pass
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    q = 101
    d = 256

    pattern_hash = 0
    for i in range(p):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q

    text_hash = 0
    for i in range(p):
        text_hash = (d * text_hash + ord(text[i])) % q

    positions = []
    for i in range(t - p + 1):
        if pattern_hash == text_hash and pattern == text[i:i+p]:
            positions.append(i)
        if i < t - p:
            text_hash = (d * (text_hash - ord(text[i]) * pow(d, p-1, q)) + ord(text[i+p])) % q
            if text_hash < 0:
                text_hash += q

    return positions

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
