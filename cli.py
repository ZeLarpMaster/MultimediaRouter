from core import App


def main():
    app = App("config.json")
    command = "help"
    rest = ""
    while command != "quit":
        if command == "quit":
            pass
        elif command == "help":
            print("""Commands:
quit - Quits this application
help - Shows this message
run - Execute the router
route add <extension> <destination> - Add a route
route del <extension> - Delete a route
bucket add <filepath> - Add a bucket
bucket del <filepath> - Delete a bucket
copy - Sets the router in copy mode (file are copied from buckets to routes)
link - Sets the router in link mode (symbolic links between buckets and routes)
""")
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
        elif command == "copy":
            app.set_copy(True)
        elif command == "link":
            app.set_copy(False)
        raw_command = input("Enter your command: ").split(" ", 1)
        command = raw_command[0]
        rest = raw_command[-1]

if __name__ == "__main__":
    main()
