# n-queen-microservice
This is an example of a microservice for PV217 Service Oriented Architecture

# Requeriments
The python package:
- [Hug](https://github.com/timothycrosley/hug)

# How to set it up

Clone the repository:
```{bash}
git clone https://github.com/i32ropie/n-queen-microservice
```

Compile the tool that solves the N-Queen problem
```{bash}
make
```

Run the server
```{bash}
./run.sh
```

# Usage
After running the server, you can go to your **$HOST:8000** ($HOST is where you execute the microservice)
to see the documentation that Hug creates. Following it, you can see that for getting the solutions
for the N-Queen problem, you just go to **$HOST:8000/get_n_queen_solutions** and use the parameter
n to specify the N. For example given **$HOST:8000/get_n_queen_solutions?n=6**, the microservice
will show us the 4 solutions.

<img src="https://i.imgur.com/FsgLlkK.png">

# Disclaimer
- This will run Hug server, which shouldn't be used for production, just for testing. You could use
uwsgi as explained [here](https://github.com/timothycrosley/hug#running-hug-with-other-wsgi-based-servers).
- The tool used for solving the N-Queen problem is an adapted version of [this](https://github.com/i32ropie/Algoritmica/tree/master/p6).

# Testing
For testing reasons I coded a [Telegram](https://telegram.org/) bot to show that the microservice
works and can be used.

The code is provided and a [video](https://youtu.be/RJrHfyCAJv4) with an example too.
