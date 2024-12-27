class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers  # List of available servers
        self.current_index = 0  # Keeps track of the current server

    def get_server(self):
        # Round-robin selection
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

    def handle_request(self, request):
        # Assign the request to a server
        server = self.get_server()
        print(f"Routing request '{request}' to server: {server}")


# Example usage
if __name__ == "__main__":
    # List of backend servers
    servers = ["Server1", "Server2", "Server3"]
    load_balancer = LoadBalancer(servers)

    # Simulate incoming requests
    requests = ["Request1", "Request2", "Request3", "Request4", "Request5"]

    for request in requests:
        load_balancer.handle_request(request)
