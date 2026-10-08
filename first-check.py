def first_check():
    # to check if the machine already have a live internet connection

    # if ping returns true
    if ping():
        live = "\nCONNECTION ACQUIRED\n"
        print(live)
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "connection acquired at: " + \
            str(connection_acquired_time).split(".")[0]
        print(acquiring_message)

        # writes into the log file
        with open(FILE, "a") as file:
            file.write(live)
            file.write(acquiring_message)
        return True

    # if ping returns false
    else:
        not_live = "\nCONNECTION NOT ACQUIRED\n"
        print(not_live)

        # writes into the log file
        with open(FILE, "a") as file:
            file.write(not_live)
        return False