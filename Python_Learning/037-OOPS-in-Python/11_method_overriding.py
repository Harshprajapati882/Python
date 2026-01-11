# Method Overriding in Python

# --- Superclass ---
class Document:
    def __init__(self, content):
        self.content = content

    def get_info(self):
        """Returns basic information about the document."""
        return f"This is a generic document with {len(self.content)} characters."

    def save(self):
        print(f"Saving the document content: '{self.content[:20]}...'")

# --- Subclass 1 ---
class WordDocument(Document):
    def __init__(self, content, author):
        super().__init__(content)
        self.author = author

    # Overriding the get_info method
    def get_info(self):
        """Provides specific information for a Word document."""
        return f"Word document by {self.author}, containing {len(self.content)} characters."

# --- Subclass 2 ---
class PdfDocument(Document):
    def __init__(self, content, is_encrypted):
        super().__init__(content)
        self.is_encrypted = is_encrypted

    # Overriding the get_info method and extending it
    def get_info(self):
        """Extends the parent's get_info method with new details."""
        # Call the parent's method first
        parent_info = super().get_info()
        encryption_status = "Encrypted" if self.is_encrypted else "Not Encrypted"
        return f"{parent_info}\nStatus: {encryption_status}"

    # Overriding the save method completely
    def save(self):
        """Provides a completely different implementation for saving."""
        if self.is_encrypted:
            print("Encrypting and then saving the PDF document.")
        else:
            print("Saving the PDF document.")


# --- Using the classes ---

# Create instances of each class
doc_generic = Document("This is a very long piece of text for a generic file.")
doc_word = WordDocument("This is the report for Q4.", "Alice")
doc_pdf = PdfDocument("Project Phoenix specifications.", True)

# Create a list of the documents
documents = [doc_generic, doc_word, doc_pdf]

print("--- Displaying Info (Polymorphism in action) ---")
for doc in documents:
    # The correct get_info() method is called for each object
    print(doc.get_info())
    print("--------------------")
# Output:
# --- Displaying Info (Polymorphism in action) ---
# This is a generic document with 51 characters.
# --------------------
# Word document by Alice, containing 24 characters.
# --------------------
# This is a generic document with 31 characters.
# Status: Encrypted
# --------------------


print("\n--- Saving Documents ---")
for doc in documents:
    # The correct save() method is called for each object
    doc.save()
# Output:
# --- Saving Documents ---
# Saving the document content: 'This is a very long ...'
# Saving the document content: 'This is the report f...'
# Encrypting and then saving the PDF document.
