from .vote import Vote

def vote(request):
    return {'vote': Vote(request)}