RATTE (Remote Administration Tool Tommy Edition) is a payload and third party module added/created to SET by 
Thomas Werth.

A couple things to note about RATTE is that it only works from inside to out on the Internet type scenarios. For
example, you would not receive a connection back if you were on the same network however it's main purpose and
design is to completely evade egress and firewall based restrictions by leveraging purely HTTP communications for 
the commands back and forth. 

Some important things to reference is that when RATTE is executed, it injects itself into FireFox and IE and replaces
the executables with a portion of its own code in it as well. So when the victim clicks on firefox or internet explorer
it will contain portions of RATTE inside of it.

RATTE relies on communications to microsoft.com to identify the path out of the network.
