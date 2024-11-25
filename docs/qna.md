## QnA
### 1. Do I need to install Python to use it?
Yes.

### 2. Can I use external Python libraries?
Yes, you can install it as usual (for example, via *pip*)

### 3. Can I use it as client-side module?
No, it doesn't support any client-side functionality, and there's no plans to add it for now due to security reasons and technical difficulties with client-side C++ modules.

### 4. Can I use it along side with Squirrel?
No, in most cases you can't. This module do call Squirrel's root table and const table directly, but there's no way to transfer data between Python and Squirrel (such as variables or class instances). 
But, if you want to use Squirrel and Python separately without data sharing, it should be ok (untested).