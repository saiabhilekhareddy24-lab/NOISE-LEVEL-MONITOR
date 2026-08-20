class NoiseLevelMonitor:
    def __init__(self):
        self.safe_limit = 85

    def classify_noise(self, db):
        if db < 40:
            return "QUIET"
        elif db < 60:
            return "MODERATE"
        elif db <= 85:
            return "LOUD"
        else:
            return "DANGEROUS"

    def monitor(self, db):
        status = self.classify_noise(db)
        print(f"Noise Level: {db:.1f} dB -> {status}")
        return status


if __name__ == "__main__":
    monitor = NoiseLevelMonitor()

    noise_values = [35.2, 52.8, 72.4, 91.6, 45.5, 88.2]

    for noise in noise_values:
        monitor.monitor(noise)
