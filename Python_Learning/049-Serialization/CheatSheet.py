"""
Serialization Cheat Sheet - Quick Reference
"""

# ============================================================================
# PICKLE CHEAT SHEET
# ============================================================================

"""
PICKLE - Python's binary serialization format

Best for: Python-only projects, fast serialization, complex objects
Protocols: 0-5 (higher = newer Python versions, faster)

Basic Usage:
    import pickle
    
    # Serialize
    bytes_data = pickle.dumps(obj)                    # To bytes
    pickle.dump(obj, file)                            # To file
    
    # Deserialize
    obj = pickle.loads(bytes_data)                    # From bytes
    obj = pickle.load(file)                           # From file
    
    # With protocol
    pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)

Classes:
    pickler = pickle.Pickler(file)
    pickler.dump(obj1)
    pickler.dump(obj2)
    
    unpickler = pickle.Unpickler(file)
    obj1 = unpickler.load()
    obj2 = unpickler.load()

Custom Classes:
    class MyClass:
        def __getstate__(self):
            # Control what gets pickled
            state = self.__dict__.copy()
            return state
        
        def __setstate__(self, state):
            # Control restoration
            self.__dict__.update(state)

SECURITY: ⚠️ Never unpickle untrusted data!
"""

# ============================================================================
# JSON CHEAT SHEET
# ============================================================================

"""
JSON - JavaScript Object Notation (universal text format)

Best for: Web APIs, data interchange, untrusted sources
Type Support: dict, list, str, int, float, bool, None

Basic Usage:
    import json
    
    # Serialize
    json_str = json.dumps(obj, indent=2)              # To string
    json.dump(obj, file, indent=2)                    # To file
    
    # Deserialize
    obj = json.loads(json_str)                        # From string
    obj = json.load(file)                             # From file

Type Mapping:
    Python          JSON
    ------          ----
    dict      →     object
    list      →     array
    str       →     string
    int       →     number
    float     →     number
    True      →     true
    False     →     false
    None      →     null

Custom Classes:
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, CustomClass):
                return {'__custom__': True, 'data': obj.data}
            return super().default(obj)
    
    json.dumps(obj, cls=CustomEncoder)

    def custom_decoder(dct):
        if '__custom__' in dct:
            return CustomClass(dct['data'])
        return dct
    
    json.loads(json_str, object_hook=custom_decoder)

Limitations:
    - No datetime support (convert to string)
    - No custom class support (use encoder/decoder)
    - No set support (convert to list)

SECURITY: ✓ Safe by default!
"""

# ============================================================================
# YAML CHEAT SHEET
# ============================================================================

"""
YAML - Human-friendly markup language

Best for: Configuration files, readable serialization
Install: pip install pyyaml

Basic Usage:
    import yaml
    
    # Serialize
    yaml_str = yaml.dump(obj, default_flow_style=False)
    yaml.dump(obj, file, default_flow_style=False)
    
    # Deserialize (SAFE)
    obj = yaml.safe_load(yaml_str)                    # Preferred!
    obj = yaml.safe_load(file)
    
    # Deserialize (UNSAFE - never with untrusted data)
    obj = yaml.load(yaml_str)                         # ⚠️ Dangerous!

Advantages:
    - Comments support (# comment)
    - Human-readable
    - Supports complex structures
    - Key-value pairs
    - Lists and nested objects

Example YAML:
    # This is a comment
    app:
      name: MyApp
      version: 1.0.0
    server:
      host: localhost
      port: 8080
    features:
      - auth
      - api
      - caching

SECURITY: ✓ Use yaml.safe_load() for untrusted data!
"""

# ============================================================================
# COMPARISON QUICK TABLE
# ============================================================================

"""
Comparison Summary:

Feature          Pickle    JSON      YAML
-----------      ------    ----      ----
Format           Binary    Text      Text
Human Readable   No        Yes       Yes
Language         Python    Universal Universal
Safe Default     No        Yes       Yes
Speed            Fast      Medium    Slow
Size             Small     Medium    Medium
Complex Types    Yes       Limited   Good
Python Objects   Yes       No        Limited
Date/Time        Yes       No        Limited
Streams          Yes       Limited   Yes

Use Cases:
  Pickle → Game saves, caching, local persistence
  JSON   → APIs, web services, data exchange
  YAML   → Config files, readable data
"""

# ============================================================================
# METHODS QUICK REFERENCE
# ============================================================================

"""
In-Memory Operations:
    pickle.dumps(obj) → bytes
    pickle.loads(bytes) → obj
    
    json.dumps(obj) → str
    json.loads(str) → obj
    
    yaml.dump(obj) → str
    yaml.safe_load(str) → obj

File Operations:
    pickle.dump(obj, file)
    pickle.load(file) → obj
    
    json.dump(obj, file)
    json.load(file) → obj
    
    yaml.dump(obj, file)
    yaml.safe_load(file) → obj

Special Classes:
    Pickler(file).dump(obj)
    Unpickler(file).load() → obj
    
    json.JSONEncoder
    json.JSONDecoder

Parameters:
    pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    json.dumps(obj, indent=2, sort_keys=True)
    yaml.dump(obj, default_flow_style=False)
"""

# ============================================================================
# ERROR HANDLING PATTERNS
# ============================================================================

"""
Safe Pickle Usage:
    try:
        with open('data.pkl', 'rb') as f:
            obj = pickle.load(f)
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"Error: {e}")

Safe JSON Usage:
    try:
        with open('data.json', 'r') as f:
            obj = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error: {e}")

Safe YAML Usage:
    try:
        with open('data.yaml', 'r') as f:
            obj = yaml.safe_load(f)
    except (yaml.YAMLError, FileNotFoundError) as e:
        print(f"Error: {e}")

Datetime Handling in JSON:
    # Convert to ISO format
    data = {'timestamp': datetime.now().isoformat()}
    json.dumps(data)
    
    # Parse back
    data = json.loads(json_str)
    timestamp = datetime.fromisoformat(data['timestamp'])
"""

# ============================================================================
# DECISION TREE
# ============================================================================

"""
Choose Your Serialization Format:

1. Do you need cross-language support?
   ├─ Yes → Use JSON (or YAML if config file)
   └─ No → Go to step 2

2. Is data from untrusted sources?
   ├─ Yes → Use JSON (never pickle!)
   └─ No → Go to step 3

3. Do you need maximum performance?
   ├─ Yes → Use Pickle
   └─ No → Go to step 4

4. Does it need to be human-readable?
   ├─ Yes → Use YAML
   └─ No → Use Pickle or JSON

5. Is this a config file?
   └─ Yes → Use YAML
   └─ No → Use Pickle or JSON
"""

# ============================================================================
# COMPLETE EXAMPLE
# ============================================================================

"""
Real-world example with all three formats:

import pickle
import json
import yaml
from pathlib import Path

class Config:
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings

# Create data
config = {
    'app_name': 'MyApp',
    'version': '1.0.0',
    'settings': {
        'debug': True,
        'port': 8080,
        'features': ['auth', 'api']
    }
}

# Save with Pickle
with open('config.pkl', 'wb') as f:
    pickle.dump(config, f, protocol=pickle.HIGHEST_PROTOCOL)

# Save with JSON
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

# Save with YAML
with open('config.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

# Load with Pickle
with open('config.pkl', 'rb') as f:
    cfg1 = pickle.load(f)

# Load with JSON
with open('config.json', 'r') as f:
    cfg2 = json.load(f)

# Load with YAML (SAFE)
with open('config.yaml', 'r') as f:
    cfg3 = yaml.safe_load(f)

print(cfg1 == cfg2 == cfg3)  # True
"""

print("✓ Serialization Cheat Sheet loaded!")
print("See source code for quick reference on:")
print("  - Pickle, JSON, and YAML usage")
print("  - Method reference for each format")
print("  - Error handling patterns")
print("  - Decision tree for choosing formats")
print("  - Complete working example")
