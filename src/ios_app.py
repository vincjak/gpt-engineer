import gptengineer
import ios_adapter
import ios_interface
import config
import utils

class IOSApp:
    def __init__(self):
        self.config = config.load_config()
        self.utils = utils.load_utils()
        self.gptengineer = gptengineer.init(self.config, self.utils)
        self.ios_adapter = ios_adapter.init(self.config, self.utils)
        self.ios_interface = ios_interface.init(self.config, self.utils)

    def run(self):
        self.ios_interface.display_welcome_message()
        while True:
            user_input = self.ios_interface.get_user_input()
            if user_input == 'exit':
                break
            response = self.gptengineer.generate_response(user_input)
            adapted_response = self.ios_adapter.adapt_response(response)
            self.ios_interface.display_response(adapted_response)

if __name__ == "__main__":
    app = IOSApp()
    app.run()