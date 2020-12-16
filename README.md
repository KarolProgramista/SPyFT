# SPyFTI
Simple Python File Transceiver Interface is a peace of software with what you can 
sent or receive files through net using simple classes and functions.
### Installation
Firstly you need to clone this repository, then to install module run  
```bash
python3 setup.py install
``` 
#### Configuration
To config some common settings as transfer speed, edit settings.py in SPyFT folder
### Documentation
The whole module is very simple, you have only two classes
``Reciever`` and ``Sender``
#### Receiver
This object receives sent file  
``Reciver.Receiver(port, save_path)``  
Both of these parameters are optional, if not given Receiver will use the default ones form
settings.py.  
It has three functions we can use
```python
Receiver.receiver_mainloop(None)
Receiver.receive_file(None)
Receiver.receive_file_as_string(None)
```
Receiver.receiver_mainloop() just infintly downloads files and saves them in specified 
earlier folder.

Receiver.receive_file() do the same as above but once

Receiver.receive_file_as_string() receives file and returns list  
``[received_file_content, received_file_name]``  
and if something gone wrong it will return -1 in both list indexes

Receiver also have errno variable which contain the last error code
Error Codes can be find in settings.py

##### Example
```python
from SPyFT.Reciver import Receiver
r = Receiver()
r.receiver_mainlopp()
```
This example shows how to setup basic file receiving server in 3 lines

#### Sender
Object sends specified file  
``Sender.Sender(port, ip)``
Both of parameters are optional, for port will be used default one
and for ip - your local ip.  
Sender has only one function  
``Sneder.send(file_path)``  
This function will send the specified file and it will be send with it's original name
so you can save it with the same name one server side.
##### Example
```python
from SPyFT.Sender import Sender
s = Sender()
s.send("path_to_file")
```
And again in three lines of code you are able to send the file

### Enjoy!