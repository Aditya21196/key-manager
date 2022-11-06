# Key Manager
This library creates a simple key manager so that the actual key is hidden from the code. This was done as a part of the homework for Data Engineering class at NYU

### Installation
```
pip install ac8593_key_manager==0.2.0   
```

### Get started
Suppose Max wants to hide the key from his code. All he needs to do is create a .txt file and put his key in that file.
Then, he can add the name of the key file to the .gitginore. This ensures that his key does not get pushed to git and can be
passed around independantly of the code he writes. Moreover, people can use their own keys too without having to change the code!

Let's say Max saves his key in max_api_key.txt

```Python
from ac8593_key_manager import KeyManager

# Instantiate a KeyManager object
key_manager = KeyManager('max_api_key.txt')

# Call the get_key method to get the key. This key can be used to build the Polygon API client
key = key_manager.get_key()
```