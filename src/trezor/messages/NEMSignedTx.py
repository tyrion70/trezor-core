# Automatically generated by pb2py
import protobuf as p


class NEMSignedTx(p.MessageType):
    FIELDS = {
        1: ('data', p.BytesType, 0),
        2: ('signature', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 70

    def __init__(
        self,
        data: bytes = None,
        signature: bytes = None,
        **kwargs,
    ):
        self.data = data
        self.signature = signature
        p.MessageType.__init__(self, **kwargs)
