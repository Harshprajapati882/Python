# Serialization in Python

## Table of Contents
1. [What is Serialization?](#what-is-serialization)
2. [Why Serialization?](#why-serialization)
3. [What is Deserialization?](#what-is-deserialization)
4. [Serialization Libraries](#serialization-libraries)
5. [Pickle Module](#pickle-module)
6. [JSON Module](#json-module)
7. [YAML Module](#yaml-module)
8. [Protocols](#protocols)
9. [Pickler and Unpickler Classes](#pickler-and-unpickler-classes)
10. [Serializing Objects](#serializing-objects)
11. [Deserializing Objects](#deserializing-objects)
12. [Custom Class Objects](#custom-class-objects)

---

## What is Serialization?

Serialization is the process of converting Python objects into a byte stream (binary format) or string representation that can be easily stored, transmitted, or written to a file. The serialized data is platform-independent and can be transferred over networks or stored in databases.

### Key Points:
- Converts complex data structures into simpler formats
- Makes data portable across different systems
- Enables persistent storage of object states
- Facilitates data transmission over networks

---

## Why Serialization?

### Reasons to Use Serialization:

1. **Data Persistence**: Save Python objects to files for later use
   - Save program state
   - Create checkpoints
   - Implement data caching

2. **Data Transmission**: Send Python objects over networks
   - API communication
   - Remote procedure calls (RPC)
   - Distributed systems

3. **Data Storage**: Store objects in databases
   - Document databases (MongoDB)
   - Cache systems (Redis)
   - SQL databases

4. **Interoperability**: Share data between different programs or languages
   - Python to JavaScript
   - Python to Java
   - Cross-platform compatibility

5. **Configuration Management**: Store configuration as serialized objects

6. **Logging and Debugging**: Record object states for analysis

---

## What is Deserialization?

Deserialization is the reverse process of serialization. It converts the serialized byte stream or string representation back into Python objects.

### Relationship:
```
Python Object → [Serialization] → Byte Stream/String → [Deserialization] → Python Object
```

---

## Serialization Libraries

Python provides multiple libraries for serialization, each with different use cases:

### 1. **Pickle**
- **Format**: Binary (native Python)
- **Python-only**: Yes
- **Security**: No (can execute arbitrary code)
- **Use Case**: Python-to-Python data transfer
- **Performance**: Fast
- **Pros**: Handles complex Python objects, compact
- **Cons**: Not human-readable, security risk

### 2. **JSON (JavaScript Object Notation)**
- **Format**: Text-based
- **Python-only**: No (language-independent)
- **Security**: Yes (safe)
- **Use Case**: Web APIs, data interchange
- **Performance**: Moderate
- **Pros**: Human-readable, wide language support, secure
- **Cons**: Doesn't support Python-specific types (datetime, custom objects)

### 3. **YAML (YAML Ain't Markup Language)**
- **Format**: Text-based, human-friendly
- **Python-only**: No (language-independent)
- **Security**: Depends on implementation
- **Use Case**: Configuration files, data exchange
- **Performance**: Slower
- **Pros**: Very human-readable, supports comments
- **Cons**: Slower than JSON, requires external library

---

## Pickle Module

### Overview
Pickle is Python's built-in serialization module. It converts Python objects into a byte stream.

### Protocols
Pickle has multiple protocols for different compatibility levels:

| Protocol | Python Version | Notes |
|----------|---|---|
| 0 | All | ASCII, human-readable, slow |
| 1 | 1.5+ | Old binary format |
| 2 | 2.3+ | Efficient binary format |
| 3 | 3.0+ | Binary format, bytes instead of strings |
| 4 | 3.4+ | Added support for very large objects |
| 5 | 3.8+ | Support for out-of-band data, faster |
| -1 | Current | Use the highest protocol in current Python version |

### Key Functions:
- `pickle.dumps()`: Serialize to bytes
- `pickle.dump()`: Serialize to file
- `pickle.loads()`: Deserialize from bytes
- `pickle.load()`: Deserialize from file

### Security Warning
⚠️ **NEVER unpickle untrusted data!** Pickle can execute arbitrary code during deserialization.

---

## JSON Module

### Overview
JSON is a text-based, language-independent serialization format. Python's `json` module provides JSON serialization.

### Key Functions:
- `json.dumps()`: Serialize to JSON string
- `json.dump()`: Serialize to file
- `json.loads()`: Deserialize from JSON string
- `json.load()`: Deserialize from file

### Supported Types:
| Python | JSON |
|--------|------|
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True | true |
| False | false |
| None | null |

### Unsupported Types:
- datetime objects
- Custom classes
- Sets
- Bytes objects

---

## YAML Module

### Overview
YAML is a human-friendly text-based format. Use the `PyYAML` library (install: `pip install pyyaml`).

### Key Functions:
- `yaml.dump()`: Serialize to YAML string
- `yaml.load()`: Deserialize from YAML string (⚠️ use `yaml.safe_load()`)
- `yaml.safe_load()`: Safe deserialization

### Advantages:
- Supports comments
- Easy to read and write
- Supports complex data structures

---

## Protocols

### What are Protocols in Pickle?

Pickle protocols determine how objects are serialized. They affect compatibility and efficiency:

- **Protocol 0**: ASCII format, readable but slow
- **Protocols 1-2**: Binary formats for Python 1.5+, 2.3+
- **Protocol 3**: Binary format for Python 3.0+
- **Protocol 4**: Added in Python 3.4, handles larger objects
- **Protocol 5**: Added in Python 3.8, out-of-band data support

### Choosing Protocol:
```python
pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)  # Best compatibility
pickle.dumps(obj, protocol=0)                        # Ensure old Python versions
pickle.dumps(obj, protocol=-1)                       # Use highest in current Python
```

---

## Pickler and Unpickler Classes

### Pickler Class
Writes pickled data to a file-like object.

```python
import pickle

data = {'name': 'Alice', 'age': 30}

# Using Pickler class
with open('data.pkl', 'wb') as f:
    pickler = pickle.Pickler(f, protocol=pickle.HIGHEST_PROTOCOL)
    pickler.dump(data)
```

### Unpickler Class
Reads pickled data from a file-like object.

```python
import pickle

# Using Unpickler class
with open('data.pkl', 'rb') as f:
    unpickler = pickle.Unpickler(f)
    data = unpickler.load()
    print(data)
```

### Advantages of Classes:
- More control over serialization
- Can handle custom persistence protocols
- Useful for streaming or incremental serialization

---

## Serializing Objects

### Serializing Simple Objects
```python
import pickle
import json

# Dictionary
data = {'name': 'Bob', 'age': 25, 'city': 'NYC'}

# Pickle
pickled = pickle.dumps(data)

# JSON
json_str = json.dumps(data)
```

### Serializing Complex Objects
Lists, tuples, nested structures all work with pickle and JSON.

---

## Deserializing Objects

### Deserializing from Bytes/Strings
```python
import pickle
import json

# Pickle
data = pickle.loads(pickled_bytes)

# JSON
data = json.loads(json_string)
```

### Deserializing from Files
```python
import pickle
import json

# Pickle from file
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

# JSON from file
with open('data.json', 'r') as f:
    data = json.load(f)
```

---

## Custom Class Objects

### Serializing Custom Objects

#### With Pickle (Automatic)
```python
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)
pickled = pickle.dumps(person)
restored = pickle.loads(pickled)
```

#### With JSON (Requires Custom Handling)
```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Need custom JSON encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

person = Person('Alice', 30)
json_str = json.dumps(person, cls=PersonEncoder)
```

### Deserializing Custom Objects

#### With Pickle
```python
pickled = pickle.dumps(person)
restored = pickle.loads(pickled)
# Works automatically if class is defined
```

#### With JSON
```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod
    def from_dict(data):
        return Person(data['name'], data['age'])

json_str = '{"name": "Alice", "age": 30}'
person = Person.from_dict(json.loads(json_str))
```

### Custom `__getstate__` and `__setstate__` (Pickle)

```python
import pickle

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self._password = 'secret123'
    
    def __getstate__(self):
        # Control what gets pickled
        state = self.__dict__.copy()
        del state['_password']  # Don't pickle password
        return state
    
    def __setstate__(self, state):
        # Control how object is restored
        self.__dict__.update(state)
        self._password = 'default_password'

account = BankAccount('12345', 1000)
pickled = pickle.dumps(account)
restored = pickle.loads(pickled)
```

---

## Comparison Table

| Feature | Pickle | JSON | YAML |
|---------|--------|------|------|
| Binary/Text | Binary | Text | Text |
| Human Readable | No | Yes | Yes |
| Python Only | Yes | No | No |
| Secure | No | Yes | Depends |
| Speed | Fast | Moderate | Slow |
| Custom Objects | Yes | No (need custom) | Limited |
| Type Support | Extensive | Limited | Good |
| File Size | Small | Moderate | Moderate |

---

## Best Practices

1. **Use `protocol=pickle.HIGHEST_PROTOCOL`** for performance
2. **Never unpickle untrusted data**
3. **Use JSON for data exchange** between different languages
4. **Use Pickle for Python-only** data storage
5. **Use YAML for configuration files**
6. **Always handle deserialize errors** properly
7. **Version your serialization** for backward compatibility
8. **Use `__getstate__`/`__setstate__`** to control what's serialized

---

## Security Considerations

### Pickle Risks:
- Can execute arbitrary Python code during unpickling
- Only unpickle data from trusted sources
- Alternative: Use `json` for untrusted data

### JSON Safety:
- Safe by default
- No code execution risk
- Limited in what can be serialized

### YAML Safety:
- Use `yaml.safe_load()` instead of `yaml.load()`
- `yaml.load()` can execute arbitrary code
