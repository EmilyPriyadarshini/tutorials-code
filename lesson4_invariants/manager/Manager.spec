/**
 * # Spec for funds manager `IManager.sol`
 */
methods {
    function getCurrentManager(uint256) external returns (address) envfree;
    function getPendingManager(uint256) external returns (address) envfree;
    function isActiveManager(address) external returns (bool) envfree;
}

invariant no2FundsHaveSameManager(uint256 fundId1, uint256 fundId2)
    getCurrentManager(fundId1) == getCurrentManager(fundId2)
    => getCurrentManager(fundId1) != 0
    => getCurrentManager(fundId2) != 0
    => fundId1 == fundId2
    {
        preserved
        {
        requireInvariant managerIsActive(fundId1);
        requireInvariant managerIsActive(fundId2);
        }
    }

invariant managerIsActive(uint256 fundId)
    getCurrentManager(fundId) != 0
    => isActiveManager(getCurrentManager(fundId)) == true
    {
        preserved claimManagement(uint256 fundId0) with (env e)
        {
            requireInvariant no2FundsHaveSameManager(fundId, fundId0);
        }
    }