from sleekxmpp import ClientXMPP


class XMPPUserRegistration(ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)

        self.add_event_handler("session_start", self.start)

    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.disconnect()


if __name__ == "__main__":
    # Replace these with your Prosody server details
    server = "localhost"
    jid = "agent1@" + server
    password = "password"  # Set the desired password for the new user

    xmpp = XMPPUserRegistration(jid, password)
    xmpp.register_plugin("xep_0077")  # In-band Registration

    print("antes do if")
    try:
        if xmpp.connect((server, 5222)):
            print("depois do if")
            xmpp.process(block=True)
            print("depois do xmpp.process")
        else:
            print("Unable to connect to the XMPP server.")
    except Exception as e:
        print(f"Error: {str(e)}")

    print("fim")
