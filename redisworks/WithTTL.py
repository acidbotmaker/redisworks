class WithTTL:
    ttl = None
    def __init__(self, value, ttl=None):
        self.value = value
        self.ttl = ttl