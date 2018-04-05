arb_string = "Some Words, Here! - Stay!"


def parse_string(data):
    v_count = 0
    c_count = 0
    sp_count = 0
    cap_l_count = 0
    sp_ch_count = 0
    for i in range(len(data)):
        if data[i].isalpha():
            if data[i] in ["a", "e", "i", "y", "u", "o"]:
                v_count += 1
                if data[i].isupper():
                    cap_l_count += 1
            else:
                c_count += 1
                if data[i].isupper():
                    cap_l_count += 1

        else:
            if data[i].isspace():
                sp_count += 1
            else:
                sp_ch_count += 1

    print "vowels {}".format(v_count)
    print "constant {}".format(c_count)
    print "spaces {}".format(sp_count)
    print "capital letters count {}".format(cap_l_count)
    print "Special characters {}".format(sp_ch_count)


parse_string(arb_string)
