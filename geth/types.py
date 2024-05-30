from __future__ import (
    annotations,
)

from typing import (
    IO,
    Any,
    Literal,
    TypedDict,
    Union,
)

IO_Any = Union[IO[Any], int, None]


class GethKwargsTypedDict(TypedDict, total=False):
    allow_insecure_unlock: bool | None
    autodag: bool | None
    cache: int | None
    data_dir: str | None
    dev_mode: bool | None
    gcmode: Literal["full", "archive"] | None
    geth_executable: str | None
    ipc_disable: bool | None
    ipc_path: str | None
    max_peers: str | None
    mine: bool | None
    miner_etherbase: int | None
    network_id: str | None
    nice: bool | None
    no_discover: bool | None
    password: bytes | str | None
    port: str | None
    preload: str | None
    rpc_addr: str | None
    rpc_api: str | None
    rpc_cors_domain: str | None
    rpc_enabled: bool | None
    rpc_port: str | None
    shh: bool | None
    stdin: str | None
    suffix_args: list[str] | None
    suffix_kwargs: dict[str, Any] | None
    tx_pool_global_slots: int | None
    tx_pool_price_limit: int | None
    unlock: str | None
    verbosity: int | None
    ws_addr: str | None
    ws_api: str | None
    ws_enabled: bool | None
    ws_origins: str | None
    ws_port: str | None


class GenesisDataTypedDict(TypedDict, total=False):
    alloc: dict[str, dict[str, Any]]
    coinbase: str
    config: dict[str, Any]
    difficulty: str
    extraData: str
    gasLimit: str
    mixhash: str
    nonce: str
    parentHash: str
    timestamp: str
