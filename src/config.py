```python
# This is the configuration file for the gptengineer application

class Config:
    def __init__(self):
        # Configuration for the GPT-Engineer
        self.gpt_engineer_config = {
            'model_name': 'gpt-3',
            'temperature': 0.5,
            'max_tokens': 200
        }

        # Configuration for the iOS application
        self.ios_app_config = {
            'app_name': 'GPTEngineer',
            'version': '1.0.0',
            'developer': 'Your Name'
        }

    def get_gpt_engineer_config(self):
        return self.gpt_engineer_config

    def get_ios_app_config(self):
        return self.ios_app_config
```