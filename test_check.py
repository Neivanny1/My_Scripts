import time
checks = range(20)

def print_and_sleep():
    print("Configuring environments....")
    time.sleep(7)
    print("Windows python envronment variable detected")
    passs = input("Do you wish to activate modules\n")
    print("WARNING")
    pin = input("Voice recognition disabled! Enter Pin to Activate\n")
    if pin == "Pammy2020":
        for check in checks:
            if check % 2 == 0:
                print(f"Test {check} passed sucessfully")
                print("Checking more tests")
                time.sleep(3)
            else:
                print(f"Test {check} failed")
                print(f"check log from log collector for more details")
    print("Checking Sucess rate")
    time.sleep(3)
    print("16/20 passed. Rate of 60%")
    print("Not compatible")
      
    print("Colleting logs...")
    time.sleep(4)
    print("Shutting......")
    time.sleep(5)  
    print('Done')
print_and_sleep()
