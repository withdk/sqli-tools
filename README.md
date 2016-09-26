      ____   _____  ____  _      _____ 
     |  _ \ / ____|/ __ \| |    |_   _|
     | |_) | (___ | |  | | |      | |  
     |  _ < \___ \| |  | | |      | |  
     | |_) |____) | |__| | |____ _| |_ 
     |____/|_____/ \___\_\______|_____|
                                   
    Example POST request with a vulnerable 'sql' parameter.
    $ python bsqli-bruter.py -u http://somesite/somepath.ext -m 'score' -d "sql=select+name+from+bbc+where+name+LIKE+'{*}%'" -v

    Example GET request with a vulnerable 'sql' parameter.
    $ python bsqli-bruter.py -u http://somesite/somepath.ext?sql=select+name+from+bbc+where+name+LIKE+'{*}%' -m 'score' -v

## Introduction:

Security researchers, developers and testers have spent considerable time coming up with techniques to identify and test for Blind SQL Injection (BSQLI), using techniques such as union selects, timing, Boolean, and out-of-band conditions. As if Blind SQL Injection was not challenging enough to find, keyword blacklisting & application filtering mechanisms are becoming more popular and often require custom payloads to exploit rather then the techniques employed by existing industry tools. 

The sqli-tools toolkit is really a proof of concept idea to try fill this gap by letting the tester identify and craft the payload and then using these tools to automate exfiltration. To further clarify, sqli-tools aids in testing and verifying the level of risk a BSQLI vulnerability poses, it not designed to find vulnerabilities as there are many tools that already focus on this. 

## Toolkit (singular for now)

___bsqli-bruter.py.___ A proof of concept tool that automates the exfiltration of 
data through Boolean blind SQL injection where the LIKE clause is being used to 
test a Boolean condition.

## Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
