
methods {
    // envfree functions
    function balanceOf(address) external returns uint256 envfree;
}

invariant address0has0balance()
    balanceOf(0) == 0;