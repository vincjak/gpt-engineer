import gptengineer
import utils
import config
import ios_adapter
import ios_interface
import ios_app

def main():
    # Initialize the modules
    gptengineer.init()
    utils.init()
    config.init()
    ios_adapter.init()
    ios_interface.init()
    ios_app.init()

    # Run the modules
    gptengineer.run()
    utils.run()
    config.run()
    ios_adapter.run()
    ios_interface.run()
    ios_app.run()

if __name__ == "__main__":
    main()