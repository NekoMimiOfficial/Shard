# Project Shard  
Shard: a better solution for transfering files and data  
it aint magic, it just works smarter.. ig?  
a file repersents a crystal which gets cut into smaller shards which are 4kB in size, any data that cant fit into a shard is called dust, data inside crystals/shards/dust are called essence  
why ?  
it just sounds nice ig.. and it describes how this project works at its core  

# Important Notice !  
were iz da cod ?  

there is no code on the master branch instead each branch implements Shard to a certain platform or language so you'll have to browse the branches :3  

# The Components  
- server:  
an app to serve and convert files into its repective shard form  
- client:  
an app to connect to the server and pull shards multithreaded-ly  
- ndtp: 
the NekoDataTransferProtocol, the transporter of shards  

# Advantages  
Project Shard allows for faster downloading and recoverable downloading sessions, whether it takes days, months, years it will never fail as long as the file remains on the server  
you can start downloading on a device then copy the shards and resume from any other device  
*Note: This project doesnt do compression  
*Note: by using the ndt protocol you agree to our TERMSOFCONDITION.md  

# Interested?  
no u not lol  

# ToDo List  
uhh.. i have it on my goog tasks but uhh.. ill write some things ig..  
```
[ ] add encryption  
[ ] break crystal into shards  
[ ] construct crystal from shards  
[ ] ndtp  
[ ] user accounts  
[ ] configurable polling  
[ ] write a damn working config lexer -> parser  
[ ] maybe.. just maybe.. android app  
```

# You Like Neko?  
you can always show your support by reaching out on my email or my mastodon account (@nekomimi@sakurajima.moe) or star-ing etc..  
if you'd like to donate me money please send it to a chariy instead  

you can always find my links at my Personal GitHub repo or my website  
