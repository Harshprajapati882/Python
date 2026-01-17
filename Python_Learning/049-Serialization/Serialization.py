"""
Serialization in Python
Comprehensive code examples demonstrating serialization and deserialization
"""

import pickle
import json
import yaml
from datetime import datetime
from pathlib import Path
from io import BytesIO


# ============================================================================
# 1. PICKLE BASICS
# ============================================================================

print("=" * 70)
print("1. PICKLE BASICS")
print("=" * 70)

# Simple serialization with pickle.dumps() and pickle.loads()
def pickle_basics():
    """Basic pickle serialization and deserialization"""
    print("\n--- Pickle: dumps() and loads() ---")
    
    # Data to serialize
    data = {
        'name': 'Alice',
        'age': 30,
        'scores': [95, 87, 92],
        'active': True
    }
    
    # Serialize to bytes
    pickled = pickle.dumps(data)
    print(f"Original data: {data}")
    print(f"Pickled (bytes): {pickled[:50]}...")  # Show first 50 bytes
    print(f"Pickled size: {len(pickled)} bytes")
    
    # Deserialize from bytes
    restored = pickle.loads(pickled)
    print(f"Restored data: {restored}")
    print(f"Data intact: {data == restored}")
    
    return restored


pickle_basics()


# ============================================================================
# 2. PICKLE WITH FILES
# ============================================================================

print("\n" + "=" * 70)
print("2. PICKLE WITH FILES")
print("=" * 70)

def pickle_file_operations():
    """Serialize and deserialize using files"""
    print("\n--- Pickle: dump() and load() ---")
    
    student = {
        'id': 101,
        'name': 'Bob Johnson',
        'grades': [85, 90, 78, 92],
        'gpa': 3.86
    }
    
    filename = '/tmp/student.pkl'
    
    # Write to file
    with open(filename, 'wb') as f:
        pickle.dump(student, f)
    print(f"Serialized to {filename}")
    
    # Read from file
    with open(filename, 'rb') as f:
        loaded_student = pickle.load(f)
    print(f"Deserialized from file: {loaded_student}")
    print(f"Data preserved: {student == loaded_student}")


pickle_file_operations()


# ============================================================================
# 3. PICKLE PROTOCOLS
# ============================================================================

print("\n" + "=" * 70)
print("3. PICKLE PROTOCOLS")
print("=" * 70)

def pickle_protocols():
    """Demonstrate different pickle protocols"""
    print("\n--- Pickle Protocols ---")
    
    data = {'name': 'Charlie', 'scores': [100, 95, 98]}
    
    protocols = [0, 1, 2, 3, 4, pickle.HIGHEST_PROTOCOL]
    
    for protocol in protocols:
        pickled = pickle.dumps(data, protocol=protocol)
        print(f"Protocol {protocol}: {len(pickled)} bytes")
    
    # HIGHEST_PROTOCOL is most efficient
    print(f"\nHighest protocol ({pickle.HIGHEST_PROTOCOL}): Best efficiency")
    print(f"Protocol 0: Best compatibility with old Python versions")


pickle_protocols()


# ============================================================================
# 4. PICKLER AND UNPICKLER CLASSES
# ============================================================================

print("\n" + "=" * 70)
print("4. PICKLER AND UNPICKLER CLASSES")
print("=" * 70)

def pickler_unpickler_classes():
    """Using Pickler and Unpickler classes for more control"""
    print("\n--- Pickler Class ---")
    
    data1 = {'user': 'Dave', 'level': 5}
    data2 = {'item': 'sword', 'damage': 15}
    data3 = [1, 2, 3, 4, 5]
    
    filename = '/tmp/multiple.pkl'
    
    # Using Pickler to write multiple objects
    with open(filename, 'wb') as f:
        pickler = pickle.Pickler(f, protocol=pickle.HIGHEST_PROTOCOL)
        pickler.dump(data1)
        pickler.dump(data2)
        pickler.dump(data3)
    print("Wrote 3 objects using Pickler class")
    
    print("\n--- Unpickler Class ---")
    
    # Using Unpickler to read multiple objects
    with open(filename, 'rb') as f:
        unpickler = pickle.Unpickler(f)
        obj1 = unpickler.load()
        obj2 = unpickler.load()
        obj3 = unpickler.load()
    
    print(f"Object 1: {obj1}")
    print(f"Object 2: {obj2}")
    print(f"Object 3: {obj3}")


pickler_unpickler_classes()


# ============================================================================
# 5. JSON BASICS
# ============================================================================

print("\n" + "=" * 70)
print("5. JSON BASICS")
print("=" * 70)

def json_basics():
    """Basic JSON serialization and deserialization"""
    print("\n--- JSON: dumps() and loads() ---")
    
    config = {
        'host': 'localhost',
        'port': 8080,
        'debug': True,
        'allowed_ips': ['127.0.0.1', '192.168.1.1'],
        'timeout': 30.5
    }
    
    # Serialize to JSON string
    json_string = json.dumps(config, indent=2)
    print("Original config:")
    print(json_string)
    
    # Deserialize from JSON string
    restored = json.loads(json_string)
    print(f"\nRestored config: {restored}")
    print(f"Data intact: {config == restored}")


json_basics()


# ============================================================================
# 6. JSON WITH FILES
# ============================================================================

print("\n" + "=" * 70)
print("6. JSON WITH FILES")
print("=" * 70)

def json_file_operations():
    """Serialize and deserialize JSON using files"""
    print("\n--- JSON: dump() and load() ---")
    
    api_response = {
        'status': 'success',
        'code': 200,
        'data': {
            'total': 100,
            'items': [
                {'id': 1, 'name': 'Item 1'},
                {'id': 2, 'name': 'Item 2'}
            ]
        }
    }
    
    filename = '/tmp/api_response.json'
    
    # Write to file
    with open(filename, 'w') as f:
        json.dump(api_response, f, indent=2)
    print(f"Serialized to {filename}")
    
    # Read from file
    with open(filename, 'r') as f:
        loaded = json.load(f)
    print(f"Deserialized: {loaded}")


json_file_operations()


# ============================================================================
# 7. JSON TYPE MAPPING
# ============================================================================

print("\n" + "=" * 70)
print("7. JSON TYPE MAPPING")
print("=" * 70)

def json_type_mapping():
    """Show Python to JSON type mapping"""
    print("\n--- Python to JSON Type Mapping ---")
    
    data = {
        'string': 'hello',
        'integer': 42,
        'float': 3.14,
        'boolean_true': True,
        'boolean_false': False,
        'none_value': None,
        'list': [1, 2, 3],
        'dict': {'nested': 'value'}
    }
    
    json_str = json.dumps(data, indent=2)
    print("Python object converted to JSON:")
    print(json_str)
    
    # Show types are preserved correctly
    restored = json.loads(json_str)
    print("\nType verification:")
    print(f"String: {type(restored['string']).__name__}")
    print(f"Integer: {type(restored['integer']).__name__}")
    print(f"Float: {type(restored['float']).__name__}")
    print(f"Boolean: {type(restored['boolean_true']).__name__}")
    print(f"None: {type(restored['none_value']).__name__}")
    print(f"List: {type(restored['list']).__name__}")
    print(f"Dict: {type(restored['dict']).__name__}")


json_type_mapping()


# ============================================================================
# 8. CUSTOM JSON ENCODER
# ============================================================================

print("\n" + "=" * 70)
print("8. CUSTOM JSON ENCODER")
print("=" * 70)

class Person:
    """Example class for JSON encoding"""
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"


class PersonEncoder(json.JSONEncoder):
    """Custom encoder for Person objects"""
    def default(self, obj):
        if isinstance(obj, Person):
            return {
                '__person__': True,
                'name': obj.name,
                'age': obj.age,
                'email': obj.email
            }
        return super().default(obj)


def custom_json_encoder():
    """Use custom encoder for custom classes"""
    print("\n--- Custom JSON Encoder ---")
    
    people = [
        Person('Alice', 30, 'alice@example.com'),
        Person('Bob', 25, 'bob@example.com')
    ]
    
    # Encode with custom encoder
    json_str = json.dumps(people, cls=PersonEncoder, indent=2)
    print("Encoded people:")
    print(json_str)


custom_json_encoder()


# ============================================================================
# 9. CUSTOM JSON DECODER
# ============================================================================

print("\n" + "=" * 70)
print("9. CUSTOM JSON DECODER")
print("=" * 70)

def person_decoder(dct):
    """Custom decoder function for Person objects"""
    if '__person__' in dct:
        return Person(dct['name'], dct['age'], dct['email'])
    return dct


def custom_json_decoder():
    """Use custom decoder to restore custom classes"""
    print("\n--- Custom JSON Decoder ---")
    
    json_str = '''[
        {
            "__person__": true,
            "name": "Charlie",
            "age": 35,
            "email": "charlie@example.com"
        },
        {
            "__person__": true,
            "name": "Diana",
            "age": 28,
            "email": "diana@example.com"
        }
    ]'''
    
    people = json.loads(json_str, object_hook=person_decoder)
    print("Decoded people:")
    for person in people:
        print(f"  {person}")


custom_json_decoder()


# ============================================================================
# 10. PICKLE WITH CUSTOM CLASSES
# ============================================================================

print("\n" + "=" * 70)
print("10. PICKLE WITH CUSTOM CLASSES")
print("=" * 70)

class BankAccount:
    """Example class with sensitive data"""
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self._pin = '1234'  # Sensitive data
    
    def __repr__(self):
        return f"BankAccount({self.account_number}, {self.owner}, ${self.balance})"


def pickle_custom_classes():
    """Pickle custom class instances"""
    print("\n--- Pickle Custom Classes ---")
    
    account = BankAccount('ACC-001', 'Eve', 5000.00)
    print(f"Original: {account}")
    print(f"PIN: {account._pin}")
    
    # Pickle the account
    pickled = pickle.dumps(account)
    print(f"Pickled size: {len(pickled)} bytes")
    
    # Unpickle
    restored = pickle.loads(pickled)
    print(f"Restored: {restored}")
    print(f"PIN preserved: {restored._pin}")


pickle_custom_classes()


# ============================================================================
# 11. GETSTATE AND SETSTATE
# ============================================================================

print("\n" + "=" * 70)
print("11. __getstate__ AND __setstate__")
print("=" * 70)

class SecureBankAccount:
    """Bank account with custom pickling (don't pickle PIN)"""
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self._pin = '1234'
        self._created = datetime.now()
    
    def __getstate__(self):
        """Control what gets pickled"""
        state = self.__dict__.copy()
        # Don't pickle sensitive data
        del state['_pin']
        return state
    
    def __setstate__(self, state):
        """Control how object is restored"""
        self.__dict__.update(state)
        # Restore PIN to default
        self._pin = '0000'
    
    def __repr__(self):
        return f"SecureBankAccount({self.account_number}, {self.owner}, ${self.balance})"


def getstate_setstate_demo():
    """Demonstrate __getstate__ and __setstate__"""
    print("\n--- __getstate__ and __setstate__ ---")
    
    account = SecureBankAccount('ACC-002', 'Frank', 10000.00)
    print(f"Original account: {account}")
    print(f"Original PIN: {account._pin}")
    
    # Pickle and unpickle
    pickled = pickle.dumps(account)
    restored = pickle.loads(pickled)
    
    print(f"\nRestored account: {restored}")
    print(f"Restored PIN (default): {restored._pin}")
    print(f"Created timestamp: {restored._created}")


getstate_setstate_demo()


# ============================================================================
# 12. YAML BASIC OPERATIONS
# ============================================================================

print("\n" + "=" * 70)
print("12. YAML BASIC OPERATIONS")
print("=" * 70)

def yaml_operations():
    """Basic YAML serialization"""
    print("\n--- YAML Serialization ---")
    
    config = {
        'application': 'MyApp',
        'version': '1.0.0',
        'server': {
            'host': 'localhost',
            'port': 8080,
            'debug': True
        },
        'database': {
            'engine': 'postgresql',
            'user': 'admin',
            'password': 'secret'
        },
        'features': ['auth', 'api', 'caching']
    }
    
    # Serialize to YAML
    yaml_str = yaml.dump(config, default_flow_style=False)
    print("YAML representation:")
    print(yaml_str)
    
    # Deserialize from YAML
    restored = yaml.safe_load(yaml_str)
    print("Restored config:", restored)


yaml_operations()


# ============================================================================
# 13. YAML FILE OPERATIONS
# ============================================================================

print("\n" + "=" * 70)
print("13. YAML FILE OPERATIONS")
print("=" * 70)

def yaml_file_operations():
    """YAML with files"""
    print("\n--- YAML File Operations ---")
    
    data = {
        'users': [
            {'id': 1, 'name': 'George', 'role': 'admin'},
            {'id': 2, 'name': 'Hannah', 'role': 'user'}
        ],
        'settings': {
            'theme': 'dark',
            'language': 'en'
        }
    }
    
    filename = '/tmp/config.yaml'
    
    # Write to file
    with open(filename, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
    print(f"Saved to {filename}")
    
    # Read from file
    with open(filename, 'r') as f:
        loaded = yaml.safe_load(f)
    print(f"Loaded: {loaded}")


yaml_file_operations()


# ============================================================================
# 14. COMPARISON: PICKLE VS JSON VS YAML
# ============================================================================

print("\n" + "=" * 70)
print("14. COMPARISON: PICKLE VS JSON VS YAML")
print("=" * 70)

def serialization_comparison():
    """Compare serialization methods"""
    print("\n--- Serialization Comparison ---")
    
    data = {
        'name': 'Isaac',
        'scores': [90, 85, 95],
        'active': True
    }
    
    # Pickle
    pickled = pickle.dumps(data)
    print(f"Pickle: {len(pickled)} bytes")
    print(f"  Bytes: {pickled[:50]}...")
    
    # JSON
    json_str = json.dumps(data)
    print(f"\nJSON: {len(json_str)} bytes")
    print(f"  String: {json_str}")
    
    # YAML
    yaml_str = yaml.dump(data)
    print(f"\nYAML: {len(yaml_str)} bytes")
    print(f"  String: {yaml_str}")
    
    print("\nComparison:")
    print(f"  Pickle is binary and compact")
    print(f"  JSON is text-based and interoperable")
    print(f"  YAML is human-friendly and readable")


serialization_comparison()


# ============================================================================
# 15. SERIALIZATION WITH ERROR HANDLING
# ============================================================================

print("\n" + "=" * 70)
print("15. SERIALIZATION WITH ERROR HANDLING")
print("=" * 70)

def serialization_with_error_handling():
    """Handle serialization errors gracefully"""
    print("\n--- Error Handling ---")
    
    # 1. JSON doesn't support datetime
    print("\n1. JSON with datetime (will fail):")
    try:
        data_with_datetime = {'timestamp': datetime.now()}
        json.dumps(data_with_datetime)
    except TypeError as e:
        print(f"   Error: {e}")
        print("   Solution: Convert datetime to string first")
        data = {'timestamp': datetime.now().isoformat()}
        print(f"   Fixed: {json.dumps(data)}")
    
    # 2. Pickle with untrusted data
    print("\n2. Safe unpickling:")
    print("   Warning: Never unpickle untrusted data!")
    print("   Use json.loads() or yaml.safe_load() for untrusted data")
    
    # 3. File not found
    print("\n3. File operations with error handling:")
    try:
        with open('/tmp/nonexistent.json', 'r') as f:
            json.load(f)
    except FileNotFoundError as e:
        print(f"   Error: {e}")


serialization_with_error_handling()


# ============================================================================
# 16. PRACTICAL EXAMPLE: SAVING GAME STATE
# ============================================================================

print("\n" + "=" * 70)
print("16. PRACTICAL EXAMPLE: SAVING GAME STATE")
print("=" * 70)

class GameState:
    """Game state for saving/loading"""
    def __init__(self, player_name, level, score, inventory):
        self.player_name = player_name
        self.level = level
        self.score = score
        self.inventory = inventory
        self.saved_at = datetime.now()
    
    def __repr__(self):
        return (f"GameState(player='{self.player_name}', level={self.level}, "
                f"score={self.score})")


def game_save_load_example():
    """Save and load game state"""
    print("\n--- Game State Save/Load ---")
    
    # Create game state
    game = GameState(
        player_name='Jack',
        level=5,
        score=2500,
        inventory=['sword', 'shield', 'potion', 'map']
    )
    print(f"Current game state: {game}")
    
    # Save using pickle
    save_file = '/tmp/gamesave.pkl'
    with open(save_file, 'wb') as f:
        pickle.dump(game, f)
    print(f"Game saved to {save_file}")
    
    # Load game
    with open(save_file, 'rb') as f:
        loaded_game = pickle.load(f)
    print(f"Game loaded: {loaded_game}")
    print(f"Inventory: {loaded_game.inventory}")


game_save_load_example()


# ============================================================================
# 17. PRACTICAL EXAMPLE: API RESPONSE HANDLING
# ============================================================================

print("\n" + "=" * 70)
print("17. PRACTICAL EXAMPLE: API RESPONSE HANDLING")
print("=" * 70)

def api_response_example():
    """Handle API responses with JSON"""
    print("\n--- API Response Handling ---")
    
    # Simulated API response
    api_response = '''
    {
        "status": "success",
        "data": {
            "user_id": 12345,
            "username": "kate_user",
            "email": "kate@example.com",
            "profile": {
                "first_name": "Kate",
                "last_name": "Smith",
                "bio": "Python developer"
            },
            "posts": [
                {"id": 1, "title": "Hello World", "likes": 42},
                {"id": 2, "title": "Python Tips", "likes": 89}
            ]
        }
    }
    '''
    
    # Parse JSON response
    response = json.loads(api_response)
    
    print("API Response parsed:")
    print(f"Status: {response['status']}")
    print(f"User: {response['data']['profile']['first_name']} {response['data']['profile']['last_name']}")
    print(f"Posts:")
    for post in response['data']['posts']:
        print(f"  - {post['title']} ({post['likes']} likes)")


api_response_example()


# ============================================================================
# 18. PRACTICAL EXAMPLE: CONFIGURATION FILES
# ============================================================================

print("\n" + "=" * 70)
print("18. PRACTICAL EXAMPLE: CONFIGURATION FILES")
print("=" * 70)

def configuration_example():
    """Use YAML for configuration files"""
    print("\n--- Configuration File Example ---")
    
    app_config = {
        'app': {
            'name': 'MyApplication',
            'version': '2.0.0',
            'debug': True
        },
        'server': {
            'host': 'localhost',
            'port': 8000,
            'workers': 4
        },
        'database': {
            'url': 'postgresql://localhost/myapp',
            'pool_size': 10,
            'echo': False
        },
        'logging': {
            'level': 'INFO',
            'file': '/var/log/myapp.log'
        }
    }
    
    # Save configuration
    config_file = '/tmp/app_config.yaml'
    with open(config_file, 'w') as f:
        yaml.dump(app_config, f, default_flow_style=False)
    print(f"Configuration saved to {config_file}")
    
    # Load configuration
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    print(f"\nLoaded configuration:")
    print(f"  App: {config['app']['name']} v{config['app']['version']}")
    print(f"  Server: {config['server']['host']}:{config['server']['port']}")
    print(f"  Database: {config['database']['url']}")


configuration_example()


# ============================================================================
# 19. STREAMS AND BUFFERS
# ============================================================================

print("\n" + "=" * 70)
print("19. STREAMS AND BUFFERS")
print("=" * 70)

def stream_example():
    """Serialize to memory buffers"""
    print("\n--- Serialization to Memory Buffers ---")
    
    data = {'message': 'Hello', 'count': 42}
    
    # Pickle to BytesIO
    buffer = BytesIO()
    pickle.dump(data, buffer)
    pickled_bytes = buffer.getvalue()
    print(f"Pickled to buffer: {len(pickled_bytes)} bytes")
    
    # Unpickle from BytesIO
    buffer = BytesIO(pickled_bytes)
    restored = pickle.load(buffer)
    print(f"Restored from buffer: {restored}")


stream_example()


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 70)
print("SERIALIZATION SUMMARY")
print("=" * 70)
print("""
Key Takeaways:
1. Pickle: Python-only, binary, fast, comprehensive - use for local storage
2. JSON: Universal, text, safe, limited types - use for APIs and web
3. YAML: Human-friendly, configuration, requires external lib - use for config files

Methods:
- pickle.dumps()/loads() - bytes in memory
- pickle.dump()/load() - file operations
- json.dumps()/loads() - JSON string in memory
- json.dump()/load() - file operations
- yaml.dump()/safe_load() - YAML operations

Security:
- Never unpickle untrusted data
- Use json or yaml.safe_load() for untrusted sources
- Use __getstate__/__setstate__ to control what's pickled

Use Cases:
- Caching: pickle (fast) or json (portable)
- APIs: json (standard)
- Configuration: yaml (human-readable)
- Game saves: pickle (complete state)
- Logs: json (structured)
""")
