
methods {
    function bids(address) external returns uint256 envfree;
    function highestBid() external returns uint256 envfree;
    function highestBidder() external returns address envfree;
}


invariant highestBidIsHighest(address bidder)
    highestBid() >= bids(bidder);

invariant bidsOfHighestBidderIsHighest()
    highestBidder() != 0 => bids(highestBidder()) == highestBid();