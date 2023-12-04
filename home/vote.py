from django.conf import settings
from .models import Subscription

class Vote(object):
    def __init__(self, request):
        self.session = request.session
        vote = self.session.get(settings.VOTE_SESSION_ID)

        if not vote:
            vote = self.session[settings.VOTE_SESSION_ID] = {}

        self.vote = vote

    def __iter__(self):
        for p in self.vote.keys():
            self.vote[str(p)]['subscription'] = Subscription.objects.get(pk=p)

        for voters in self.vote.values():
            voters['total_vote'] = int(voters['subscriber_votes'].vote_count - voters['vote_counter'])

        yield voters

    def __len__(self):
        return sum(voters['vote_counter'] for voters in self.vote.values())

    def save(self):
        self.session[settings.VOTE_SESSION_ID] = self.vote
        self.session.modified = True

    def update(self, vote_id, vote_add=1, update_vote=False):
        vote_id = str(vote_id)

        if vote_id not in self.vote:
            self.vote[vote_id] = {'vote_counter': int(vote_add), 'id': vote_id}

        if update_vote:
            self.vote[vote_id]['vote_counter'] += int(vote_add)

            if self.vote[vote_id]['vote_counter'] == 0:
                self.remove(vote_id)

        self.save()

    def reduce(self, voters_id, sub=-1, reduce_sub=False):
        voters_id = str(voters_id)

        if voters_id not in self.vote:
                self.vote[voters_id] = {'vote_counter': int(sub), 'id':voters_id}


        if reduce_sub:
                self.vote[voters_id]['vote_counter'] -= int(sub)

        if self.vote[voters_id]['vote_counter'] == 0:
                    self.remove(voters_id)

        self.save()


    def total_votes(self):
        for p in self.vote.keys():
             self.vote[str(p)]['subscription'] = Subscription.objects.get(pk=p)

        return int(sum(voters['votes'].vote_count - voters['vote_counter'] for voters in self.vote.values())) 