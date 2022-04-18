from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from brownie import network
import pytest
import time


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
