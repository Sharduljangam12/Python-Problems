from datetime import datetime

print(dir(datetime))  #dir will give the list of all the methods present in that module [dir() → “Show me what tools are available”], dir() returns a list of attributes and methods of an object (module, class, or instance)

print(help(datetime)) #Help will give me the detailed information about the module [help() → “Explain how to use those tools”], help() provides detailed documentation about the object, including how its methods work

'''🔹 dir(datetime)

👉 Returns a list of all attributes inside the datetime class
This includes:

methods (now, strftime, etc.)
internal attributes (__add__, __str__, etc.)

👉 Think:

“What can I use from this object?”

🔹 help(datetime)

👉 Shows detailed documentation:

what the class does
method descriptions
parameters
usage

👉 Think:

“How does this actually work?”'''