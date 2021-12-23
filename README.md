# Crontab Bundle

Define crontab entries via Bundlewrap.

## Config
```python
node['example'] = {
    'metadata': {
        'crontab': {
            'daslampe': [
                {
                    'minute': '*/5',
                    'command': 'echo "Foobar"'
                },
            ],
            'root': [
                {
                    'minute': '00',
                    'hour': '00',
                    'dayOfMonth': '01',
                    'month': '1',
                    'dayOfWeek': '*',
                    'command': 'echo "Happy new year!"',
                },
            ],
        },
    },
}
```

Default values for `minute`, `hour`, `dayOfMonth`, `month` and `dayOfWeek` are `*`.