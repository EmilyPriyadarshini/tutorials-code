
methods
{
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function totalVotes() external returns (uint256) envfree;
}

ghost bool votedChanged {
    init_state axiom !votedChanged;
}

ghost bool voteCalled {
    init_state axiom !voteCalled;
}

hook Sstore _hasVoted[KEY address voter]
    bool newVal (bool oldVal) {
    if (votedChanged == false) {
        votedChanged = true;
        voteCalled = true;
    }
}

invariant ifHasVotedChangedThenVoteCalled()
    votedChanged => voteCalled;
