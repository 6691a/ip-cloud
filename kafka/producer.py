from confluent_kafka import Producer
from confluent_kafka.serialization import Serializer


class BaseProducer(object):
    def __init__(
        self,
        *,
        topic: str,
        bootstrap_servers: list[str],
        client_id: str,
        key_serializer: Serializer,
        value_serializer: Serializer,
    ):
        self.topic = topic
        self.producer = Producer(
            {
                "bootstrap.servers": ",".join(bootstrap_servers),
                "client.id": client_id,
            }
        )
        self.key_serializer = key_serializer
        self.value_serializer = value_serializer

    def produce(self, key: str, value: str, partition: int = -1, timestamp=0, headers=None, on_delivery=None):
        self.producer.produce(
            self.topic,
            key=key,
            value=value,
            partition=partition,
            timestamp=timestamp,
            headers=headers,
            on_delivery=on_delivery,
        )

    def flush(self, timeout: float):
        self.producer.flush(timeout)
