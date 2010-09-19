'''
TODO: 	Implement shorthand char list. e.g. [a-zA-Z]
		Implement start word e.g  ***ben*****  in this example, we replace only the asterisks
		Implement multi-processing. Allow users to generate the list in chunks, each chunk on its own CPU
		Implement function hook. i.e. A user can pass in a function that will apply to each string
		generated with the generator. e.g. p.generator(function_call=compare_md5, *kwargs) 
		
		Implement the ability to generate a custom dictionary file. A dictionary file of 15 char
		strings with the full ascii char set will be to large. So, using a starting string we can 
		add a header listing the charset and the number of links in the chain.
		Each row will represent a chain of len N.
		Once we have a reduced size file, we can pass it into a function that can generate the next
		link in the chain.
		
		file example:
		charset=abcdef0123456789	chainlen=10		stringlen=2		direction=forward
		aa
		a4
		be
		b8
	    ...
	    
	    Once the file is done, we can iterate over it how we want. We can do all the strings first 
	    and look for a match or we can iterate over chains.
	    
		
		
veganhacker[AT]gmail[DOT]com

Copyright 2010 Ben Lambert 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 
Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

'''

class PasswordDictionary():
    def __init__(self, char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+=-`<>,./?;:\'"[]{}|\\ ', 
                 string_length = 3):
        self.string_len = string_length
        self.char_picklist = char_list
           
    def product(self, *args):
        if not args:
            return iter(((),)) # yield tuple()
        return (items + (item,) for items in self.product(*args[:-1]) for item in args[-1])
	    
    def generator(self, direction='forward'):
        if direction == 'backward':
        ## return z-a
            return self.product(*[self.char_picklist[::-1] for i in xrange(self.string_len)])
        ## Return a-z
        else: return self.product(*[self.char_picklist for i in xrange(self.string_len)])
        
        
if __name__ == '__main__':	
    pass