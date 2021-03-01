for i in [1, 2]:
    print("i: {:d}".format(i));
    for j in [3.0, 4.0]:
        print("    j: {:.1f}".format(j));
        for w in ["yes", "no"]:
            print("        w: {:s}".format(w));
    # First indent level
    for k in [5.0, 6.0]:
        print("    K: {:.1f}".format(k));