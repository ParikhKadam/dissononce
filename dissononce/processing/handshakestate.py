from dissononce.processing.handshakepatterns.handshakepattern import HandshakePattern

from dissononce.dh.keypair import KeyPair
from dissononce.dh.key_public import PublicKey

import logging

logger = logging.getLogger(__name__)
logging.getLogger('transitions').setLevel(logging.INFO)


class HandshakeState(object):
    def initialize(self, handshake_pattern, initiator, prologue, s, e=None, rs=None, re=None):
        """
        :param handshake_pattern: valid handshake_pattern
        :type handshake_pattern: HandshakePattern
        :param initiator: boolean specifying this party's role as either initiator or responder
        :type initiator: bool
        :param prologue: prologue byte sequence which may be zero-length, or which may contain context information
        that both parties want to confirm is identical
        :type prologue: bytes
        :param s: local static key pair
        :type s: KeyPair
        :param e: local ephemeral key pair
        :type e: KeyPair | None
        :param rs:  remote party's static public key
        :type rs: PublicKey | None
        :param re: remote party's ephemeral public key
        :type re: PublicKey | None
        :return:
        :rtype:
        """

    @property
    def rs(self):
        return None

    @property
    def re(self):
        return None

    @property
    def s(self):
        return None

    @property
    def e(self):
        return None

    def write_message(self, payload, message_buffer):
        """
        :param payload:
        :type payload: bytes
        :param message_buffer:
        :type message_buffer: bytearray
        :return:
        :rtype: tuple | None
        """
    def read_message(self, message, payload_buffer):
        """
        :param message:
        :type message: bytes
        :param payload_buffer:
        :type payload_buffer: bytearray
        :return:
        :rtype: tuple | None
        """
