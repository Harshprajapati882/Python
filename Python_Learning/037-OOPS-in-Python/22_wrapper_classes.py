# Wrapper Classes in Python

# --- The Original Object ---
# Imagine this class comes from a library and we cannot modify it.
class SimpleHttpClient:
    """A simple client for making web requests."""
    def __init__(self, base_url):
        self.base_url = base_url
        print("SimpleHttpClient initialized.")

    def get(self, endpoint):
        """Makes a GET request."""
        print(f"Making GET request to: {self.base_url}{endpoint}")
        # In a real scenario, this would involve network operations.
        return {"status": 200, "data": f"Response from {endpoint}"}

    def post(self, endpoint, data):
        """Makes a POST request."""
        print(f"Making POST request to: {self.base_url}{endpoint} with data: {data}")
        return {"status": 201, "message": "Created"}


# --- The Wrapper Class ---
# We want to add logging and caching to the HTTP client without changing its code.
import time

class EnhancedHttpClient:
    """
    A wrapper class that adds logging and caching to an HTTP client.
    """
    def __init__(self, http_client):
        # The wrapper holds a reference to the original object.
        self._wrapped_client = http_client
        self._cache = {}

    def get(self, endpoint):
        """
        Overrides the original 'get' method to add new functionality.
        """
        # 1. Add caching logic
        if endpoint in self._cache:
            timestamp, data = self._cache[endpoint]
            if time.time() - timestamp < 10: # Cache for 10 seconds
                print(f"LOG: Returning cached response for {endpoint}")
                return data
        
        # 2. Add logging before delegation
        print(f"LOG: Request initiated for {endpoint}")
        
        # 3. Delegate the actual call to the wrapped object
        response = self._wrapped_client.get(endpoint)
        
        # 4. Add logging after delegation
        print(f"LOG: Request completed for {endpoint} with status {response.get('status')}")
        
        # 5. Store the response in the cache
        self._cache[endpoint] = (time.time(), response)
        
        return response

    def __getattr__(self, name):
        """
        This is a special method that gets called for any attribute
        that is not found on the wrapper object itself.
        It makes the wrapper 'transparent' for all other methods/attributes.
        """
        print(f"LOG: Delegating call '{name}' to the wrapped client.")
        return getattr(self._wrapped_client, name)

# --- Usage ---

# 1. Create the original object
simple_client = SimpleHttpClient("https://api.example.com")

# 2. Wrap it with our EnhancedHttpClient to add functionality
enhanced_client = EnhancedHttpClient(simple_client)


# 3. Use the wrapper as if it were the original object

# Call the 'get' method (which is explicitly overridden in the wrapper)
print("\n--- Calling the overridden 'get' method ---")
response1 = enhanced_client.get("/users")
print("Response:", response1)

print("\n--- Calling 'get' again (should hit the cache) ---")
time.sleep(2)
response2 = enhanced_client.get("/users")
print("Response:", response2)


# Call the 'post' method (which is NOT defined in the wrapper)
# The __getattr__ method will be triggered to delegate the call.
print("\n--- Calling the delegated 'post' method ---")
response3 = enhanced_client.post("/users", data={"name": "Alice"})
print("Response:", response3)

# Access an attribute of the original object
print("\n--- Accessing a delegated attribute ---")
print(f"Base URL: {enhanced_client.base_url}")
