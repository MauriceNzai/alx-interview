
finally:
    print("File size: {:d}".format(total_file_size))
    sorted_keys = sorted(status_code.keys())
    for key in sorted_keys:
        val = status_code[key]
        if val != 0:
            print("{}: {}".format(key, val))
