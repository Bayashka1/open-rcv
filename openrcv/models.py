
import json
from random import randint


def to_json(obj):
    return json.dumps(obj, indent=4)


class JsonMixin(object):

    def to_json(self):
        return to_json(self.__jsobj__())


class BallotList(JsonMixin):

    """

    This should be used only for tests and small sets of ballots.
    For large numbers of ballots, ballot data should be kept on the
    file system for memory reasons.

    """

    def __init__(self, ballots=None):
        if ballots is None:
            ballots = []
        self.ballots = ballots

    def __jsobj__(self):
        return [" ".join((str(c) for c in ballot)) for ballot in self.ballots]


# TODO: document what this class is for.  For test data input?
# TODO: add a dict of who breaks ties in each round there is a tie.
class MinimalContest(JsonMixin):

    def __init__(self, candidates, ballots):

        """
        Arguments:
          candidates: integer number of candidates

        """

        self.ballots = ballots
        self.candidates = candidates

    def __jsobj__(self):
        return {
            "ballots": self.ballots.__jsobj__(),
            "candidates": self.candidates,
        }


class ContestInfo(object):

    """
    Attributes:
      candidates: a list of the names of all candidates, in numeric order.
      name: name of contest.
      seat_count: integer number of winners.

    """

    ballot_count = 0

    def __init__(self):
        pass

    def get_candidates(self):
        """Return an iterable of the candidate numbers."""
        return range(1, len(self.candidates) + 1)

    # TODO: look up the proper return type.
    def __repr__(self):
        return self.name


# TODO: remove "Test" from the name since this is used in real code.
class TestRoundResults(JsonMixin):

    """
    Represents the results of a round for testing purposes.

    """

    def __init__(self, totals):
        """
        Arguments:
          totals: dict of candidate number to vote total.

        """
        self.totals = totals

    def __jsobj__(self):
        return {
            "totals": self.totals,
        }


# TODO: remove "Test" from the name since this is used in real code.
class TestContestResults(JsonMixin):

    """
    Represents contest results for testing purposes.

    """

    def __init__(self, rounds):
        """
        Arguments:
          rounds: an iterable of TestRoundResults objects.

        """
        self.rounds = rounds

    def __jsobj__(self):
        return {
            "rounds": [r.__jsobj__() for r in self.rounds],
        }
