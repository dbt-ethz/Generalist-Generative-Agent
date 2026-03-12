import socket


def udp_listener(worker):
    # Define the address and port to listen on
    server_address = ("localhost", 12346)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set the socket option to reuse the address
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the server address
    sock.bind(server_address)

    worker.display_message("Listening for incoming UDP messages...")

    try:
        while True:
            # Check if worker has requested cancellation
            if worker.has_requested_cancellation():
                worker.display_message("Cancelling listener...")
                break

            # Receive message
            data, address = sock.recvfrom(
                65535
            )  # Buffer size max is 65535, typical is 4096 bytes
            message = data.decode()

            # Update the result with the received message
            worker.update_result(message)

            # Display the received message
            # worker.display_message("Received from %s:\n%s" % (str(address), message))
            worker.display_message("Received from %s" % (str(address)))

    except Exception as e:
        # Display the error message
        worker.display_message("Error: %s" % str(e))
        worker.update_result("Error: %s" % str(e))

    finally:
        # Ensure the socket is closed properly
        sock.close()
        worker.display_message("Listener stopped.")
