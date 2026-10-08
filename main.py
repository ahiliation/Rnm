def main():
    # MAIN
    monitor_start_time = datetime.datetime.now()
    
    # monitoring time is when the script
    # started monitoring internet connection status
    monitoring_date_time = "monitoring started at: " + \
        str(monitor_start_time).split(".")[0]

    if first_check():
        # if true
        print(monitoring_date_time)
        
        # monitoring will only start when
        # the connection will be acquired

    else:
        # if false
        while True:
          
            # infinite loop to check if the connection is acquired
            # will run until there is a live internet connection
            if not ping():
              
                # if connection not acquired
                time.sleep(1)
            else:
              
                # if connection is acquired
                first_check()
                print(monitoring_date_time)
                break

            with open(FILE, "a") as file:
                # writes into the log file
                file.write("\n")
                file.write(monitoring_date_time + "\n")

    while True:
      
        # FIRST WHILE, infinite loop,
        # will run until the machine is on
        # or the script is manually terminated
        if ping():
            # if true: the loop will execute after every 5 seconds
            time.sleep(5)

        else:
          
            # if false: fail message will be displayed
            down_time = datetime.datetime.now()
            fail_msg = "disconnected at: " + str(down_time).split(".")[0]
            print(fail_msg)

            with open(FILE, "a") as file:
                # writes into the log file
                file.write(fail_msg + "\n")

            while not ping():
                # infinite loop,
                # will run till ping() return true
                time.sleep(1)

            up_time = datetime.datetime.now()
            
            # will execute after while true is
            # false (connection restored)
            uptime_message = "connected again: " + str(up_time).split(".")[0]

            down_time = calculate_time(down_time, up_time)
            
            # calling time calculating
            # function, printing down time
            unavailablity_time = "connection was unavailable for: " + down_time

            print(uptime_message)
            print(unavailablity_time)

            with open(FILE, "a") as file:
                
                # log entry for connected restoration time,
                # and unavailability time
                file.write(uptime_message + "\n")
                file.write(unavailablity_time + "\n")