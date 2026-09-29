from network_utils import (
    get_ip_configuration,
    ping_host,
    dns_lookup,
    run_full_diagnostics,
)


def print_result(title, result):
    print(f"\n--- {title} ---")
    print(result)


def show_menu():
    print("\n========================================")
    print("     IT NETWORK TROUBLESHOOTING ASSISTANT")
    print("========================================")
    print("1. Check IP configuration")
    print("2. Test gateway / host with ping")
    print("3. Test DNS lookup")
    print("4. Run full diagnostics")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("\nEnter your choice (1-5): ").strip()

        try:

            if choice == "1":
                print_result(
                    "IP CONFIGURATION",
                    get_ip_configuration()
                )

            elif choice == "2":
                host = input(
                    "Enter host/IP to ping [8.8.8.8]: "
                ).strip()

                if not host:
                    host = "8.8.8.8"

                print_result(
                    "PING TEST",
                    ping_host(host)
                )

            elif choice == "3":
                host = input(
                    "Enter domain [google.com]: "
                ).strip()

                if not host:
                    host = "google.com"

                print_result(
                    "DNS LOOKUP",
                    dns_lookup(host)
                )

            elif choice == "4":
                print_result(
                    "FULL NETWORK DIAGNOSTICS",
                    run_full_diagnostics()
                )

            elif choice == "5":
                print(
                    "\nThank you for using the "
                    "IT Network Troubleshooting Assistant."
                )
                break

            else:
                print("\nInvalid choice. Please select 1-5.")

        except KeyboardInterrupt:
            print("\n\nProgram stopped by user.")
            break

        except Exception as error:
            print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
