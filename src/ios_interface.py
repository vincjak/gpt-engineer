import UIKit
from src import gptengineer, ios_adapter, config, utils

class GPTEngineerViewController: UIViewController {
    var gptEngineer: GPTEngineer!
    var config: Config!
    var utils: Utils!

    override func viewDidLoad() {
        super.viewDidLoad()
        self.init()
    }

    func init() {
        self.config = config.Config()
        self.utils = utils.Utils()
        self.gptEngineer = gptengineer.GPTEngineer(self.config, self.utils)
    }

    func run() {
        let adaptedGptEngineer = ios_adapter.adapt(self.gptEngineer)
        adaptedGptEngineer.run()
    }
}