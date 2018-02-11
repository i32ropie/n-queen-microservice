import hug
import os

# @hug.get('/')
# def help():
#     return "This microservice generates all the solutions for N-Queen problem given the N between 4 and 10. To try it, just click here: htpp://0.0.0.0:8000/8"

@hug.get()
def get_n_queen_solutions(n):
    """This microservice generates all the solutions for N-Queen problem given the N between 4 and 10."""
    try:
        n = int(n)
    except:
        return {"errors": "You must specify a number between 4 and 10"}
    if n < 4 or n > 10:
        return {"errors": "You must specify a number between 4 and 10"}
    else:
        output = {"success":[]}
        folder = os.popen('./main {}'.format(n)).read()
        for x in os.listdir(folder):
            with open('{}/{}'.format(folder, x)) as f:
                output["success"].append(f.read().rstrip('\n'))
        os.popen('rm -rf {}'.format(folder))
        return output
