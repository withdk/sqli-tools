# sqli-tools 

Introduction:

Security researchers, developers and testers have spent considerable time 
coming up with techniques to identify and test for Blind SQL Injection (BSQLI), 
using techniques such as union selects, timing, Boolean, and out-of-band 
conditions. As if Blind SQL Injection was not challenging enough to find, 
keyword blacklisting & application filtering mechanisms are becoming more 
popular and often require custom payloads to exploit rather then the techniques 
employed by existing industry tools. 

The sqli-tools toolkit is really a proof of concept idea to try fill this gap 
by letting the tester identify and craft the payload and then using these tools 
to automate exfiltration. To further clarify, sqli-tools aids in testing and 
verifying the level of risk a BSQLI vulnerability poses, it not designed to 
find vulnerabilities as there are many tools that already focus on this. 

Tools:

bsqli-bruter.py. A proof of concept tool that automates the exfiltration of 
data through Boolean blind SQL injection where the LIKE clause is being used to 
test a Boolean condition.

Example POST request with a vulnerable 'sql' parameter.
$ python bsqli-bruter.py -u http://somesite.com/somepath.ext -m 'score' -d 
"sql=select+name+from+bbc+where+name+LIKE+'{*}%'" -v
	
Example GET request with a vulnerable 'sql' parameter.
$ python bsqli-bruter.py -u 
http://somesite.com/somepath.ext?sql=select+name+from+bbc+where+name+LIKE+'{*}%
' -m 'score' -v

TODO:

If the opportunity arises additional tools will be added to the toolkit, but 
this is it for now :)

Homepage:
https://github.com/davidkierznowski/sqli-tools
