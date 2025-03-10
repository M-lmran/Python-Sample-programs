from smsframework import OutgoingMessage
from smsframework import Gateway
from smsframework import ClickatellProvider

gateway = Gateway()
gateway.add_provider('main', ClickatellProvider)
gateway.send(OutgoingMessage("9566661856", "hi, testing from my laptop"))

