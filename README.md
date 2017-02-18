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

# About

Application security testing requires knowledge of many aspects of computing systems and networks. Normally, when analyzing applications that have a back end database, you will check for SQL injection vulnerabilities. Most applications will do a good job with input filtering at the various layers. There will be checks in the client side, the server side, and all the other layers from middleware down to the database. In between, you'll also have various security defenses such as firewalls, web application firewalls, and intrusion detection or prevention systems enforcing various types of size, syntactic, and grammar restrictions. Additionally, there will be plain whitelist and blacklist approaches across these layers to further hinder your ability as an adversary to successfully compromise the target application. Usually, you'll also find the database errors to be generic and non-descript when sent back to the client as one of the last layers of security. This will usually be a boolean true or false, or some sign of success of failure of your request. But this is where things get interesting.

After maneuvering through all these restrictions and finding some form of SQL injection to work, you will find yourself at a very limited position to continue. Most SQL injection testing tools will help automate and find an input validation issue that will give you a starting point. You'll find that a specific way to input the data will return some form of failure or false flag. However, this will not be enough to know what it does, what the structure of the database is, or what the underlying data actually is. Being able to derive valuable information will lend itself to your ability to automate and enumerate requests and results while keeping track of state information. There aren't many tools out there that allow you to do this.

As part of a proof-of-concept tool, @withdk put together a quick SQLI data extraction tool that you can configure and train using a found SQL injection vulnerability to automate, hold state, and further derive more information from the binary results of the application. Finally, this helps reach the ultimate objective to exfiltrate data. It is a nice proof of concept to show that you can build something quick using Python and some basic libraries and an indicator to the security community to build more capabilities like this into their testing tools.

You can find the Blind SQL Injection (BSQLI) Exploration Tool here: https://github.com/withdk/sqli-tools.

You can also find more information on designing software more securely at these links:

OWASP : https://www.owasp.org/index.php/Main_Page
Secure Software Design and Programming : https://www.dwheeler.com/secure-class/

@DrCruft and @withDK

## Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
