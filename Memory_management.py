import gc  # We will use this to manually trigger garbage collection
import sys  # To check the memory usage of objects

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

# 1. **Memory Allocation**: Create some objects
product1 = Product("Apple", 1.20, 100)
product2 = Product("Banana", 0.50, 200)

# Python allocates memory for these objects automatically when we create them
print(f"Product 1: {product1}")
print(f"Product 2: {product2}")

# Check memory usage of product1 and product2
print(f"Memory used by product1: {sys.getsizeof(product1)} bytes")
print(f"Memory used by product2: {sys.getsizeof(product2)} bytes")

# 2. **Reference Counting**: Both `product1` and `product2` are referenced here, so their reference count is 2 each
# In Python, when you assign an object to a variable, that variable holds a reference to the object

# Let's make product1 point to product2

import sys
print(f"Reference count for product1 (Banana object): {sys.getrefcount(product1)}")

print(f"Product 1 (after reassigning): {product1}")
product1 = product2

# Now, product1 and product2 are pointing to the same object (the "Banana" product)
print(f"Product 1 (after reassigning): {product1}")

# At this point, the reference count of the object containing "Banana" has increased to 2.
# product1 and product2 both refer to the same object.

# 3. **Deallocation & Garbage Collection**:
# Now let's delete product2, which will reduce the reference count of the "Banana" object.

del product2  # Delete the reference to "Banana"

# After `del product2`, the reference count of the "Banana" product should drop to 1.
# product1 still references the "Banana" product, so the memory used by this object is still retained.

# 4. **Triggering Garbage Collection**:
# If there were any other unreferenced objects, Python’s garbage collector would clean them up.
gc.collect()  # Forces garbage collection to run

# After deleting product2, Python automatically manages memory and cleans up unreferenced objects.
# However, in this example, product1 is still referencing the "Banana" product.

# 5. **Check Reference Count of Objects**:
# We can manually check the reference count of an object using sys.getrefcount() to see how many references are still pointing to the object.

import sys
print(f"Reference count for product1 (Banana object): {sys.getrefcount(product1)}")

# 6. **Cleaning Up & Memory Deallocation**:
# Now, if we delete `product1`, we free the last reference to the "Banana" object.
# This reduces the reference count to zero, and Python will automatically reclaim the memory.

del product1  # Delete the last reference

# 7. **Memory After Deallocation**:
gc.collect()  # Running garbage collection again (though Python usually does this automatically)
print("Garbage collection has been triggered, and memory is cleaned up.")

# 1. Memory Allocation:

# What it means: When you create an object like product1 or product2, Python gives them memory to store their data (like the name, price, and quantity).
# In simpler terms: Think of memory allocation as renting space in a building to store your stuff.
# Each product is assigned space in the building (the computer's memory).

# 2. Reference Counting:

# What it means: Every time you assign an object to a variable,
# Python keeps track of how many times that object is being used or referenced.
# This is called "reference counting."
# In simpler terms: Imagine you have a toy (the object) and you give it to two friends (variables like product1 and product2).
# The toy's reference count is 2 because both friends have it.
# When you reassign product1 to product2, both are holding onto the same toy, so the reference count increases to 2 for that toy.


# 3. Deallocation:

# What it means: When you remove a reference to an object (for example, using del), Python lowers the reference count for that object. If the reference count drops to zero, Python knows that object is no longer needed, and it can free up the memory.
# In simpler terms: If you take back the toy from one friend (like deleting product2),
# the toy's reference count goes down by 1. But if one friend is still holding the toy (like product1),
# it won’t be thrown away yet.

# 4. Garbage Collection:

# What it means: Python automatically cleans up memory that is no longer being used. This is called "garbage collection." It happens when there are no more references to an object, but you can also manually tell Python to do it using gc.collect().
# In simpler terms: Imagine there’s a garbage collector in your building who picks up all the trash (unneeded objects). He comes in and cleans up when no one is using the stuff (no references to the object), but you can also ask him to come early if needed.


# 5. Checking Reference Count:
# What it means: You can check how many references are still pointing to an object using sys.getrefcount(). Even if you delete one reference (like product2), the object might still be referenced elsewhere (like product1), so the object isn't deleted yet.
# In simpler terms: You can count how many people are still holding the toy. If two people are holding it, it won’t be thrown away until both let go of it.

# 6. Memory Deallocation After All References are Removed:
# What it means: Once all references to an object are deleted, its reference count drops to zero, and Python can safely free the memory.
# In simpler terms: Once both friends let go of the toy (deleting all references like product1 and product2), the toy will be thrown away (memory is freed), because no one is using it anymore.
# Summary Example in Simple Terms:
# Creating Objects (Memory Allocation):
# You have a toy (object), and you store it in two rooms (variables).
# Reference Counting:
# Both rooms are holding onto the same toy. The toy’s reference count is 2.
# Deleting a Reference (Deallocation):
# One room gives back the toy, so now only one room is holding onto it (reference count goes down).
# Garbage Collection:
# When both rooms give up the toy, the garbage collector comes and picks it up.
# Checking Reference Count:
# You check how many rooms are holding the toy.
# Final Memory Cleanup:
# When no one is holding the toy anymore, it’s thrown away (memory is freed).