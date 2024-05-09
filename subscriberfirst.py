import paho.mqtt.client as mqtt

# MQTT 브로커에서 메시지가 도착했을 때 호출되는 콜백 함수
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload.decode("utf-8")) + "' on topic '" + message.topic + "'")

# MQTT 브로커 주소와 포트
broker_address = "localhost"
port = 1883

# MQTT 클라이언트 생성 (콜백 API 버전 5 사용)
client = mqtt.Client(protocol=mqtt.MQTTv5)
client.on_message = on_message

# MQTT 브로커에 연결
client.connect(broker_address, port)

# 구독할 토픽
topic = "test/topic"

# 토픽 구독
client.subscribe(topic)

# 메시지 수신을 계속해서 대기
client.loop_forever()