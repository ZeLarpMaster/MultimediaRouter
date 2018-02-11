from core import App


def main():
    app = App("config.json")
    command = "help"
    rest = ""
    while command != "quit":
        if command == "quit":
            pass
        elif command == "help":
            print("Commands:\nquit - Quits this application\nhelp - Shows this message\nrun - Execute the router\n"
                  "route add <extension> <destination> - Add a route\nroute del <extension> - Delete a route\n"
                  "bucket add <filepath> - Add a bucket\nbucket del <filepath> - Delete a bucket\n")
        elif command == "run":
            app.run()
        elif command == "route":
            args = rest.split(" ", 1)
            sub_cmd = args[0]
            if sub_cmd == "add":
                routes = args[-1].split(" ", 1)
                if len(routes) == 2:
                    app.add_route(routes[0], routes[1])
            elif sub_cmd == "del":
                app.remove_route(args[1])
        elif command == "bucket":
            args = rest.split(" ", 1)
            sub_cmd = args[0]
            if sub_cmd == "add":
                app.add_bucket(args[1])
            elif sub_cmd == "del":
                app.remove_bucket(args[1])
        raw_command = input("Enter your command: ").split(" ", 1)
        command = raw_command[0]
        rest = raw_command[-1]

if __name__ == "__main__":
    main()
