<b>Context Managers</b>
--Use to allocate and release resources precisely
<br>
The most widely used context manager is <b>with</b>

Every context manager must have at least __enter__ and __exit__ methods defined.

<code><b>__enter__</b></code> takes object reference while <code><b>__exit__</code></b> takes 4 arguments self, exception_type, exception_value and trackback value

The with statement stores the __exit__ method of File class.</br>
It calls the __enter__ method of File class.</br>
__enter__ method opens the file and returns it.</br>
the opened file handle is passed to opened_file.</br>
we write to the file using .write()</br>
with statement calls the stored __exit__ method.</br>
the __exit__ method closes the file.
