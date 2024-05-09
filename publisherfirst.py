import paho.mqtt.publish as publish

# MQTT 브로커 주소와 포트
broker_address = "localhost"
port = 1883

# 발행할 토픽과 메시지
topic = "test/topic"
message = "jungbin first MQTT for subscriber"

# 메시지 발행
publish.single(topic, message, hostname=broker_address, port=port)