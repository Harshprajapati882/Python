# Serialization in Python

## Overview
Serialization is the process of converting Python objects into a format that can be stored or transmitted (bytes or strings), and deserialization is the reverse process.

## Files in This Directory

- **Serialization.md** - Comprehensive notes on serialization concepts, libraries, and best practices
- **Serialization.py** - Practical code examples demonstrating all serialization techniques

## Quick Start

### Run the Examples
```bash
python Serialization.py
```

This will run 19 different examples covering:
1. Pickle basics (dumps/loads)
2. Pickle with files (dump/load)
3. Pickle protocols
4. Pickler and Unpickler classes
5. JSON basics
6. JSON with files
7. JSON type mapping
8. Custom JSON encoders
9. Custom JSON decoders
10. Pickle with custom classes
11. `__getstate__` and `__setstate__` methods
12. YAML basics
13. YAML file operations
14. Comparison of all methods
15. Error handling
16. Game state save/load example
17. API response handling example
18. Configuration file example
19. Stream and buffer operations

## Key Concepts

### Serialization Methods

#### Pickle (Python-only)
```python
import pickle

# To bytes
data_bytes = pickle.dumps(obj)

# From bytes
obj = pickle.loads(data_bytes)

# To file
pickle.dump(obj, file)

# From file
obj = pickle.load(file)
```

#### JSON (Universal)
```python
import json

# To string
json_str = json.dumps(obj)

# From string
obj = json.loads(json_str)

# To file
json.dump(obj, file)

# From file
obj = json.load(file)
```

#### YAML (Human-friendly)
```python
import yaml

# To string
yaml_str = yaml.dump(obj)

# From string (safe)
obj = yaml.safe_load(yaml_str)

# To file
yaml.dump(obj, file)

# From file (safe)
obj = yaml.safe_load(file)
```

### When to Use What?

| Use Case | Best Choice | Reason |
|----------|-------------|--------|
| Python-only projects | Pickle | Comprehensive support, fast |
| Web APIs | JSON | Language-independent standard |
| Configuration files | YAML | Human-readable, supports comments |
| Caching | Pickle | Speed and completeness |
| Data exchange | JSON | Universal compatibility |
| Untrusted data | JSON or YAML | Safe by default (not pickle) |

## Important Security Notes

⚠️ **WARNING**: Never unpickle untrusted data!
- Pickle can execute arbitrary Python code
- Always use JSON or `yaml.safe_load()` for untrusted sources
- Validate data before deserializing

## Custom Class Serialization

### With Pickle (Automatic)
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)
pickled = pickle.dumps(person)
restored = pickle.loads(pickled)
```

### With JSON (Custom Encoder/Decoder)
```python
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

json_str = json.dumps(person, cls=PersonEncoder)
```

### Controlling Pickle Behavior
```python
class SecureClass:
    def __getstate__(self):
        # Control what gets pickled
        state = self.__dict__.copy()
        del state['_sensitive_data']
        return state
    
    def __setstate__(self, state):
        # Control how object is restored
        self.__dict__.update(state)
        self._sensitive_data = None
```

## Examples Covered

### Basic Operations
- Serializing and deserializing simple objects
- File-based operations
- Error handling

### Advanced Topics
- Pickle protocols and performance
- Pickler/Unpickler classes
- Custom JSON encoders/decoders
- `__getstate__` and `__setstate__` methods
- Stream and buffer operations

### Real-World Applications
- Game state saving
- API response handling
- Configuration files
- Data caching

## Performance Considerations

1. **Pickle**: Fastest, smallest size, Python-only
2. **JSON**: Medium speed, medium size, universal
3. **YAML**: Slowest, human-readable, good for config

Choose based on your priority: speed, compatibility, or readability.

## Related Topics
- Object serialization
- Persistence patterns
- Data interchange formats
- Configuration management
- API design

## Additional Resources

See `Serialization.md` for:
- Detailed explanations of each concept
- Complete protocol reference
- Security best practices
- Comprehensive comparison tables
