from cosm.query.rest_client import QueryRestClient
from cosm.staking.interface import Staking

from cosmos.staking.v1beta1.query_pb2 import (
    QueryDelegationRequest,
    QueryDelegationResponse,
    QueryDelegatorDelegationsRequest,
    QueryDelegatorDelegationsResponse,
    QueryDelegatorUnbondingDelegationsRequest,
    QueryDelegatorUnbondingDelegationsResponse,
    QueryDelegatorValidatorRequest,
    QueryDelegatorValidatorResponse,
    QueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse,
    QueryHistoricalInfoRequest,
    QueryHistoricalInfoResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryPoolRequest,
    QueryPoolResponse,
    QueryRedelegationsRequest,
    QueryRedelegationsResponse,
    QueryUnbondingDelegationRequest,
    QueryUnbondingDelegationResponse,
    QueryValidatorDelegationsRequest,
    QueryValidatorDelegationsResponse,
    QueryValidatorRequest,
    QueryValidatorResponse,
    QueryValidatorsRequest,
    QueryValidatorsResponse,
    QueryValidatorUnbondingDelegationsRequest,
    QueryValidatorUnbondingDelegationsResponse,
)
from google.protobuf.json_format import Parse


class StakingRestClient(Staking):
    """Staking REST API module."""

    API_URL = "/cosmos/staking/v1beta1"

    def __init__(self, rest_api: QueryRestClient):
        """Initialize."""
        self._rest_api = rest_api

    def Validators(self, request: QueryValidatorsRequest) -> QueryValidatorsResponse:
        """Validators queries all validators that match the given status."""
        json_response = self._rest_api.get(f"{self.API_URL}/validators")
        return Parse(json_response, QueryValidatorsResponse())

    def Validator(self, request: QueryValidatorRequest) -> QueryValidatorResponse:
        """Validator queries validator info for given validator address."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}"
        )
        return Parse(json_response, QueryValidatorResponse())

    def ValidatorDelegations(
        self, request: QueryValidatorDelegationsRequest
    ) -> QueryValidatorDelegationsResponse:
        """ValidatorDelegations queries delegate info for given validator."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations"
        )
        return Parse(json_response, QueryValidatorDelegationsResponse())

    def ValidatorUnbondingDelegations(
        self, request: QueryValidatorUnbondingDelegationsRequest
    ) -> QueryValidatorUnbondingDelegationsResponse:
        """ValidatorUnbondingDelegations queries unbonding delegations of a validator."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/unbonding_delegations"
        )
        return Parse(json_response, QueryValidatorUnbondingDelegationsResponse())

    def Delegation(self, request: QueryDelegationRequest) -> QueryDelegationResponse:
        """Delegation queries delegate info for given validator delegator pair."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations/{request.delegator_addr}"
        )
        return Parse(json_response, QueryDelegationResponse())

    def UnbondingDelegation(
        self, request: QueryUnbondingDelegationRequest
    ) -> QueryUnbondingDelegationResponse:
        """UnbondingDelegation queries unbonding info for given validator delegator pair."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_addr}/delegations/{request.delegator_addr}/unbonding_delegation"
        )
        return Parse(json_response, QueryUnbondingDelegationResponse())

    def DelegatorDelegations(
        self, request: QueryDelegatorDelegationsRequest
    ) -> QueryDelegatorDelegationsResponse:
        """DelegatorDelegations queries all delegations of a given delegator address."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegations/{request.delegator_addr}"
        )
        return Parse(json_response, QueryDelegatorDelegationsResponse())

    def DelegatorUnbondingDelegations(
        self, request: QueryDelegatorUnbondingDelegationsRequest
    ) -> QueryDelegatorUnbondingDelegationsResponse:
        """DelegatorUnbondingDelegations queries all unbonding delegations of a given delegator address."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/unbonding_delegations"
        )
        return Parse(json_response, QueryDelegatorUnbondingDelegationsResponse())

    def Redelegations(
        self, request: QueryRedelegationsRequest
    ) -> QueryRedelegationsResponse:
        """Redelegations queries redelegations of given address."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/redelegations"
        )
        return Parse(json_response, QueryRedelegationsResponse())

    def DelegatorValidators(
        self, request: QueryDelegatorValidatorsRequest
    ) -> QueryDelegatorValidatorsResponse:
        """DelegatorValidators queries all validators info for given delegator address."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/validators"
        )
        return Parse(json_response, QueryDelegatorValidatorsResponse())

    def DelegatorValidator(
        self, request: QueryDelegatorValidatorRequest
    ) -> QueryDelegatorValidatorResponse:
        """DelegatorValidator queries validator info for given delegator validator pair."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_addr}/validators/{request.validator_addr}"
        )
        return Parse(json_response, QueryDelegatorValidatorResponse())

    def HistoricalInfo(
        self, request: QueryHistoricalInfoRequest
    ) -> QueryHistoricalInfoResponse:
        """HistoricalInfo queries the historical info for given height."""
        json_response = self._rest_api.get(
            f"{self.API_URL}/historical_info/{request.height}"
        )
        return Parse(json_response, QueryHistoricalInfoResponse())

    def Pool(self, request: QueryPoolRequest) -> QueryPoolResponse:
        """Pool queries the pool info."""
        json_response = self._rest_api.get(f"{self.API_URL}/pool")
        return Parse(json_response, QueryPoolResponse())

    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """Parameters queries the staking parameters."""
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return Parse(json_response, QueryParamsResponse())
